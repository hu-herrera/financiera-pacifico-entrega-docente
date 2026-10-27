# Informe de diagnóstico y propuesta de solución

**Estudiante:** Hugo Eduardo Herrera Inostroza\
**Curso:** Proyecto de Título APT\
**Caso:** 6 - Financiera Pacífico\
**Fecha de actualización:** 27 de octubre de 2026\
**Horizonte:** cinco años\
**Versión:** C5 A/B, consolidación para revisión docente

## 1. Resumen ejecutivo

Financiera Pacífico necesita mantener acceso a la aplicación financiera y telefonía cuando falla un acceso o un equipo. La ficha identifica sucursales sin contingencia, cambios manuales y exigencia de cifrado/auditoría. La solución combina transportes alternativos, dos routers y dos switches por sucursal, par de firewalls en Casa Matriz, segmentación y recuperación de máquinas virtuales entre servidores existentes.

Se comparan A Cisco/Palo Alto y B MikroTik/OPNsense con el mismo alcance de 23 sedes y 650 puestos. A requiere CLP 793.126.897 iniciales; B, CLP 281.194.478. El costo del alcance a 60 meses asciende a 1.503.734.277 y 966.801.858 CLP, respectivamente. Ambas superan la referencia inicial de 160 millones; la inversión se justifica por riesgos mitigados y con límites explícitos sobre ahorro y disponibilidad.

El proyecto entrega un simulador web propio y pruebas reproducibles. Demuestra comportamiento de caminos, fallas, políticas y dependencias del modelo. No afirma operación de firmware o medición física. La homologación física no es un entregable académico pendiente de este caso ficticio.

## 2. Datos oficiales y supuestos

| Tipo | Información | Fuente / criterio |
|---|---|---|
| Oficial | 780 trabajadores, 22 sedes y aproximadamente 650 usuarios TI | Hoja Empresas, fila 7 |
| Oficial | CM/datacenter y 21 sucursales; doble ISP central, MPLS único remoto, OSPF y 10.70/16 | Fichas de Casos, fila 7 |
| Oficial | RTO sucursal≤5 min, cifrado, auditoría y seis aperturas | Fichas de Casos, fila 7 |
| Oficial | Core 99,99 %/sucursal 99,95 %, L3, firewall/VPN y NMS central | Datos Técnicos, fila 7 |
| Adoptado | 23 sedes: CM + 22 sucursales; 650 PCs y 650 T54W existentes | Adaptación del equipo y distribución del simulador |
| Adoptado | Dos MPLS centrales de 1 Gbps y dos ISP de 500 Mbps; MPLS remoto 100 Mbps | Línea base ANTES del proyecto |
| Adoptado | Modelos, cohortes, capacidades de host, IPAM y carga | Fichas C5 A/B |
| Supuesto comercial | Leo disponible, caudales/agrupación Starlink, cobertura extrema, comodatos y 10 % de descuento | Condiciones explícitas del caso ficticio |
| Resultado | Pruebas y cifras aritméticas | Fuentes JSON, tests y registro E6 |

El evento MPLS de tres horas pertenece a la ficha; no acredita una tasa de incidentes, multas o tiempos observados en cada sede. No se importan los valores 180 ms/6 % de otro caso. Los 650 usuarios TI no es una constatación oficial de 650 equipos físicos. El escenario de 23 sedes es una ampliación explícita de la ficha de 22.

## 3. Diagnóstico de la infraestructura actual

El inventario previo es mixto: routers 1921, 4321 y C1121X según renovación; switches 2960-S y C9200L en sucursales; CM con dos 2911, dos C9200L y un ASA5512. Cada remota depende de un router, un switch y un MPLS de 100 Mbps. Central tiene dos MPLS de 1 Gbps y dos ISP de 500 Mbps. La redundancia central no elimina el acceso único remoto ni el firewall único.

La demanda normal calculada de una sede de 30 puestos alcanza aproximadamente 26,4 Mbps. El acceso 100 Mbps cubre ese perfil. El motivo principal de modernizar es evitar desconexión por falla de un elemento, mejorar control y preparar crecimiento; no afirmar que la red anterior estaba siempre saturada.

