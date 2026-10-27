'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.resolve(__dirname,'..'),sim=path.resolve(process.env.SIMULATOR_DIR||path.join(root,'../fina'));
function payload(file,key){const c={window:{}};vm.createContext(c);vm.runInContext(fs.readFileSync(path.join(sim,file),'utf8'),c);return JSON.parse(JSON.stringify(c.window[key]));}
const D=payload('network/c5-data.js','C5Data'),story=payload('network/client-story.js','ClientStory'),M=require(path.join(sim,'network/c5-model.js'));
const read=f=>JSON.parse(fs.readFileSync(path.join(root,'Anexos',f),'utf8'));
const exercises=read('Ejercicios_Recuperacion_C5.json'),ipam=fs.readFileSync(path.join(root,'Anexos/Inventario_IPAM_Puertos.md'),'utf8');
for(const [variant,sites] of [['A',D.sites],['B',D.bSites]]){
 const cm=sites[0];
 test(variant+': alcance e inventario vigente',()=>{
  assert.equal(sites.length,23);assert.equal(sites.reduce((n,s)=>n+s.workstations,0),650);
  assert.equal(sites.reduce((n,s)=>n+s.after.routers,0),44);assert.equal(sites.reduce((n,s)=>n+s.after.switches,0),46);
  assert.equal(sites.reduce((n,s)=>n+s.after.ap_count,0),48);assert.equal(sites.reduce((n,s)=>n+s.wan_services.length,0),92);
  assert.equal(sites.reduce((n,s)=>n+(s.tunnels?.length||0),0),704);
  assert.equal(sites.reduce((n,s)=>n+s.after.routers_reused,0),variant==='A'?7:0);
  assert.equal(sites.reduce((n,s)=>n+s.after.switches_reused,0),variant==='A'?19:2);
 });
 test(variant+': presupuesto de presentación conciliado con el JSON público',()=>{
  const a=read('Presupuesto_C5_A.json'),b=read('Presupuesto_C5_B.json');
  const initial=variant==='A'?a.initial_outlay_gross_clp:b.totals.initial_outlay_gross_clp;
  const period=variant==='A'?a.scoped_cost_60_months_gross_clp:b.totals.scoped_cost_60_months_gross_clp;
  assert.deepEqual(story.budget[variant],{initial,monthly:a.wan.monthly_gross_clp,period});
  assert.equal(period,initial+11010123*60+(variant==='A'?50000000:25000000));
 });
 test(variant+': IPAM conserva direcciones de todos los puestos',()=>{
  const section=ipam.split('## Alternativa '+variant)[1].split('## Alternativa ')[0];
  for(const s of sites)for(const p of s.endpoints)for(const k of ['pc','phone','wifi_pc_reserved','wifi_phone_reserved'])assert.ok(section.includes(p[k]),s.id+' '+p[k]);
 });
 test(variant+': 4950 combinaciones WAN no vacías conservan overlay candidato',()=>{
  let count=0;
  const external=(s,mask)=>Object.fromEntries(s.wan_services.map((w,i)=>[w.id,!!(mask&(1<<i))]));
  for(const s of sites.slice(1))for(let remote=1;remote<16;remote++)for(let hub=1;hub<16;hub++){
   assert.ok(M.overlayPath(s,M.inspect(s,M.makeState(),external(s,remote)),cm,M.inspect(cm,M.makeState(),external(cm,hub))),s.id+' '+remote+'/'+hub);count++;
  }assert.equal(count,4950);
 });
 test(variant+': sin acceso utilizable no se anuncia overlay',()=>{
  const s=sites[1],none=Object.fromEntries(s.wan_services.map(w=>[w.id,false]));
  assert.equal(M.overlayPath(s,M.inspect(s,M.makeState(),none),cm,M.inspect(cm,M.makeState())),false);
 });
 test(variant+': sin candidato coincidente se rechaza el camino',()=>{
  const s=structuredClone(sites[1]);s.tunnels=[];assert.equal(M.overlayPath(s,M.inspect(s,M.makeState()),cm,M.inspect(cm,M.makeState())),false);
 });
 test(variant+': caída de sitio elimina LAN, equipos y aplicación remota',()=>{
  const s=sites.find(s=>s.id==='s19'),state={...M.makeState(),faults:['site']},z=M.inspect(s,state);
  assert.equal(z.siteAvailable,false);assert.equal(z.gatewayAvailable,false);assert.equal(z.activeWan,null);
  assert.ok(Object.values(z.poweredNodes).every(v=>!v));assert.equal(M.access(s,state,M.endpoints(s)[0],z).local,false);
 });
 test(variant+': ocho comprobaciones HA aisladas cumplen su resultado esperado',()=>{const r=M.recoveryAudit(cm);assert.equal(r.passed,8);assert.equal(r.rtoMeasuredSeconds,null);assert.equal(r.rpoMeasuredSeconds,null);});
 for(const expected of exercises.variants.find(v=>v.variant===variant).scenarios){
  test(variant+': recuperación '+expected.scenario+' coincide con el anexo publicado',()=>assert.deepEqual(M.recoveryExercise(cm,{scenario:expected.scenario}),expected));
 }
}
