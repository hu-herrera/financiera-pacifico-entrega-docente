# Evidencia de pruebas y reproducción pública

Cierre documental: 27 de octubre de 2026. Este registro separa los resultados históricos declarados de las comprobaciones públicas del corte actual. Los conteos no se suman como casos únicos.

## Corte actual

- Simulador: `hu-herrera/fina`, commit `bb47152bb74b8dfee9e728e74a2e6e2c26e05412`.
- Alcance publicado: 30 pruebas Node del modelo y 16 casos de interfaz con Chromium/Playwright 1.62.1.
- Las 30 pruebas de modelo aprobaron localmente. Incluyen 9.900 combinaciones WAN como comprobaciones internas, 14 ejercicios de recuperación A/B y ocho escenarios HA por alternativa.
- El conjunto completo de desarrollo aprobó 109 pruebas Node localmente. Su código permanece privado y este resultado no se presenta como una ejecución pública de CI.
- La ejecución pública [40602232862](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/actions/runs/40602232862), sobre la entrega `adec142` y fina `bb47152`, aprobó los 30 casos de modelo y los 16 casos de navegador. También aprobaron manifiesto, ZIP, Excel y flujo anual. El resultado es verificable en sus logs y artefactos.

[Workflow público y ejecuciones](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/actions/workflows/verificacion-publica.yml). Cada ejecución identifica el commit de la entrega y obtiene el SHA del simulador desde `Verificacion/corte.json`. Sus artefactos conservan TAP, reporte JSON y capturas; una ejecución de Pages no sustituye estos resultados.

## Registros históricos

| Corte | Resultado declarado | Evidencia y límite |
|---|---|---|
| 23/10, 228ec26 | 78 Node; 144 navegador; selección posterior de 31; 1.351 caminos | Registro histórico en informe/E6; logs completos fuera de los dos repositorios públicos |
| 24/10, WAN-2 | 79 pruebas de lógica | Revisión histórica de distribuidores; no describe el corte WAN-3 |
| 25/10, capacidad | 93 Node; 151 navegador, commit privado 377af3c / run 40140351278 | Registros del anexo de cierre; acceso a logs privado |
| 25/10, WAN-3 | 99 Node; 44 navegador seleccionadas; 9.900 combinaciones internas | Conteos y alcance del anexo WAN-3; no sumarlos a pasadas previas |
| 26/10, fina 5779eeb | 71 Node seleccionadas y 161 navegador mencionadas en el mensaje del commit | No verificadas públicamente por esta revisión. El README actual no contiene esos conteos |

En `5779eebfab67c782d0fcfcc67b0eb1caec72c355` sí existe [Pages 40307930631](https://github.com/hu-herrera/fina/actions/runs/40307930631): checkout, empaquetado y despliegue. Sus jobs no ejecutan Node tests ni Playwright. La consulta con SHA corto o filtrada por pull request no acredita la ausencia de todas las ejecuciones. Tampoco ese despliegue acredita las 71/161 pruebas del mensaje.

## Reproducción

Clonar ambos repositorios públicos en carpetas hermanas llamadas `fina` y `financiera-pacifico-entrega-docente`. Seleccionar en `fina` el SHA de `Verificacion/corte.json`; desde la entrega ejecutar:

```bash
python Verificacion/documentos.py
SIMULATOR_DIR=../fina node --test Verificacion/modelo.test.cjs
npm install --prefix Verificacion --no-save @playwright/test@1.62.1
Verificacion/node_modules/.bin/playwright install chromium
SIMULATOR_DIR=../fina Verificacion/node_modules/.bin/playwright test --config Verificacion/playwright.config.cjs
```

`documentos.py` comprueba huellas, copias dentro del ZIP, valores guardados de Excel y flujo anual. Las pruebas Node comprueban inventario, presupuesto, IPAM, candidatos WAN, fallos negativos, caída de sitio y recuperación. Los 16 casos de navegador operan los controles E1–E7 y la escena 10, en A y B. El resultado exige observar el estado y la disponibilidad HTTPS; no basta con una etiqueta de éxito.

## Límites y material consultable

RTO/RPO siguen como objetivos; los tiempos físicos, sesiones, capacidad contratada y certificación de hardware no se deducen de estas pruebas. Las fuentes académicas Markdown están en `Fuentes/`, junto con sus PDF. Presupuesto A/B, política, ACL y admisión de video se publican en `Anexos/`; no se necesita acceso al repositorio de trabajo privado para consultar esas referencias.

## Trazabilidad de la primera ejecución pública

[40601870797](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/actions/runs/40601870797), sobre fina `9b5139e`: manifiesto, ZIP, Excel y 30 pruebas de modelo aprobados; 14 casos E1–E7 aprobados y dos casos de recuperación detenidos por una discrepancia del título visible. Se corrige la sustitución del título en el renderizador, se conserva la expectativa y se repite el conjunto sobre el nuevo SHA. El fallo no se registra como una aprobación de la escena 10.


## Resultado público confirmado

| Ejecución | Corte del simulador | Comprobación | Resultado |
|---|---|---|---|
| 40602232862 | bb47152bb74b8dfee9e728e74a2e6e2c26e05412 | Manifiesto, ZIP, Excel y flujo anual | PASS |
| 40602232862 | bb47152bb74b8dfee9e728e74a2e6e2c26e05412 | 30 pruebas Node públicas | 30 PASS / 0 FAIL |
| 40602232862 | bb47152bb74b8dfee9e728e74a2e6e2c26e05412 | 16 casos Chromium: E1–E7 y escena 10, A/B | 16 PASS / 0 FAIL |

[Logs y artefactos de la ejecución](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/actions/runs/40602232862). La matriz de 9.900 combinaciones y los 14 ejercicios de recuperación están incluidos en las 30 pruebas Node; no son 9.914 pruebas adicionales. El reporte de navegador y sus capturas se conservan junto al TAP del modelo. El registro 71/161 de 5779eeb sigue sin verificarse públicamente y no se sustituye por estos conteos.

[Resumen verificable en JSON](Resultado_Verificacion_Publica_27_oct_2026.json). Los artefactos de Actions tienen retención temporal. Para conservar la evidencia se versionan también [el reporte completo de navegador](Evidencia_Publica_27_oct_2026/interfaz.json), [el resultado TAP del modelo](Evidencia_Publica_27_oct_2026/modelo.tap) y las capturas [A](Evidencia_Publica_27_oct_2026/escena10-A.png) y [B](Evidencia_Publica_27_oct_2026/escena10-B.png), además del resumen y los identificadores de ejecución.
