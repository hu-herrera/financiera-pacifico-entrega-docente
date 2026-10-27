# Entregable 3 — Diseño de alto nivel (HLD)

**Financiera Pacífico · edición C5 A/B, revisión WAN-3 · cierre documental 27 de octubre de 2026**

## 1. Arquitectura general

La red conecta 22 sucursales con Casa Matriz mediante VPN. Los servicios financieros, PBX, DNS/NTP, AAA y registros residen en CM. La navegación de los usuarios usa **full tunnel**: viaja cifrada a CM y sale por el firewall central. No se activa una salida local sin inspección cuando se pierde el hub.

| Elemento | ANTES | DESPUÉS A/B |
|---|---|---|
| Sucursal | Un router, un switch, un MPLS de 100 Mbps | Dos routers, dos switches, dos distribuidores y cuatro transportes |
| CM | Dos routers, dos switches, un ASA, dos MPLS de 1 Gbps y dos ISP de 500 Mbps | Dos firewalls HA, dos switches existentes y cuatro transportes: Starlink, Leo, Entel y WOM |
| VLAN | Segmentación del escenario base | Datos, voz, invitados, Wi-Fi y gestión con permisos explícitos |
| Datacenter | Funciones por host, un enlace por equipo | Hosts conservados, dos enlaces por equipo, réplica y quórum |
| Puesto | Teléfono y PC comparten puerto de acceso | Se conserva el puesto y se añade contingencia Wi-Fi independiente |

Los planos de CM y S06, para ANTES/A/B, están en [Topologías](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Topologias_ANTES_A_B.pdf). El [anexo técnico](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Inventario_IPAM_Puertos.md) detalla las 23 sedes.

## 2. Distribución WAN y caminos

En cada sucursal WAN-A distribuye Starlink y Entel; WAN-B distribuye Leo y WOM. Cada distribuidor conecta ambos routers. Cada router conecta ambos switches mediante enlaces L3 independientes. La pérdida de un distribuidor elimina dos transportes, dejando un satelital y un móvil en el otro dominio. No hay enlace L2 que mezcle ambos distribuidores ni rutas de negocio por el puerto de administración.

En A el par de switches remoto actúa como stack. En B son dos switches independientes con LACP/RSTP y gateway redundante según la ficha. No se atribuyen StackWise ni 80 Gbps al CRS328. Central mantiene su stack Cisco existente en ambas opciones.

La VPN contempla cuatro transportes y cuatro extremos centrales por router: 16 candidatos por router, 32 por sucursal y 704 en total. Son posibilidades de camino, no 704 sesiones activas obligatorias. El par central activo/pasivo comparte los extremos virtuales; no duplica la cifra por tener dos miembros.

## 3. Capacidad y degradación

Se modela 30 % de puestos concurrentes a 2/0,5 Mbps, voz 10 % a 0,16 Mbps, una reserva de tráfico del 10 % y utilización máxima del 70 %. El perfil general excluye video; el escenario de video se calcula aparte. Copias y actualizaciones se programan o se detienen en contingencia.

| Escenario | Puestos | CM bajada Mbps | CM subida Mbps | Crítico por sentido Mbps |
| --- | --- | --- | --- | --- |
| Actual sin video | 650 | 433,856 | 647,413 | 93,956 |
| Actual con video | 650 | 881,713 | 1088,199 | 93,956 |
| Seis aperturas con video | 830 | 1119,124 | 1401,981 | 119,696 |
| Aperturas, crecimiento y video | 967 | 1212,247 | 1540,786 | 141,374 |

El principal simulado central es 1000/1000 Mbps; el continental remoto 100/100 y el insular/polar 50/50. El perfil actual sin video cabe en CM; el pico actual con video supera 1 Gbps de subida. Se requiere control de admisión de videollamadas y revisar capacidad antes de abrir las seis sedes. Un puerto de 2,5 GbE no es una garantía de 2,5 Gbps de servicio.

Leo central tiene requisito propuesto 200/200 para tráfico crítico y Leo remoto 10/10. Los máximos de terminal y las velocidades móviles no se convierten en mínimos garantizados. La contingencia prioriza aplicación, voz y servicios indispensables; limita video, invitados, actualizaciones y copias grandes.

## 4. Alta disponibilidad de servidores

HA significa **alta disponibilidad**. Aquí consiste en recuperar las máquinas virtuales críticas en el otro host cuando falla uno; no se presenta como una aplicación distribuida activa en dos nodos ni como conservación de todas las sesiones.

DC-01 y DC-02 son Dell R740 de ocho núcleos físicos. DC-01 conserva 64 GiB/2000 GB útiles. DC-02 se amplía de 32 a 64 GiB y de 1000 a 3840 GB útiles. BKP-01, Dell R540 de 8 TB útiles, conserva copias y aloja el testigo. La ampliación de CLP 1.450.000 se reasigna desde la reserva de ingeniería, sin aumentar el total.

Proxmox VE usa réplica ZFS asíncrona y quórum de dos de tres votos. La recuperación requiere réplica utilizable y aislamiento/fencing del host fallado. En contingencia se reservan 52 GiB de VMs críticas y 4 GiB para hipervisor; NMS se pausa. Los 1600 GB replicados más 20 % de margen caben en 2000 GB. El objetivo es RPO 60 s y recuperación 300 s, sin presentarlos como tiempos físicos medidos. Se evita el retorno automático al host reparado.

Perder ambos hosts, el quórum necesario o CM completa impide la recuperación automática. Un repositorio y un testigo en el mismo edificio no equivalen a un segundo datacenter.

## 5. Seguridad y operación

Política de mínimo privilegio: usuarios a HTTPS de aplicación; base de datos solo desde aplicación; voz hacia PBX; invitados aislados; gestión desde NOC. Se controlan retornos, antispoofing y tráfico lateral mediante ACL y firewalls de host donde el tráfico no atraviesa una SVI.

VLAN130 es administración **en banda**; no se anuncia como OOB independiente. La pérdida de toda la WAN impide gestión remota por esa misma red. Se mantienen consola local, respaldos de configuración, alertas, registros centralizados y versiones en Git.

La autonomía eléctrica y el rendimiento instalado no se certifican en el navegador. UPS, climatización e instalaciones existentes son aportes del escenario del cliente, separados de la oferta de red.

## 6. Escalabilidad

Se reservan seis aperturas: San Pedro de Atacama, Ovalle, Los Andes, Los Ángeles, Osorno y Castro. El escenario de capacidad de 30 puestos por nueva sede produce 830 puestos; con crecimiento de sedes existentes llega a 967. Ninguna de esas cifras sustituye los 650 puestos actuales ni implica una compra incluida hoy. E7 separa el costo de expansión.

Revisión WAN-3 del 25/10: [cuatro accesos en central y continuidad extremo a extremo](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Continuidad_Cuatro_WAN_25_oct_2026.md).
