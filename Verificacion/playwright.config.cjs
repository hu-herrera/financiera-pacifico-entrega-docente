const {defineConfig}=require('@playwright/test');
module.exports=defineConfig({testDir:__dirname,testMatch:'interfaz.spec.cjs',timeout:45000,workers:1,retries:0,reporter:[['line'],['json',{outputFile:'resultados/interfaz.json'}]],outputDir:'resultados/interfaz',use:{browserName:'chromium',headless:true,viewport:{width:1366,height:900},trace:'retain-on-failure'}});
