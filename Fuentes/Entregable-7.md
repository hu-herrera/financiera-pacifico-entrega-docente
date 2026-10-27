# Entregable 7 — Presupuesto, TCO, despliegue y migración

**Financiera Pacífico · edición C5 A/B, revisión WAN-3 · cierre documental 27 de octubre de 2026**

## 1. Alcance económico

Presupuesto de planificación para modernizar las 23 sedes actuales durante 60 meses. Todos los importes se expresan en CLP con IVA supuesto. Son referencias públicas, precios condicionados y reservas de ingeniería; no constituyen cotización, compra ejecutada ni contrato con operadores.

USD/CLP 1000 y EUR/CLP 1100 son supuestos de cálculo; el hardware importado aplica reserva 8 % antes de IVA 19 %. No son tipo de cambio observado ni tasa arancelaria afirmada. Se redondea cada partida una sola vez; el subtotal conserva esa suma. La contingencia 15 % se aplica una vez.

## 2. Resumen A/B

| Concepto | A · Cisco/Palo Alto | B · MikroTik/OPNsense |
| --- | --- | --- |
| Subtotal de partidas | 689.675.563 | 244.516.937 |
| Contingencia de implantación 15 % | 103.451.334 | 36.677.541 |
| Inversión inicial | 793.126.897 | 281.194.478 |
| WAN mensual | 11.010.123 | 11.010.123 |
| WAN 60 meses | 660.607.380 | 660.607.380 |
| Reserva de operación 5 años | 50.000.000 | 25.000.000 |
| Costo del alcance 60 meses | 1.503.734.277 | 966.801.858 |

**Fórmula:** costo del alcance 60 meses = inversión inicial + WAN 60 meses + reserva de operación. La inversión ya está incluida; no se añade una segunda vez. Parte del desembolso corresponde a servicios/licencias prepagados, por lo que no todo debe llamarse CAPEX contable.

B es CLP 511.932.419 menor en inversión y CLP 536.932.419 menor a 60 meses que A. Es diferencia entre propuestas, no ahorro neto frente a facturas anteriores. Ambas superan la referencia original CLP 160 millones; no se declara que cumplan aquel monto. El costo completo de operar la financiera, ROI y payback frente al ANTES no se han inventado.

## 3. Inventario y partidas A


A compra 37 routers y 27 switches remotos; reutiliza siete routers, 17 switches remotos y dos centrales. Incluye licencias SEC/VPERF para los nuevos, suscripción inicial de switches donde corresponde, dos PA-1410 con ATP/soporte 60 meses y 46 distribuidores WAN MikroTik (45 hEX y un CRS310). Los 46 kits de StackWise contienen sus cables: no se compran otros 46 por duplicado.

## 4. Inventario y partidas B


B compra 42 CCR2004, dos RB5009, 44 CRS328, dos DEC3852, 45 hEX y un CRS310. Los 44 DAC de 1 m corresponden a dos enlaces de 10G por pareja remota. Conserva switching central y servicios existentes. Elimina partidas Cisco SEC/VPERF/DNA, ATP/soporte Palo Alto, StackWise remoto y HSCI que no corresponden a B. Mantiene instalación, logística y reserva operativa.

## 5. WAN y tratamiento de operadores

Las 92 mensualidades corresponden a cuatro servicios centrales y cuatro por sucursal. El escenario fija Starlink CM 1.500.000, veinte continentales 250.000 cada una y dos pequeñas 200.000; Leo 200.000 por sede; Entel 15.900 y WOM 15.990 en cada una de las 23 sedes, antes de descuento. El 10 % supuesto se aplica una sola vez: CLP 12.233.470→11.010.123 mensuales; por 60 meses, CLP 660.607.380.

Starlink/Leo incluyen terminales, agregación del operador, instalación/reemplazo en comodato como premisa comercial ficticia. Los 46 CPE móviles se compran aparte. La ingeniería de cableado, puertos, trunks y módulos dentro de nuestra red sí pertenece a la propuesta y está presupuestada. La mención de un servicio no acredita un contrato ni cobertura real por dirección.

## 6. Servidores y elementos existentes

No se compran PCs, teléfonos ni hosts completos. DC-02 recibe CLP 250.000 de RAM y CLP 1.200.000 de SSD en espejo desde la reserva de ingeniería; esta conserva CLP 6.550.000. La reasignación no aumenta subtotal ni contingencia. Se conservan DC-01, DC-02, BKP-01, 650 T54W y 650 PCs.

Cableado horizontal, racks, UPS, baterías, generador, climatización e instalaciones eléctricas existentes quedan fuera de esta oferta. El presupuesto no permite prometer autonomía, recuperación de todo el edificio ni un segundo datacenter financiado. La reserva de operación no vuelve a cobrar ATP/soporte prepagado y no significa personal existente gratuito.

