# Entregable 4 — Diseño de bajo nivel (LLD)

**Financiera Pacífico · edición C5 A/B, revisión WAN-3 · cierre documental 27 de octubre de 2026**

## 1. Especificación y trazabilidad

Las fichas JSON alimentan la topología, las vistas de dispositivos y el anexo técnico. El [inventario/IPAM/puertos A/B](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Inventario_IPAM_Puertos.md) incluye, para cada sede, modelos ANTES/DESPUÉS, direcciones, VLAN, conexiones y 650 puestos con sus IP cableadas y reservas Wi-Fi. Es parte integral de este entregable.

[Fuente A](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Inventario_IPAM_Puertos.md) · [fuente B](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Inventario_IPAM_Puertos.md) · [ACL Cisco](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/ACL_Acceso_C5_Cisco.txt) · [reglas comunes](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Politica_Seguridad_C5.json).

## 2. Plan de direccionamiento

N es el número de sede (0 para CM, 1–22 para sucursales). Las reservas nuevas 10.80/10.81/10.82 y 10.253 complementan la red corporativa original 10.70/16; no se presentan como subredes contenidas dentro de 10.70/16.

| Función | VLAN | Red típica | Gateway |
|---|---|---|---|
| Datos cableados | 10 | 10.70.N.0/25 | .1 |
| Voz cableada | 20 | 10.70.(64+N).0/25 | .1 |
| Invitados | 40 | 10.70.(96+N).0/26 | .1 |
| Datos Wi-Fi | 110 | 10.81.N.0/25 | .1 |
| Voz Wi-Fi | 120 | 10.82.N.0/25 | .1 |
| Gestión | 130 | 10.80.N.0/27 | .1 lógico según variante |
| Servidores, solo CM | 50 | 10.70.200.0/24 | 10.70.200.1 |
| Tránsito stack–firewall, CM | 131 | 172.31.0.0/29 | .1 stack / .2 par HA |
| Underlay de operadores | 201–204 | Bloques 10.252 por sede | Direcciones de CPE/miembros en anexo |
| Overlay | Túneles L3 | 10.253.N.0/25 | 32 redes /30 por sucursal |

Los tránsitos router–switch de una sucursal son cuatro /30 dentro de 172.31.N.0/28. Los puertos LAN internos de C 1121 X usan VLAN/SVI cuando son puertos de switch; no se les atribuye `no switchport` indiscriminadamente. No se forma un EtherChannel combinando los dos routers.

Los extremos públicos documentales centrales están en 198.51.100.0/29 y 203.0.113.0/29 (RFC5737); las direcciones .4 representan los extremos virtuales. No son IP públicas asignadas por un operador. B reserva 172.31.255.0/30 para sincronización central dedicada.

## 3. Cableado y puertos

WAN-A remota: dos puertos hacia CPE, dos trunks hacia routers y uno de gestión. WAN-B repite esa distribución con Leo/WOM. Los trunks WAN solo transportan las VLAN del operador correspondiente; la gestión 130 llega por puerto independiente. En A y B los cinco puertos del hEX quedan asignados a esas funciones.

Cada router tiene un enlace de datos a cada switch y un acceso de gestión según ficha. En A los puertos remotos 19/20 reciben los tránsitos L3;21 gestión router;22 gestión distribuidor;24 AP. La tabla exacta varía por modelo y está en el anexo; no se hereda automáticamente de A a B.

El PC conecta detrás del teléfono, compartiendo el puerto de acceso con datos 10 y voz 20. Los AP transportan 40/110/120/130, con nativa sin servicio 999. Ante falla de switch, PC y teléfono usan radios independientes y su dirección Wi-Fi reservada, si AP y AAA están disponibles. El teléfono requiere su propia alimentación; el PC no lo alimenta por Wi-Fi.

### Central por variante

| Función | A · PA-1410 | B · DEC3852 |
|---|---|---|
| WAN-A | ethernet 1/9 multigig | Un RJ 45 de 2,5G |
| WAN-B | ethernet 1/1 | Un RJ 45 de 2,5G |
| LAN | ethernet 1/19 y /20,10G | Dos SFP+ de 10G |
| Gestión | MGT separado | Un RJ 45 |
| Sincronización | HA1-A, HA1-B, HSCI y respaldo HA2 | Un RJ 45 dedicado, pfsync/XMLRPC |
| Elección de activo | HA A/P PAN-OS | CARP sobre interfaces de servicio |

