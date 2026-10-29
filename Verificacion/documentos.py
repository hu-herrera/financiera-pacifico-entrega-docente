"""Verify the delivered bytes, archive and economic controls; no external packages."""
from pathlib import Path
import hashlib,zipfile,json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
rows=[line.split(maxsplit=1) for line in (R/'MANIFIESTO.sha256').read_text().splitlines() if line.strip()]
for digest,name in rows:
 p=R/name;assert p.is_file(),name
 assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,('manifest',name)
with zipfile.ZipFile(R/'Entrega_Profesor_Financiera_Pacifico.zip') as z:
 assert z.testzip() is None
 assert set(z.namelist())=={name for _,name in rows}|{'MANIFIESTO.sha256'}
 for _,name in rows:assert z.read(name)==(R/name).read_bytes(),('archive',name)
 assert z.read('MANIFIESTO.sha256')==(R/'MANIFIESTO.sha256').read_bytes()
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(R/'Anexos/Presupuesto_Inventario.xlsx') as z:
 root=ET.fromstring(z.read('xl/worksheets/sheet1.xml'));cells={c.get('r'):c for c in root.findall('.//s:c',ns)}
 for cell,value in {'B8':793126897,'C8':281194478,'B9':660607380,'C9':660607380,'B11':1503734277,'C11':966801858,'B19':11010123,'C19':11010123}.items():assert round(float(cells[cell].find('s:v',ns).text))==value,(cell,value)
 for name in z.namelist():
  if name.startswith('xl/worksheets/') and name.endswith('.xml'):assert not [c for c in ET.fromstring(z.read(name)).findall('.//s:c',ns) if c.get('t')=='e']
annual=11010123*12
assert 793126897+annual+10000000==935248373
assert 281194478+annual+5000000==418315954
assert 935248373+4*(annual+10000000)==1503734277
assert 418315954+4*(annual+5000000)==966801858
for p in (R/'Fuentes').glob('*.md'):
 text=p.read_text();assert 'github.io/fin/' not in text,p
 assert 'https://github.com/hu-herrera/financiera-pacifico-trabajo-privado/' not in text,p
summary=json.loads((R/'Anexos/Resultado_Verificacion_Publica_27_oct_2026.json').read_text())
report=json.loads((R/'Anexos/Evidencia_Publica_27_oct_2026/interfaz.json').read_text())
cut=json.loads((R/'Verificacion/corte.json').read_text())
assert summary['simulator_commit']  # corte histórico del 27 de octubre
assert report['stats']['expected']==summary['browser']['passed']==16
assert report['stats']['unexpected']==summary['browser']['failed']==0
assert report['stats']['skipped']==0 and report['stats']['flaky']==0
tap=(R/'Anexos/Evidencia_Publica_27_oct_2026/modelo.tap').read_text()
for line in ['# tests 30','# pass 30','# fail 0']:assert line in tap,line
assert summary['node']['passed']==30 and summary['node']['failed']==0
current=json.loads((R/'Anexos/Resultado_Verificacion_Publica_28_oct_2026.json').read_text())
assert current['simulator_commit']  # corte histórico
report=json.loads((R/'Anexos/Evidencia_Publica_28_oct_2026/interfaz.json').read_text())
assert report['stats']['expected']==current['browser']['passed']==52
assert report['stats']['unexpected']==report['stats']['skipped']==report['stats']['flaky']==0
log=(R/'Anexos/Evidencia_Publica_28_oct_2026/modelo.tap').read_text()
for line in ['# tests 60','# pass 60','# fail 0']:assert line in log,line
assert current['node']['passed']==60 and current['node']['failed']==0
for run in json.loads((R/'Anexos/Evidencia_Publica_28_oct_2026/recorrido.json').read_text()):
 assert run['scenes']==list(range(1,14)) and run['status']=='PASS' and not run['errors']
latest=json.loads((R/'Anexos/Resultado_Verificacion_Publica_29_oct_2026.json').read_text())
assert latest['simulator_commit']==cut['simulator_commit']
report=json.loads((R/'Anexos/Evidencia_Publica_29_oct_2026/interfaz.json').read_text())
assert report['stats']['expected']==latest['browser']['passed']==52
assert report['stats']['unexpected']==report['stats']['skipped']==report['stats']['flaky']==0
log=(R/'Anexos/Evidencia_Publica_29_oct_2026/modelo.tap').read_text()
for line in ['# tests 60','# pass 60','# fail 0']:assert line in log,line
outline=json.loads((R/'Anexos/Recorrido_Presentacion_13_Escenas.json').read_text())['scenes']
assert [s['number'] for s in outline]==list(range(1,14))
assert len({s['id'] for s in outline})==len({s['title'] for s in outline})==13
for run in json.loads((R/'Anexos/Evidencia_Publica_29_oct_2026/recorrido.json').read_text()):
 assert run['scenes']==list(range(1,14)) and run['status']=='PASS' and not run['errors']
for run in json.loads((R/'Anexos/Evidencia_Publica_29_oct_2026/correspondencia.json').read_text()):
 assert not run['errors'] and run['status']=='PASS'
 assert [{k:s[k] for k in ('number','id','title','phases')} for s in run['scenes']]==outline
timing=json.loads((R/'Anexos/Tiempos_Recorrido_Automatico.json').read_text())
assert timing['reading_wpm']==115
assert [s['id'] for s in timing['scenes']]==[s['id'] for s in outline]
for t,o in zip(timing['scenes'],outline):
 assert t['title']==o['title'] and list(t['steps'])==o['phases']
 assert t['introSeconds']>0 and t['outroSeconds']>=0
 assert all(isinstance(v,int) and v>=10 for v in t['steps'].values())
assert timing['estimated_seconds']==sum(t['introSeconds']+sum(t['steps'].values())+(t['outroSeconds'] if t['steps'] else 0) for t in timing['scenes'])
with zipfile.ZipFile(R/'Presentacion/Avance_Financiera_Pacifico_30_oct_2026.pptx') as z:
 slides=[n for n in z.namelist() if __import__('re').fullmatch(r'ppt/slides/slide\d+\.xml',n)]
 assert len(slides)==13
 ppt_titles=[]
 for i,scene in enumerate(outline,1):
  root=ET.fromstring(z.read(f'ppt/slides/slide{i}.xml'))
  text=[n.text or '' for n in root.iter() if n.tag.endswith('}t')]
  assert text[0]==scene['title'],(i,text[0],scene['title'])
  ppt_titles.append(text[0])
 assert len(set(ppt_titles))==13
 for n in z.namelist():
  if '/media/' in n:assert len(z.read(n))>0,('empty image',n)
 assert 'Para finalizar' in z.read('ppt/slides/slide13.xml').decode()
 # La narración personal se entrega por separado.
 assert not any('guion' in n.lower() or n.startswith('Video/') for n in z.namelist())
assert not any('guion' in name.lower() or name.startswith('Video/') for _,name in rows)
print(json.dumps({'scope':'DOCUMENTOS_Y_PAQUETE','manifest_entries':len(rows),'archive':'PASS','workbook':'PASS','annual_economics':'PASS','public_links':'PASS','current_model':60,'current_browser':52,'web_scenes':13,'ppt_slides':13,'scene_titles':'MATCH','example_phases':'MATCH'},ensure_ascii=False))