## 7. Expansión separada

Seis aperturas no se suman a la inversión ni mensualidades actuales. El cálculo de referencia A de red futura es CLP 191.034.261 con contingencia, antes de logística adicional, y CLP 2.602.206 de WAN mensual al abrir las seis. Es una referencia de A y no debe presentarse como precio cerrado de B. PCs/teléfonos de esas aperturas se consideran aporte del cliente; las fechas determinan los meses de servicio. El año seis no se incluye en el horizonte actual.

## 8. Despliegue propuesto

| Fase relativa | Actividad | Salida para avanzar |
|---|---|---|
| Semanas 1–2 | Confirmar inventario del escenario, capacidad, responsables y ventanas | BOM/IPAM y respaldo de configuración |
| Semanas 3–4 | Preparar configuración de A o B, políticas, monitoreo, réplica y reversión | Configuración revisada y recuperación documentada |
| Semanas 5–6 | Piloto CM y una sucursal, manteniendo MPLS transitorio | Aplicación, voz, seguridad, fallas y rollback aceptados |
| Semanas 7–9 | Tres olas de seis sucursales | Acta por sede y estabilidad antes de la siguiente ola |
| Semanas 10–11 | Tres sucursales finales con logística especial | Las 22 remotas migradas:1+18+3 |
| Semana 12 | Estabilización, capacitación y cierre | Documentación, respaldos y retiro MPLS autorizado por aceptación |

Es un cronograma propuesto, no una instalación ejecutada ni compromiso de entrega de proveedores. Jefatura coordina alcance/cambios; redes configura caminos/puertos/VPN; seguridad revisa permisos; sistemas configura HA/backup; telefonía verifica PBX; operación recibe monitoreo y runbooks.

## 9. Ventana y reversión por sede

1. Respaldar configuración, registrar direccionamiento/puertos y probar aplicación/voz antes del cambio.
2. Preparar la nueva red sin activar dos DHCP/gateways incompatibles sobre la misma LAN.
3. Validar transportes, túneles, rutas de retorno y políticas con un puesto piloto.
4. Migrar por grupos; comprobar APP, DNS, voz, invitados, gestión y fallas recuperables.
5. Revertir si falla un servicio crítico, hay exposición de red o se alcanza el límite acordado de la ventana. Restaurar enlaces/configuración previos y confirmar servicio.
6. Guardar configuración aceptada, logs y acta. No retirar MPLS hasta aceptar la sustitución; en el diseño final quedan cero MPLS.

## 10. Riesgos, operación y aceptación

| Riesgo | Tratamiento |
|---|---|
| Menor capacidad en respaldo | Priorizar APP/voz y limitar video/copias; no prometer operación plena |
| Pérdida de un host | Réplica/quórum/fencing y capacidad N+1 definidas en E3/E4 |
| Pérdida de CM | Declarar límite del diseño actual y recuperación externa separada |
| Cuotas, cobertura y dependencia de operador | Premisas del caso identificadas, sin inventar contratos |
| Cambios de precios | Mantener corte económico y documentar diferencias antes de sustituirlo |
| Error de cambio | Respaldo, piloto, ventana y rollback |

Operación propuesta: alertas continuas WAN/HA/servicios; revisión diaria de copias/logs; respaldos después de cambios; revisión mensual de capacidad, permisos y parches; ensayo periódico de recuperación. Actualizar un miembro cada vez y conservar acceso de consola. La aceptación académica se acredita con diseño conciliado, prototipo y pruebas E6; no queda condicionada a homologar equipos físicos inexistentes.

## 11. Fuentes y archivo de cálculo

[Excel de presupuesto e inventario](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Presupuesto_Inventario.xlsx) · [JSON A con fuentes/precios](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Presupuesto_C5_A.json) · [JSON B con fuentes/precios](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Presupuesto_C5_B.json) · [base económica A](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Corte_Economico_C5.json). Las tablas históricas de E7 del 15 de octubre no reemplazan estas partidas.



## 12. Plan por año y distribución del costo

Los cinco años son el horizonte de operación y evaluación. La implantación inicial se organiza en la ventana de doce semanas de este entregable, dentro del año 1; no se pospone artificialmente equipamiento esencial hasta el año 4 para simular que cabe en 160 millones.