Los routers 2911 y switches 3560 revisados en el diagnóstico inicial pueden soportar routing, VLAN/802.1Q, QoS y VPN según capacidades/licencias. Las restricciones se fundamentan por ciclo de soporte, rendimiento de servicios/cifrado y escala, no por negar esas funciones. No se mantienen ISR 4451/3850 como compras de la propuesta vigente.

DC-01 R740 aloja APP/BD; DC-02 R740, PBX/DNS/NTP/AAA/NMS; BKP-01 R540 conserva respaldos. En ANTES los hosts tienen roles separados y un enlace cada uno. Sus modelos y recursos son el inventario académico adoptado, no un levantamiento físico.

## 4. Impacto y riesgos

| Dependencia | Efecto posible | Respuesta |
|---|---|---|
| MPLS/router único remoto | Interrupción de acceso al sistema financiero y voz central | Rutas y routers alternativos |
| Switch único remoto | Pérdida de conectividad/PoE de puestos | Dos switches y contingencia Wi-Fi independiente |
| Firewall único CM | Dependencias centrales sin salida/seguridad operativa | Par HA con enlaces y estados coherentes |
| Un host por función | Pérdida de servicios al caer el host | Réplica y recuperación de VMs críticas |
| Cambios sin trazabilidad suficiente | Mayor dificultad para revertir/auditar | Git, respaldo, política y registro de eventos |
| Dependencia del edificio CM | Una pérdida total puede afectar servicios y copias | Límite explícito; recuperación externa fuera de la compra actual |

Se reconocen efectos operacionales y reputacionales posibles sin asignar pérdida monetaria por minuto, multas o datos de transacciones inexistentes. No renovar mantiene las dependencias identificadas.

## 5. Arquitectura propuesta

Por sucursal: dos routers, dos switches, dos distribuidores WAN y cuatro transportes: Starlink/Leo/Entel 5G/WOM 4G. WAN-A agrupa Starlink/Entel y WAN-B Leo/WOM. La pérdida de un distribuidor conserva un satelital y un móvil en el otro dominio. Cada router llega a ambos switches por enlaces L3 independientes.

Central: dos firewalls activo/pasivo, dos switches existentes y cuatro WAN: Starlink, Leo, Entel y WOM. Las 92 suscripciones son 23 × 4. Los NGFW solo están en CM; no se compran 44 firewalls remotos. La navegación usa VPN hacia CM y sale inspeccionada allí. Si CM cae no se activa una salida local sin inspección.

A instala 44 routers C1121X (siete reutilizados/37 nuevos) y 44 switches remotos (17 reutilizados/27 nuevos). B incorpora 42 CCR2004 y dos RB5009 en S22, 44 CRS328, dos DEC3852, 45 hEX y un CRS310. Ambas conservan los dos C9200L centrales, 650 PCs/650 teléfonos y los hosts existentes. B mantiene sus propios puertos, LACP/RSTP/VRRP y CARP/pfsync; no hereda StackWise ni HSCI.

Los planos físicos/lógicos, puertos y referencias están en E3/E4 y los anexos. Los hEX trabajan en bridge VLAN, sin NAT/DHCP/VPN. La gestión entra por puerto separado y no se convierte en ruta de negocio.

## 6. Capacidad y seguridad

El principal CM de 1000/1000 Mbps cubre el perfil actual sin video (bajada 433,856/subida 647,413 Mbps calculados). El pico con video llega a 881,713/1088,199 Mbps: la subida supera 1 Gbps. El diseño exige prioridad APP/voz, control de admisión de video y programación de copias. Antes de seis aperturas se revisa capacidad; no se suma ancho de banda de dos proveedores para prometerlo a una sola sesión.

Se separan datos 10, voz 20, invitados 40, servidores 50 (CM), Wi-Fi 110/120 y gestión 130. Cada VLAN tiene subred/gateway y política; sus prefijos IP se enrutan por IPsec, sin extender etiquetas L2 de una sede a otra. Usuarios acceden a APP por HTTPS; BD solo desde APP; voz hacia PBX; invitados sin redes internas; NOC para administración. APP/BD comparten VLAN50 y requieren filtros de host además del perímetro.

