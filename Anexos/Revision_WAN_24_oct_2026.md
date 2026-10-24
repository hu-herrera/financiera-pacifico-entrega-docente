# Revisión WAN-2: distribuidores comunes A/B

**Fecha:** 24-10-2026. **Revisión económica:** C5-ECO-2-WAN-MIKROTIK.

## Problema y corrección

B ya utilizaba MikroTik, mientras A conservaba C1300, pese a la instrucción de usar otra marca en ambas opciones. Se reemplazan también en A los 45 distribuidores gigabit por hEX E50UG y el distribuidor multigigabit central por CRS310-8G+2S+IN. No cambia el ANTES ni la cantidad de transportes, routers, switches de acceso o firewalls.

Los distribuidores trabajan en L2 con VLAN de operador aisladas, sin NAT, DHCP ni VPN. En sucursal: ether1/2 CPE, ether3/4 routers y ether5 gestión. En central: ether1 CPE, ether2/3 firewalls y ether4 gestión. Los tres enlaces de datos de WAN-A central son 2,5G. Se conservan dos dominios WAN independientes y no se habilitan rutas de negocio por gestión.

## Conciliación de A

| Concepto CLP | C5-ECO-1 histórico | WAN-2 vigente | Diferencia |
|---|---:|---:|---:|
| Subtotal | 710.667.942 | 689.173.923 | -21.494.019 |
| Contingencia | 106.600.191 | 103.376.088 | -3.224.103 |
| Inicial | 817.268.133 | 792.550.011 | -24.718.122 |
| Alcance 60 meses | 1.526.153.453 | 1.501.435.331 | -24.718.122 |

WAN mensual CLP 10.981.422 y B CLP 280.617.592 inicial / 964.502.912 a 60 meses se mantienen. Las seis aperturas continúan fuera de la compra actual; su red de referencia A se recalcula a CLP 191.034.261 antes de logística adicional.

Los unitarios adoptados son CLP 77.048 por hEX y 281.459 por CRS310, iguales en A/B. Precios sugeridos oficiales USD 59,95 / USD 219, consultados el 24-10-2026. Conversión supuesta USD/CLP 1000, reserva importadora 8 % e IVA 19 %, incluidos una vez en esos unitarios. Fuentes: https://mikrotik.com/product/hex_2024 y https://mikrotik.com/product/crs310_8g_2s_in.

## Validación ejecutada

| Comprobación | Resultado | Alcance |
|---|---|---|
| Node, `tests/*.test.cjs` | PASS, 79 pruebas | Cálculo, modelo, políticas y consistencia |
| Navegador C5/dispositivos/presentación | PASS, 31 casos | 30 en pasada inicial; recorrido A/B repetido tras actualizar su expectativa de importe |
| Puertos y VLAN de distribuidores A/B | PASS | Todos los extremos únicos, cinco puertos remotos, gestión aislada y camino superviviente ante falla de cada distribuidor |
| Generadores C5, presupuesto, navegador, seguridad y presentación | PASS | Comprobación `--check` de cada fuente/salida |
| Excel | PASS | Inicial A/B y total a 60 meses conciliados con JSON, fórmulas recalculadas |
| Hardware/protocolos físicos | NO PROBADO | Fuera del alcance académico ficticio, no pendiente para entregar el prototipo |

La primera pasada de navegador encontró una expectativa de prueba con el importe anterior de A. El simulador ya mostraba CLP 792,6 millones. Se corrigió la expectativa y el recorrido completo A/B pasó al repetirse. No se presenta una expectativa obsoleta como un fallo de conectividad.

Ejecución local: Playwright con Chromium 153, compilación de @sparticuz/chromium, por indisponibilidad del descargador habitual. Los workflows mantienen su Chromium de CI. Las pruebas verifican el modelo web, no firmware ni SLAs físicos.

## Concordancia

Se actualizan fichas, puertos de topología, vistas de dispositivo, modelo del navegador, presupuesto y congelación económica, presentación integrada, IPAM, PDF de revisión, planilla y PPT docente. El guion personal retira el pendiente condicional. El archivo C5-ECO-1 se conserva como histórico identificado.