| Año | Trabajo y sedes priorizadas | Resultado esperado |
|---|---|---|
| 1 | Staging y capacitación; CM y S01 como piloto; luego 18 remotas continentales; cierre S20/S21/S22 por logística | 23 sedes migradas por acta; configuración, políticas, HA y reversión documentadas |
| 2 | Operación de las 23 sedes; revisión de capacidad, cuotas, parches y recuperación | Estabilidad y ajustes dentro de las reservas; nuevas aperturas sujetas a fase separada |
| 3 | Mantenimiento, prueba de restauración y revisión de derechos/licencias | Renovar lo exigible sin duplicar servicios prepagados; no se promete reposición gratuita |
| 4 | Revisión de demanda y ciclo de vida; evaluar mayor capacidad antes de ampliar | Decisión de expansión o nueva inversión separada, según escenarios 830/967 puestos |
| 5 | Operación, evaluación de resultados y plan del siguiente ciclo | Cierre del horizonte 60 meses; renovaciones del año 6 separadas |

| Año | Inicial A | Inicial B | WAN común | Reserva A / B | Total A / B |
| --- | --- | --- | --- | --- | --- |
| 1 | 793.126.897 | 281.194.478 | 132.121.476 | 10.000.000 / 5.000.000 | 935.248.373 / 418.315.954 |
| 2 | 0 | 0 | 132.121.476 | 10.000.000 / 5.000.000 | 142.121.476 / 137.121.476 |
| 3 | 0 | 0 | 132.121.476 | 10.000.000 / 5.000.000 | 142.121.476 / 137.121.476 |
| 4 | 0 | 0 | 132.121.476 | 10.000.000 / 5.000.000 | 142.121.476 / 137.121.476 |
| 5 | 0 | 0 | 132.121.476 | 10.000.000 / 5.000.000 | 142.121.476 / 137.121.476 |

La suma mantiene A 1.503.734.277 y B 966.801.858 CLP. La WAN opera doce meses por año como convención de planificación; los meses efectivos durante las olas se ajustarían sin duplicar los contratos MPLS transitorios, cuyo solapamiento no se supone cotizado. No se incluye salario incremental del personal existente. Capacitación operativa y transferencia se consideran dentro de la implantación por sede e ingeniería común; no hay un curso externo o certificación Cisco adicional cotizado. Mantención se cubre con la reserva anual y el soporte prepagado definido por alternativa.

## 13. Valores unitarios y evidencia de precios

La siguiente tabla complementa los totales por partida anteriores. Los unitarios A se muestran en su moneda/base original; los B en CLP con IVA adoptados. Un unitario mostrado redondeado puede no reproducir el total si se redondea otra vez: gobierna el redondeo por partida de la fuente JSON/Excel.

| Partida A | Cant. | Unitario original | Base | Total CLP con IVA |
|---|---:|---:|---|---:|
| Router sucursal, hardware base | 37 | 1032570 | CLP_NET | 45.464.057 |
| Licencia SEC por router nuevo | 37 | 882.75 | USD_NET | 38.867.483 |
| Licencia VPERF por router nuevo | 37 | 2200 | USD_NET | 96.866.000 |
| Switch nuevo 24 puertos PoE, Network Essentials | 27 | 2109344 | CLP_NET | 67.773.223 |
| Suscripción inicial switch nuevo, 3 años | 27 | 808.99 | USD_NET | 25.992.849 |
| Kit stack completo por miembro | 46 | 815 | USD_NET | 48.182.148 |
| Firewall central hardware | 2 | 11385 | USD_NET | 29.264.004 |
| ATP central 60 meses por miembro HA | 2 | 12825 | USD_NET | 30.523.500 |
| Soporte fabricante PA-1410, 60 meses | 2 | 10500 | USD_NET | 24.990.000 |
| Distribuidor WAN MikroTik hEX E50UG, bridge VLAN | 45 | 77048 | CLP_GROSS | 3.467.160 |
| Distribuidor WAN-A central MikroTik CRS310, bridge VLAN 2,5G | 1 | 281459 | CLP_GROSS | 281.459 |
| CPE móvil Entel 5G, comprado | 23 | 342850 | CLP_GROSS | 7.885.550 |
| CPE móvil WOM 4G, comprado | 23 | 158790 | CLP_GROSS | 3.652.170 |
| AP Wi-Fi de contingencia | 48 | 300000 | CLP_GROSS | 14.400.000 |
| Reserva máxima Wi-Fi PCs existentes | 650 | 50000 | CLP_GROSS | 32.500.000 |
| Segunda fuente switches 24P | 29 | 799 | USD_NET | 29.779.369 |
| Segunda fuente switches 48P | 17 | 2962.99 | USD_NET | 64.736.591 |
| Reserva segunda fuente firewall central | 2 | 900000 | CLP_GROSS | 1.800.000 |
| Transceptores LAN central 10G | 8 | 300000 | CLP_GROSS | 2.400.000 |
| Latiguillo óptico central | 4 | 50000 | CLP_GROSS | 200.000 |
| Cable HA2 HSCI central | 1 | 250000 | CLP_GROSS | 250.000 |
| Cat6, organización y accesorios de montaje | 23 | 800000 | CLP_GROSS | 18.400.000 |
| Diseño RF, instalación y aceptación Wi-Fi | 23 | 500000 | CLP_GROSS | 11.500.000 |
| Implantación y migración de red por sede | 23 | 2500000 | CLP_GROSS | 57.500.000 |
| Traslados regionales y logística de implantación | 1 | 25000000 | CLP_GROSS | 25.000.000 |
| Ingeniería común, laboratorio y documentación | 1 | 6550000 | CLP_GROSS | 6.550.000 |
| DC-02: ampliación de 32 a 64 GiB RAM | 1 | 250000 | CLP_GROSS | 250.000 |
| DC-02: par SSD empresarial 3,84 TB en espejo | 1 | 1200000 | CLP_GROSS | 1.200.000 |

