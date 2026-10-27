# Entregable 1 — Diagnóstico y definición del problema

**Financiera Pacífico · edición C5 A/B, revisión WAN-3 · cierre documental 27 de octubre de 2026**

## 1. Resumen ejecutivo

Financiera Pacífico necesita conservar el acceso a su aplicación financiera, telefonía y servicios de apoyo cuando falla un enlace o un equipo. El problema principal de la red anterior es su dependencia de un acceso, un router y un switch por sucursal. Casa Matriz ya tiene redundancia parcial, pero conserva un único firewall y servidores con funciones separadas sin recuperación automática entre hosts.

La propuesta incorpora caminos alternativos, dos routers y dos switches por sucursal, un par de firewalls centrales y recuperación de máquinas virtuales entre los servidores existentes. El simulador permite comparar el ANTES con dos opciones de equipamiento del DESPUÉS: A Cisco/Palo Alto y B MikroTik/OPNsense. La demostración explica qué sigue funcionando y qué se pierde en cada falla.

## 2. Antecedentes y alcance

| Elemento | Definición |
|---|---|
| Ficha original | Casa Matriz + 21 sucursales = 22 sedes; 780 trabajadores y aproximadamente 650 usuarios TI |
| Adaptación del equipo | Casa Matriz + 22 sucursales = 23 sedes, incluidas Hanga Roa y Base Frei |
| Inventario de puestos adoptado | 650 PCs y 650 teléfonos SIP-T54W existentes; un teléfono por puesto |
| Horizonte económico | 60 meses |
| Crecimiento reservado | Seis sucursales adicionales; 29 sedes futuras en total |
| Objetivos de la ficha | Core 99,99 %; sucursales 99,95 %; recuperación de sucursal ≤300 s |
| Referencia presupuestaria original | CLP 160.000.000; ambas alternativas la superan |
| Caso | Proyecto ficticio; equipos, carga y acuerdos de operadores son supuestos identificados |

Fuente académica: `Capstone_Ingenieria_Conectividad_Redes.xlsx`. La adaptación a 23 sedes se declara como decisión del equipo y no como dato literal de esa ficha. Casa Matriz y su datacenter cuentan como una sola sede. Los seis sitios futuros no se cuentan como instalaciones actuales.

## 3. Infraestructura ANTES

Cada sucursal tiene un router, un switch PoE y un MPLS de 100 Mbps. El inventario es mixto: existen equipos antiguos y renovaciones parciales. No se describe toda la red como si conservara exactamente los mismos modelos desde 2006.

Casa Matriz tiene dos Cisco 2911, dos C9200L-48P-4X-E existentes, un ASA5512 y **dos circuitos MPLS de 1 Gbps cada uno**, además de dos ISP de 500 Mbps cada uno. En total hay 24 circuitos MPLS: dos centrales y 22 remotos. Dos circuitos de 1 Gbps no convierten un flujo en uno de 2 Gbps ni dan redundancia al único acceso de la sucursal.

La aplicación y base de datos se alojan en DC-01; PBX, DNS/NTP y monitoreo en DC-02; BKP-01 es un repositorio separado dentro del mismo edificio. Los tres tienen un enlace de acceso en ANTES. Los modelos académicos asignados son Dell PowerEdge R740 para DC-01/DC-02 y R540 para BKP-01.

La carga normal calculada de una sucursal de 30 puestos alcanza aproximadamente 26,4 Mbps: **100 Mbps sí cubren ese perfil**. La modernización se justifica por continuidad, seguridad, crecimiento y gestión, sin inventar saturación permanente o incidentes observados.

### Inventario por sede

