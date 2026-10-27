# Bitácora académica de evolución del proyecto

**Hugo Eduardo Herrera Inostroza - Proyecto de Título APT - Financiera Pacífico**

## 1. Alcance del registro

Esta síntesis conserva la secuencia de las entradas 001–042 de la bitácora de trabajo del 17 al 23 de octubre de 2026. Los hitos 43 y 44 resumen el cierre técnico y la preparación de la carpeta docente. La primera entrega y la retroalimentación preceden a estos registros, sin asignarles una fecha de revisión no comprobada.

Las propuestas, cifras y pendientes históricos describen su momento. No sustituyen el corte vigente C5 A/B. Se distingue desarrollo del prototipo, propuesta de implantación y trabajo efectivamente realizado: no se registran compras, contratos o instalación física como hechos.

## 2. Estado de cierre

23 sedes actuales, 650 PCs y 650 teléfonos adoptados. ANTES tiene dos MPLS centrales de 1 Gbps, dos ISP de 500 Mbps y un MPLS de 100 Mbps por sucursal. DESPUÉS usa cuatro WAN en central y cuatro por sucursal, sin MPLS. A: CLP 793.126.897 inicial / 1.503.734.277 a 60 meses. B: CLP 281.194.478 inicial / 966.801.858 a 60 meses. WAN común 11.010.123 CLP/mes. Las seis aperturas están separadas.

Los hosts existentes incorporan recuperación de VMs con réplica/quórum, ampliación de DC-02 y enlaces a ambos switches. La homologación de equipos físicos no es un pendiente de la entrega académica ficticia.

## 3. Secuencia de cambios

### 001. Continuidad y servicios centrales (17-10-2026)

Se identifican puntos únicos de falla en router, firewall y servicios. Se exige distinguir redundancia de equipos, independencia de caminos y recuperación de aplicaciones.

### 002. Inventario y procedencia (17-10-2026)

Se revisa la ficha del Capstone y se separan trabajadores, usuarios TI e inventario técnico adoptado. Se aclara la ubicación central de telefonía y servicios.

### 003. Alcance geográfico (17-10-2026)

Hanga Roa y Base Frei quedan dentro de las 23 sedes iniciales; no se cuentan como aperturas futuras. El crecimiento adicional se mantiene separado.

### 004. Primera investigación de hardware (17-10-2026)

Se comparan equipos, capacidades y precios referenciales. El resultado es un escenario preliminar sujeto a dimensionamiento, sin compras o cotizaciones adjudicadas.

### 005. Definición del ANTES (17-10-2026)

Se documentan modelos, puertos compartidos teléfono-PC y dependencias del datacenter como supuestos. Se conservan los elementos redundantes ya existentes.

### 006. Seguridad y alcance de cumplimiento (17-10-2026)

Se amplía el diagnóstico de control y responsabilidades. Se diferencia obsolescencia de incumplimiento legal; la naturaleza regulatoria de la entidad ficticia no se presume.

### 007. Integración del inventario inicial (17-10-2026)

El navegador muestra sedes, puestos, teléfonos, servidores y fallas del ANTES. La excepción satelital inicial de S21/S22 se corrige posteriormente en las entradas 010/011.

### 008. Dimensionamiento inicial de renovación (17-10-2026)

Se calculan puertos, crecimiento, PoE, túneles y recursos de servicios. Dos switches por sede se evalúan por capacidad y función, evitando agregar un tercero sin necesidad.

### 009. Candidata de consolidación en NGFW (17-10-2026)

Se estudia concentrar routing/VPN/QoS en firewalls remotos para reducir equipos. Esa alternativa evoluciona a C4 y luego se sustituye por C5 con routers remotos.

### 010. Corrección del transporte ANTES (17-10-2026)

Se adopta MPLS por cable para todas las ubicaciones del caso, incluidas las especiales, como premisa ficticia. Se elimina la excepción satelital introducida en la base inicial.