El diseño propone IPsec/IKEv2/AES-256 y gestión/autenticación centralizadas. AES, ACL y registros apoyan controles de referencia PCI DSS 1/2/4/7/8/10, pero no acreditan cumplimiento integral ni aplicabilidad SOX por ser una financiera. La ficha no demuestra incumplimiento normativo del ANTES.

## 7. Detección, conmutación y recuperación

OSPF necesita información de salud: IP SLA/track en A, sondas Netwatch/control de ruta en B, estado de interfaces/adyacencias y DPD de VPN. Se evalúa upstream aunque la portadora siga activa y se supervisan servicios centrales. Los comandos del navegador son educativos; no una sesión con protocolos reales. E4 especifica la correspondencia con las siete fallas solicitadas por el profesor, incluida la función central de routing ahora ubicada en el par de firewalls.

El retorno del escenario E7 usa cinco segundos didácticos de estabilidad; no se presenta como un tiempo real de convergencia ni cinco minutos de hardware. La caída completa de una sede o CM se declara indisponible si no quedan dependencias/caminos suficientes.

En servidores, DC-02 aumenta a 64 GiB y 3840 GB útiles con CLP 1.450.000 reasignados de ingeniería. Los dos R740 usan réplica ZFS, qdevice en BKP y dos de tres votos. La recuperación exige réplica utilizable y fencing; reserva 52 GiB de VMs críticas más 4 GiB de host y pausa NMS. RPO objetivo 60 s y recuperación 300 s, sin conservación garantizada de sesiones. No cubre pérdida total del edificio ni reemplaza backup.

## 8. Inversión y alcance de cinco años

| Concepto CLP con IVA supuesto | A | B |
| --- | --- | --- |
| Inicial | 793.126.897 | 281.194.478 |
| WAN mensual | 11.010.123 | 11.010.123 |
| WAN 60 meses | 660.607.380 | 660.607.380 |
| Reserva operativa 5 años | 50.000.000 | 25.000.000 |
| Costo del alcance 60 meses | 1.503.734.277 | 966.801.858 |

El desembolso incluye contingencia 15 % y servicios/licencias prepagados, no todo CAPEX contable. El total 60 meses ya incluye el inicial. B reduce costo frente a A por plataforma/licencias y distinta reserva de operación; no demuestra ahorro neto contra el ANTES. E7 incluye cantidades/unitarios y flujo por año. La suma de los costos anuales coincide con estos totales.

La referencia de 160 millones no se cumple: A la supera en 633.126.897 iniciales y B en 121.194.478. La autorización docente permite fundamentar un presupuesto superior, sin sostener que distribuir las compras en fases reduce el costo total de la solución. La inversión se justifica por servicios protegidos y riesgos mitigados. El presupuesto queda como propuesta académica, no aprobación financiera real.

Se incluyen implementación, cableado/módulos del diseño, logística, transferencia/capacitación operativa y reservas de mantención. No se añaden cursos/certificaciones externos sin precio. No se recompran PCs, teléfonos, hosts completos o infraestructura eléctrica. Seis aperturas y año 6 son fases separadas. El escenario móvil/satélite conserva sus límites de cuotas, cobertura y capacidad.

## 9. Implementación por año

Año 1: configuración, capacitación y piloto CM/S01; tres olas de seis remotas y cierre S20/S21/S22 sujeto a logística, dentro de las doce semanas propuestas. Se mantiene MPLS transitorio hasta aceptación y rollback. Las compras necesarias para la redundancia se contabilizan en el inicial.

Años 2–4: operación y mantenimiento de 23 sedes, parches, revisión de capacidad, restauración y derechos de actualización. Las seis futuras se incorporan solo con fase/presupuesto propios; no se prometen gratuitas. Año 5: evaluación de resultados y plan de renovación del siguiente ciclo. La WAN se calcula por doce meses/año como convención del flujo E7.

## 10. Evaluación y resultados