DEC3852 usa cuatro RJ 45 y dos SFP+ por miembro. Perder su enlace de sincronización no equivale a perder todos los caminos de servicio; se alerta sobre estado/sesiones sin inventar una caída de ambos firewalls. Los nombres WAN/LAN/SYNC de B expresan roles de la especificación, no nombres de interfaz PAN-OS.

DC-01 conecta NIC 1/NIC 2 a puerto 43 de SW 1/SW 2; DC-02 a 44; BKP-01 a 45. Los hosts transportan VLAN50/130 y usan bond activo/reserva. BKP usa VLAN50/24; su máscara no es la/27 de gestión de hipervisores.

## 4. Enrutamiento, VPN y Qo S

IKEv2/IPsec route-based con NAT-T, identidades distintas, selección de origen y tablas de transporte separadas. El underlay no intercambia sus defaults con la tabla de negocio. Se comprueban camino de ida/retorno, salud del túnel y dependencia de servicios centrales. No se mantiene un default de negocio únicamente porque el CPE responda.

La prioridad de transporte no suma automáticamente velocidades para una sesión. Se conserva ruta útil al perder un equipo/enlace cuando queda un camino válido. La Qo S prioriza aplicación financiera y voz; no crea capacidad cuando el transporte sobreviviente resulta insuficiente. Se limita video y se programan copias.

## 5. Matriz de servicios y permisos

| Origen → destino | IP destino | Puerto/servicio | Política |
|---|---|---|---|
| Usuarios → aplicación | 10.70.200.10 | TCP 443 | Permitir |
| Usuarios → BD | 10.70.200.11 | TCP 5432 | Denegar |
| Aplicación → BD | 10.70.200.11 | TCP 5432 | Permitir solo desde APP |
| Teléfonos → PBX | 10.70.200.20 | TCP 5061, UDP 10000–20000 | Señalización/medios y retorno autorizado |
| Red corporativa → DNS/NTP | 10.70.200.30 | TCP/UDP 53, UDP 123 | Permitir según segmento |
| Equipos autorizados → AAA | 10.70.200.31 | UDP 1812/1813, TCP 49 | Restringir a gestión/autenticación |
| Gestión → NMS/logs | 10.70.200.40 | SNMPv3 y syslog TLS según dirección del flujo | Acceso controlado |
| NOC → administración | NOC 10.80.0.10 como origen | SSH/HTTPS y servicios de gestión definidos | Solo origen autorizado |
| Invitados → redes internas | Redes corporativas | Cualquiera | Denegar |
| Hosts → repositorio/testigo | 10.70.200.50 | TCP 8007/TCP 5403 | Par de hosts autorizado |

APP y BD comparten VLAN50: sus filtros de host son necesarios porque el tráfico local no atraviesa automáticamente el firewall central. Corosync UDP 5405–5412, réplica SSH TCP 22 y migración TCP 60000–60050 se restringen al par de hosts; administración TCP 8006 solo desde NOC. Las ACL de entrada incluyen antispoofing y retornos necesarios, sin un permiso general final.

SNMPv3 usa autenticación/privacidad; las ACL de gestión no sustituyen autenticación. No se publican contraseñas, claves privadas ni PSK. La excepción ICMP temporal del simulador se limita a dos IP activas y no abre TCP/UDP ni otra VLAN.

## 6. Detección de fallas y selección de ruta

OSPF recalcula rutas cuando cambia la información disponible; no prueba por sí solo la salud de un proveedor o de una aplicación. El diseño separa detección, elección de camino y retorno:

| Capa | Mecanismo de diseño | Comprobación en el prototipo |
|---|---|---|
| Puerto/enlace | Estado de interfaz y adyacencia; detección de vecino, con BFD solo si la plataforma/versión lo admite | Corte de puerto/enlace y eliminación de ese camino |
| Upstream con portadora | A: IP SLA y tracking; B: Netwatch/sondas y control de rutas por transporte | Estado upstream fallido aunque el enlace físico siga activo |
| VPN | DPD y supervisión del extremo remoto; retirada del camino overlay si falla | Túnel lógico no elegible |
| Servicio | Sondas a aplicación, DNS y PBX, separadas del ping al CPE | Dependencias de hosts/servicios centrales |
| Retorno | Confirmación de estabilidad y retorno controlado, evitando oscilaciones | Estado «recuperando» y espera didáctica de cinco segundos del escenario E7 |