### 011. Consistencia funcional del ANTES (17-10-2026)

Inventario, topología y caminos se sincronizan con MPLS remoto y navegación centralizada. Se explicita el único enlace de cada host existente y su dependencia del switch.

### 012. Hipótesis de carga y respaldo (17-10-2026)

Se añaden perfiles normal/exigente, voz y almacenamiento con recursos explícitos. El enlace central único y los ISP de 300 Mbps de esta etapa se sustituyen en revisiones posteriores.

### 013. C4 de cuatro WAN y NGFW remotos (17-10-2026)

Se propone par PA-540 por sucursal, PA-1410 central y cuatro transportes. Se revisan puertos físicos, gestión y dominios de falla; este diseño no es el C5 final.

### 014. Capacidad durante fallas (17-10-2026)

Se generan 64 escenarios de carga/crecimiento y pérdida de enlaces. Se evita sumar velocidades nominales sin considerar sentido, ruta activa o capacidad sobreviviente.

### 015. Jerarquía documental (17-10-2026)

Se establece un diseño maestro que diferencia ANTES, candidata C4 y expansión. Los datos de futuros puestos se separan de compras iniciales.

### 016. Presupuesto por alcance (17-10-2026)

Se separan hardware y ATP prepagado 60 meses, partidas sin precio y horizonte 60/72. Se impide volver a cobrar cada año un servicio ya prepagado.

### 017. Candidata DC3 (17-10-2026)

Se dimensiona un clúster de tres hosts con Ceph y nueve VMs, memoria y redes dedicadas. C5 sustituye después esa compra por recuperación entre los hosts existentes.

### 018. Switching y repositorio DC3 (17-10-2026)

Se comparan switches DC, conectores combo, almacenamiento y red de replicación. Dos cables en una tarjeta no se interpretan como independencia de hardware.

### 019. Alcance de hosts y soporte (18-10-2026)

Se diferencia cantidad objetivo de nodos y cantidad nueva por comprar. Se revisan tarjetas independientes, ranuras, arranque y soporte de la candidata DC3.

### 020. Migración del prototipo a C4/DC3 (18-10-2026)

El modelo integra NGFW remotos/centrales, tránsitos y dependencias de energía/enlaces. Se separa control HA de datos sin afirmar prevención universal de split-brain.

### 021. Sincronización documental C4 (18-10-2026)

Se concilian informe, IPAM, topologías y planilla con las cantidades C4. La ficha académica original se conserva sin alterar.

### 022. Revisión de protocolos y mediciones (18-10-2026)

Se detectan instrucciones de configuración que aún correspondían a otra versión. Se añade cálculo offline de pérdida/RTT con muestras identificadas, sin atribuir mediciones físicas.

### 023. Dependencias de energía y operación (18-10-2026)

Se corrige el dominio energético de switches DC y se documentan rollback, responsabilidades y plan de doce semanas. No se infiere autonomía a partir de contar UPS.

### 024. Metodología del prototipo web (18-10-2026)

Se formaliza el simulador propio como prototipo académico, con pruebas y límites. Los ensayos de fabricantes se reservan para una eventual implementación y no un segundo prototipo pendiente.

### 025. Capacidad activa y pérdida de CM (18-10-2026)

Se distingue disponibilidad lógica de capacidad útil. La pérdida del edificio central retira servicios y copias locales; en esa versión se conservaba Internet local remoto, distinto del full tunnel C5.

### 026. Perfil central y recuperación externa C4 (18-10-2026)

Se estudian radios centrales 2,5G y recuperación AWS como propuesta dimensionada. Esos recursos no se mantienen como compra/aprovisionamiento del cierre C5.

### 027. Dimensionamiento del transporte anterior (18-10-2026)

Se confirma que 100 Mbps remotos cubren carga normal y se elevan los ISP centrales a 500 Mbps. Se diferencia referencia comercial de un contrato de la financiera.