Se registran 78 pruebas de lógica, 144 de navegador en la pasada general, 31 en la pasada final y 1.351 comprobaciones adicionales de caminos. Las 31 repiten parte del alcance general; no se suman como casos distintos. El registro histórico atribuye esas pasadas al commit 228ec26. Sus logs completos no están publicados en los dos repositorios de entrega. La verificación pública del cierre del 27 de octubre se identifica por separado en el anexo de evidencia.

Se comprueban inventario/IPAM, ACL, caminos de ida/retorno, fallas individuales y dobles, ausencia de caminos por gestión y HA condicionada. La métrica visible de conectividad es del estado simulado, no disponibilidad anual. E6 define disponibilidad, conmutación, RTT, pérdida, jitter, utilización, voz, recuperación e incidentes con su método y evidencia disponible.

## 11. Respuesta a la retroalimentación docente

| Observación | Corrección y ubicación |
|---|---|
| Hechos y supuestos mezclados | Caso oficial y sección 2; E1 diferencia ficha, adaptación e hipótesis |
| Capacidades de equipos previos incorrectas | Sección 3/E1 corrigen VLAN, routing, QoS y VPN; no se renueva por capacidades ficticiamente ausentes |
| Equipos propuestos de generaciones anteriores | E2 compara C5 A/B y consulta SKU/ciclo de vida sin confundir producto de migración con retirado |
| Cantidades contradictorias | E1/E2, Excel y anexo por 23 sedes; actuales, reutilizados y nuevos diferenciados |
| Presupuesto artificialmente ajustado | Sección 8/E7 muestran aumento, unitarios, reservas y distribución anual |
| OSPF insuficiente como detección | Sección 7/E4 incorpora salud de interfaz/upstream/túnel/servicio y retorno controlado |
| VLAN transportadas por IPsec | Sección 6/E4 explica rutas IP entre subredes y etiquetas locales |
| Normativa garantizada por AES/VLAN | Sección 6/E4 usa relaciones con controles y limita la conclusión |
| Redacción y codificación | UTF-8, numeración continua y diagramas PDF legibles |
| Siete escenarios de continuidad | Matriz explícita E4 y resultados del modelo E6 |
| Fases durante cinco años | Sección 9/E7 distingue implantación inicial de operación y gasto anual |
| Evidencia y fuentes | E5/E6, anexos de ingeniería y fuente primaria/precios |

## 12. Entrega y conclusión

La propuesta transforma un conjunto de dependencias únicas en una arquitectura con alternativas y límites explícitos. Conserva inventario útil, compara dos plataformas y presenta un costo trazable. El prototipo demuestra la lógica de continuidad y seguridad del diseño; no convierte objetivos en resultados medidos de una red real.

La carpeta reúne caso oficial/original, este diagnóstico y propuesta, siete entregables, bitácora y anexos técnicos. El enlace al simulador permite verificar el comportamiento que describen los documentos. Los estados históricos de la bitácora no sustituyen el cierre C5 A/B.

**Fuentes:** caso original del Capstone, retroalimentación docente, fichas C5 A/B, presupuestos y pruebas. Las referencias de fabricante y de precios se detallan en Anexos/Fuentes_Tecnicas_y_Precios.md.

## Revisión WAN-3 del 25 de octubre

Se agregan Entel y WOM también en Casa Matriz, con dos CPE y 32 túneles candidatos por sucursal. La continuidad exige un acceso utilizable en cada extremo. Los proveedores pueden ser distintos. La conectividad móvil conserva un camino, con capacidad y concurrencia degradadas. Ver continuidad-cuatro-wan-cm.md y el presupuesto vigente; esta revisión sustituye los importes de cortes anteriores.


## Cierre documental del 27 de octubre

Se concilian flujo anual, WAN a 60 meses y diferencia sobre la referencia presupuestaria. E4 representa la caída completa de una sucursal; E6 conserva acceso móvil también en central. La escena 10 incorpora recuperación de datos y conciliación sin modificar las compras. La evidencia histórica y las verificaciones públicas nuevas se presentan con sus alcances separados.

[Registro de evidencia y reproducción pública](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md).