| Sede | Ubicación | PCs / teléfonos | Router ANTES | Switch ANTES |
| --- | --- | --- | --- | --- |
| CM | Santiago Centro | 55 / 55 | CISCO2911-SEC/K9 | C9200L-48P-4X-E |
| S01 | Providencia | 30 / 30 | CISCO1921-SEC/K9 | WS-C2960S-48LPS-L |
| S02 | Las Condes | 30 / 30 | ISR4321/K9 | C9200L-48P-4G-E |
| S03 | Maipú | 30 / 30 | CISCO1921-SEC/K9 | WS-C2960S-48LPS-L |
| S04 | Puente Alto | 30 / 30 | ISR4321/K9 | C9200L-48P-4G-E |
| S05 | La Florida | 30 / 30 | ISR4321/K9 | C9200L-48P-4G-E |
| S06 | Arica | 28 / 28 | ISR4321/K9 | C9200L-48P-4G-E |
| S07 | Iquique | 28 / 28 | ISR4321/K9 | C9200L-48P-4G-E |
| S08 | Antofagasta | 28 / 28 | ISR4321/K9 | C9200L-48P-4G-E |
| S09 | Copiapó | 28 / 28 | C1121X-8P | C9200L-48P-4G-E |
| S10 | La Serena | 28 / 28 | ISR4321/K9 | C9200L-48P-4G-E |
| S11 | Valparaíso | 28 / 28 | CISCO1921-SEC/K9 | WS-C2960S-48LPS-L |
| S12 | Rancagua | 28 / 28 | CISCO1921-SEC/K9 | WS-C2960S-48LPS-L |
| S13 | Talca | 28 / 28 | ISR4321/K9 | C9200L-48P-4G-E |
| S14 | Chillán | 28 / 28 | C1121X-8P | C9200L-48P-4G-E |
| S15 | Concepción | 28 / 28 | CISCO1921-SEC/K9 | WS-C2960S-48LPS-L |
| S16 | Temuco | 28 / 28 | ISR4321/K9 | C9200L-48P-4G-E |
| S17 | Valdivia | 28 / 28 | C1121X-8P | C9200L-48P-4G-E |
| S18 | Puerto Montt | 28 / 28 | ISR4321/K9 | C9200L-48P-4G-E |
| S19 | Coyhaique | 28 / 28 | C1121X-8P | C9200L-48P-4G-E |
| S20 | Punta Arenas | 28 / 28 | C1121X-8P | C9200L-48P-4G-E |
| S21 | Hanga Roa (Isla de Pascua) | 17 / 17 | C1121X-8P | C9200L-24P-4G-E |
| S22 | Antártica Chilena | 8 / 8 | C1121X-8P | C9200L-24P-4G-E |

## 4. Brechas y respuesta

| Riesgo | Efecto | Respuesta del rediseño |
|---|---|---|
| Acceso/router único remoto | La sucursal pierde el camino a CM al fallar ese elemento | Cuatro transportes y dos routers |
| Switch único remoto | Los puestos conectados pierden acceso | Dos switches y Wi-Fi de contingencia para PC/teléfono |
| ASA central único | Interrumpe la salida y el acceso a servicios centrales | Dos firewalls en activo/pasivo |
| Servicios concentrados por host | Caer un servidor detiene sus servicios | Réplica, quórum y reinicio de VMs en el host superviviente |
| Copias en el mismo edificio | No resuelven pérdida completa de CM | Límite explícito y procedimiento de recuperación externa fuera del alcance financiado actual |
| Cambios manuales y permisos amplios | Errores y accesos innecesarios | Configuración versionada, ACL, registros y gestión restringida |

## 5. Objetivos y aceptación académica

Diseñar y demostrar caminos alternativos, segmentación, política de acceso, redundancia de equipos y recuperación de hosts. Los objetivos anuales de disponibilidad se mantienen en el informe; la barra del simulador muestra **conectividad simulada**, no uptime anual medido. E6 identifica pruebas realizadas y límites de la evidencia.

El alcance no incluye comprar de nuevo PCs, teléfonos, hosts completos, UPS ni racks existentes. Sí incluye cableado de interconexión, puertos, módulos, adaptación del clúster y servicios de implantación presupuestados. Los contratos pertenecen al servicio del operador; la ingeniería de conexión de nuestra red pertenece al diseño.

La homologación de equipos físicos no es un entregable académico pendiente de este proyecto ficticio. El prototipo entregado es el simulador web propio.

## 6. Criterio técnico del diagnóstico corregido

Los ISR 2911 y Catalyst 3560 mencionados en el borrador inicial pueden ofrecer routing, VLAN/802.1Q, QoS y VPN según familia, licencia e imagen. No se justifica la renovación negando esas capacidades ni limitando el router arbitrariamente a tres o cuatro túneles. El inventario C5 actual es mixto y conserva equipos recientes donde cumplen la función definida.

Los riesgos se justifican por puntos únicos de falla, capacidad con servicios habilitados, ciclo de soporte, actualizaciones y crecimiento. La caída MPLS de tres horas pertenece al caso; no demuestra que todas las fallas duren ese tiempo, que el RTO se haya medido incumplido ni que exista una tasa real de incidentes.

No se atribuyen a Financiera Pacífico los 180 ms/6 % de pérdida de otro caso. La operación de MPLS no prueba ausencia de cifrado, y tener un NMS central es un antecedente oficial: la mejora propuesta es reforzar su alcance y la trazabilidad, no inventar que no existía monitoreo.

## 7. Fuentes de esta edición

[Datos vigentes A](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Inventario_IPAM_Puertos.md), [datos B](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Inventario_IPAM_Puertos.md), [revisión final](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md) y [anexo de inventario, IP y puertos](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Inventario_IPAM_Puertos.md). Las versiones C4/DC3 y la edición documental del 15 de octubre son antecedentes históricos.

Revisión WAN-3 del 25/10: [cuatro accesos en central y continuidad extremo a extremo](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Continuidad_Cuatro_WAN_25_oct_2026.md).