### 028. Historia de la base ANTES (18-10-2026)

Se adopta origen 2006, renovación 2011–2013 y mejoras parciales hasta 2025. No se atribuyen todos los equipos a 2006; el segundo MPLS central se incorpora posteriormente.

### 029. Corrección de referencia de tarifas (18-10-2026)

Se corrigen unidades, proveedor y valores de una fuente contractual pública. La estimación histórica pasa a 11.423.822 CLP/mes, sin presentarla como factura ni ahorro.

### 030. Matriz de carga por sede (18-10-2026)

Se calculan caudal, consumo y reservas por23 sedes con supuestos comunes. Se analiza sensibilidad de cuotas y degradación, sin confundir demanda calculada con medición.

### 031. Expansión separada (18-10-2026)

Se fijan 23 sedes/650 puestos; 29/830 tras aperturas y 29/967 con crecimiento adicional. Las seis aperturas no se compran ni cobran en la fase inicial.

### 032. Límites de continuidad C4 (18-10-2026)

Se consolida la candidata y se ejecuta una auditoría de 299 casos del modelo. Se describen puestos afectados, capacidad y pérdida de CM sin prometer disponibilidad absoluta.

### 033. Respaldo Wi-Fi independiente (18-10-2026)

Se diseña contingencia inalámbrica para PC y teléfono con radios y direcciones propias. El modelo telefónico T54W se incorpora al diseño y luego C5 lo adopta como inventario existente.

### 034. Cierre histórico C4/DC3 (18-10-2026)

Se concilian Excel, informe y topologías de esa versión. Inicial 1.724.961.010 y alcance 60 meses 4.587.531.835 CLP son cifras históricas reemplazadas por C5.

### 035. Fichas C5 con reutilización (22-10-2026)

Se vuelve a routers en sucursales y seguridad solo central, conservando hosts y teléfonos. A define 37 routers/27 switches nuevos y sus licencias, reduciendo alcance respecto de C4/DC3.

### 036. Base económica C5-ECO-1 (22-10-2026)

Se fija A 817.268.133 iniciales y 1.526.153.453 a 60 meses, con WAN 10.981.422/mes. Una huella de precios/cantidades detecta variaciones silenciosas.

### 037. Alternativa B de menor costo (22-10-2026)

Se incorpora MikroTik/OPNsense y comparación A/B. B 303.737.301/987.622.621 es una primera cifra, luego corregida al sustituir distribuidores y cables.

### 038. Concordancia del navegador con C5 (22-10-2026)

Se reemplaza el inventario C4 activo por las fichas C5 A/B. Ping, terminal, mapa, fallas y reservas Wi-Fi consultan el mismo motor; B utiliza 42 CCR2004 y dos RB5009 en S22.

### 039. Interfaz de demostración integrada (23-10-2026)

Se integra comparación de escenarios sobre la topología y el motor del prototipo. La validación comprueba navegación, reconstrucción de fallas y restauración del estado.

### 040. Política de seguridad C5 (23-10-2026)

Se incorporan matriz de servicios, ACL de acceso/gestión y filtros de host APP/BD. Se definen AAA, NOC y dependencias de autenticación sin agregar servidores físicos.

### 041. Capacidad y visualización WAN (23-10-2026)

Se fija Starlink central 1000/1000 Mbps como supuesto y se separan puerto, servicio y máximo de terminal Leo. Se explicita que el pico de video supera capacidad y exige admisión.

### 042. Dispositivos y HA de hosts (23-10-2026)

Se reemplaza JSON interno por estado/interfaces/configuración legibles. ANTES queda con dos MPLS centrales de 1 Gbps; DC-02 se amplía mediante reasignación y se integra réplica/quórum/fencing.

### 043. Cierre de WAN B y evidencias (23-10-2026)

Se sustituyen 46 C1300 de B por 45 hEX y un CRS310, se ajusta DEC3852 y 44 DAC de 10G. B cierra 280.617.592 iniciales y 964.502.912 a 60 meses; las pruebas finales están registradas.

