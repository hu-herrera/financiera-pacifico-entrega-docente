const {defineConfig}=require('@playwright/test');
const path=require('node:path'),results=path.resolve(process.env.GITHUB_WORKSPACE||process.cwd(),'resultados');
module.exports=defineConfig({testDir:__dirname,testMatch:'interfaz.spec.cjs',timeout:45000,workers:1,retries:0,reporter:[['line'],['json',{outputFile:path.join(results,'interfaz.json')}]],outputDir:path.join(results,'interfaz'),use:{browserName:'chromium',headless:true,viewport:{width:1366,height:900},trace:'retain-on-failure'}});