Las sondas deben salir por el transporte que evalúan; si usan otra WAN producirían un falso positivo. La política propuesta usa varios destinos y confirmación de fallas antes del cambio. Los intervalos instalados y temporizadores BFD/DPD dependen de plataforma y se definen para respetar el objetivo de 300 s. No se presentan los cinco segundos de animación como convergencia física medida ni como configuración universal de fabricante.

La caída de Casa Matriz no activa salida local sin inspección en esta arquitectura full tunnel. La ausencia de camino se informa como indisponibilidad, aunque un router remoto conserve su interfaz de Internet.

## 7. Correspondencia con los siete escenarios solicitados

| Escenario del profesor | Tratamiento en el diseño vigente |
|---|---|
| Caída MPLS de sucursal | ANTES pierde su único acceso. DESPUÉS no conserva MPLS: se prueba pérdida del principal Starlink y uso de otra WAN |
| Caída de Internet de respaldo | Pérdida de Leo o de un respaldo móvil conserva otro camino solo si está disponible; alarma sin prometer capacidad plena |
| Router principal de Casa Matriz | ANTES se comprueba el otro router y sus accesos. En DESPUÉS el routing central corresponde al par de firewalls: se prueba su relevo |
| Caída completa de sucursal | E4 aplica el fallo de sitio en S19: equipos, LAN y cuatro transportes quedan indisponibles. Un respaldo WAN no compensa la pérdida completa de la sede |
| Indisponibilidad del proveedor principal | Se retira ese transporte en las sedes afectadas y se busca alternativa; se consideran fallas correlacionadas |
| Operación 4G/5G | Sucursales y CM conservan Entel/WOM. Un acceso móvil utilizable en cada extremo puede sostener el camino con VPN, permisos y servicios disponibles; la capacidad es degradada |
| Retorno del principal | Se verifica estabilidad y retorno controlado; no se confunde reparación de host con retorno automático de VMs |

## 8. Transporte de subredes y VLAN

Las etiquetas 802.1Q se usan en enlaces locales de acceso/trunk. Cada VLAN tiene una subred y un gateway; sus prefijos IP se enrutan por la VPN. Un túnel IPsec tradicional no extiende automáticamente la VLAN de capa 2 entre sucursales. La política de E4 autoriza los prefijos de datos, voz y gestión según servicio; no anuncia a través del overlay las redes de acceso de operadores ni una ruta que permita saltar el control central.

## 9. Configuración por equipo

Al pulsar un dispositivo se revisan estado, interfaces, VLAN/redes, política, configuración TXT, CLI y exportación. El TXT es la especificación educativa; `sim link` y `sim port` son comandos del simulador. No se anuncian como archivos universales importables en IOS-XE, RouterOS, PAN-OS u OPNsense.



## 10. Relación con controles de seguridad

La ficha exige cifrado y auditoría. La propuesta incorpora IPsec/IKEv2 con AES-256 según la suite seleccionada, gestión autenticada, ACL de mínimo privilegio y registros. Esos controles apoyan objetivos de confidencialidad, restricción de acceso y trazabilidad; no constituyen una certificación PCI DSS o SOX.

Como referencia académica de PCI DSS, los controles de red/segmentación se relacionan con el requisito 1; configuración segura con 2; protección criptográfica en tránsito con 4; accesos/identidad con 7 y 8; y registros/monitoreo con 10. El anexo de fuentes identifica PCI SSC. La aplicabilidad requeriría definir si existen datos de tarjetas y el entorno evaluado. El diseño WAN no verifica políticas, procesos, endpoints, retención y todas las demás exigencias del estándar, por lo que no se afirma cumplimiento integral ni incumplimiento probado del ANTES.

Revisión WAN-3 del 25/10: [cuatro accesos en central y continuidad extremo a extremo](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Continuidad_Cuatro_WAN_25_oct_2026.md).