### 044. Paquete para revisión docente (23-10-2026)

Se incorporan caso original/transcrito, diagnóstico corregido, E1–E7 y anexos. Se completan plan anual, flujo de costos, mecanismos de detección, unitarios, controles y respuesta a observaciones.

## 4. Evidencia y cierre de versiones

La revisión de red 228ec26 registra 78 pruebas de lógica, 144 de navegador en la pasada general y 31 en la pasada final; las pasadas no se suman como casos únicos. Hay 1.351 comprobaciones adicionales de caminos y 21 controles de generación. Los workflows de simulador, LAN/LACP y Pages están aprobados para ese corte.

C4/DC3, los precios preliminares y los estados de pruebas pendientes de entradas anteriores son antecedentes. La fuente vigente para cantidades y costo es C5 A/B y sus presupuestos; para el comportamiento, el simulador y E6. La pérdida completa de CM, sesiones físicas y rendimiento instalado mantienen sus límites explícitos.

## 5. Trazabilidad de los cambios finales

- 72f99a8: vistas de dispositivo, MPLS central y HA de hosts.
- e158de2: máscara de BKP/gestión.
- 7bb4b70: modelo visible WAN-A/B y conectividad simulada.
- 228ec26: distribuidores WAN B, interfaces, sincronización y presupuesto.
- 62e832d: cierre de documentos y constructores de anexos.
- 596221d: organización de E1–E7.

La preparación del paquete docente modifica documentación, no el motor de red ni los totales económicos adoptados.

## 6. Cierre de distribución WAN común (24-10-2026)

Se unifica el criterio de distribución WAN entre las alternativas A y B, sustituyendo los distribuidores de A por equipos MikroTik: 45 MikroTik hEX E50UG y un CRS310-8G+2S+IN. Los 44 hEX remotos usan ether1/2 para CPE, ether3/4 para routers y ether5 para gestión. En central, ether1 enlaza el CPE, ether2/3 el par de firewalls y ether4 gestión. No hay NAT, DHCP ni terminación VPN en esta función.

La revisión C5-ECO-2-WAN-MIKROTIK reemplaza C5-ECO-1 sin alterar WAN mensual ni el resto del alcance. El subtotal disminuye CLP 21.494.019, la contingencia CLP 3.224.103 y el inicial CLP 24.718.122. A queda en CLP 792.550.011 iniciales y 1.501.435.331 a 60 meses. B conserva CLP 280.617.592 / 964.502.912. Las cifras de las entradas históricas describen su revisión original.


## 7. Continuidad WAN-3 (25-10-2026)

Se añaden Entel y WOM también en Casa Matriz. El diseño queda en 92 servicios y 704 túneles candidatos por alternativa, con conectividad condicionada a un acceso utilizable en cada extremo, políticas, VPN y servicios. Se concilian dos CPE adicionales, mensualidades y flujo a cinco años. Los importes de la sección 6 se conservan como corte WAN-2 histórico.

## 8. Recuperación local y datos (26-10-2026)

La escena 10 y el anexo C5-RECUPERACION-1 muestran réplica completada, dos operaciones por conciliar y bloqueos por mayoría, aislamiento, antigüedad e inconsistencia. Se utilizan DC-01, DC-02 y BKP-01 existentes; la ampliación de DC-02 ya forma parte del presupuesto. RTO 300 s y RPO 60 s siguen como objetivos sin medición física.

## 9. Consolidación de la entrega (27-10-2026)

Se corrigen cifras antiguas del informe y del flujo anual, se actualiza E6 y se completa E4 como caída de sitio. Los enlaces de consulta académica apuntan a material público. Se añade reproducción pública de alcance explícito y se regeneran PDF, paquete y manifiesto. Las cifras históricas de pruebas se conservan como registros declarados; no sustituyen una ejecución verificable sobre el nuevo corte.