| Partida B | Cant. | Unitario CLP con IVA | Total CLP con IVA |
|---|---:|---:|---:|
| CPE móvil Entel 5G, comprado | 23 | 342.850 | 7.885.550 |
| CPE móvil WOM 4G, comprado | 23 | 158.790 | 3.652.170 |
| AP Wi-Fi de contingencia | 48 | 300.000 | 14.400.000 |
| Reserva máxima Wi-Fi PCs existentes | 650 | 50.000 | 32.500.000 |
| Transceptores LAN central 10G | 8 | 300.000 | 2.400.000 |
| Latiguillo óptico central | 4 | 50.000 | 200.000 |
| Cat6, organización y accesorios de montaje | 23 | 800.000 | 18.400.000 |
| Diseño RF, instalación y aceptación Wi-Fi | 23 | 500.000 | 11.500.000 |
| Implantación y migración de red por sede | 23 | 2.500.000 | 57.500.000 |
| Traslados regionales y logística de implantación | 1 | 25.000.000 | 25.000.000 |
| Ingeniería común, laboratorio y documentación | 1 | 6.550.000 | 6.550.000 |
| DC-02: ampliación de 32 a 64 GiB RAM | 1 | 250.000 | 250.000 |
| DC-02: par SSD empresarial 3,84 TB en espejo | 1 | 1.200.000 | 1.200.000 |
| DAC MikroTik XS+DA0001 1m · enlaces LACP interswitch | 44 | 37.271 | 1.639.924 |
| Distribuidor WAN MikroTik hEX E50UG · bridge VLAN | 45 | 77.048 | 3.467.160 |
| Distribuidor WAN-A central MikroTik CRS310-8G+2S+IN | 1 | 281.459 | 281.459 |
| Router estándar MikroTik CCR2004-16G-2S+ | 42 | 553.350 | 23.240.700 |
| Router sede pequeña MikroTik RB5009UG+S+IN | 2 | 307.466 | 614.932 |
| Switch PoE MikroTik CRS328-24P-4S+RM | 44 | 646.990 | 28.467.560 |
| Appliance OPNsense DEC3852 | 2 | 2.683.741 | 5.367.482 |

## 14. Justificación de la inversión superior a la referencia

La diferencia compra redundancia de equipos, caminos alternativos, segmentación, capacidad de administración y recuperación de servicios; protege acceso al core financiero y VoIP. Reutilizar PCs/teléfonos/hosts y equipos recientes evita renovar toda la plataforma. B reduce el costo de adquisición/licencias frente a A, conservando el objetivo lógico, con otro esquema de soporte y operación.

Si no se realiza la inversión, persisten el único acceso/router/switch de cada sucursal y el firewall único central, además de la dependencia de servicios por host. Eso mantiene la exposición a interrupciones, sin que sea necesario inventar multas, pérdidas por minuto o una rentabilidad para justificarlo. La aceptación de un presupuesto ampliado es una decisión propuesta al patrocinador; no se afirma que esté aprobada una compra real.

**Revisión del 24-10-2026:** distribuidores WAN MikroTik comunes A/B. A: hEX E50UG, 45 × CLP 77.048 = 3.467.160; CRS310, 1 × CLP 281.459. Los unitarios brutos adoptados incluyen conversión, reserva de importación e IVA una sola vez, igual que B. Se retiran las partidas C1300 de la compra vigente.

## Cierre de capacidad del 25 de octubre

Se adopta [admisión de video C5](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Admision_Video_C5.md): hasta 30 terminales remotos y tres centrales con cámara; 965,627 Mbps de subida objetivo central. En contingencia se suspende el video y se posponen cargas no esenciales. Es una política de operación propuesta, con cálculo verificable y sin control automático de reuniones. La política de video conserva el principal y su límite; el presupuesto incorpora por separado la revisión WAN-3. Antes de crecimiento o aperturas se recalcula capacidad.

Revisión WAN-3 del 25/10: [cuatro accesos en central y continuidad extremo a extremo](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Continuidad_Cuatro_WAN_25_oct_2026.md).
