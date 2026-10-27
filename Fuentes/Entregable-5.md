# Entregable 5 - Prototipo y demostración de la WAN

**Financiera Pacífico - C5 A/B - cierre documental 27 de octubre de 2026**

## 1. Objetivo

Demostrar la coherencia de una red WAN de 23 sedes y 650 puestos mediante un simulador web propio. El prototipo integra topología, inventario por dispositivo, direccionamiento, políticas y motor de caminos. Permite contrastar el ANTES con A Cisco/Palo Alto y B MikroTik/OPNsense.

[Acceso al prototipo](https://hu-herrera.github.io/fina/). La evidencia reproducible y sus alcances se detallan en E6.

## 2. Componentes implementados

| Componente | Función verificable |
|---|---|
| Inventario por sede | Modelos, función, direcciones y equipos anteriores/propuestos |
| Ficha de dispositivo | Estado, interfaces, VLAN, IP, puerto local y vecino |
| Motor de caminos | Ruta de ida/retorno, dependencias y política del flujo |
| Fallas | Puerto, enlace, proveedor/upstream, router, switch, distribuidor, firewall, AP y hosts |
| VPN lógica | Elegibilidad de candidatos y extremos centrales por transporte |
| Seguridad | APP, BD, voz, DNS/NTP, AAA, invitados y gestión con mínimo privilegio |
| Acceso de contingencia | Wi-Fi independiente de PC y teléfono, condicionado por AP/AAA |
| HA central | Relevo de firewall y sincronización diferenciados por A/B |
| HA de servidores | Recuperación de VMs con réplica/quórum/fencing; bloqueo si faltan condiciones |
| Datos comunes | Topología, configuración educativa, inventario y presupuesto alimentados por JSON |

## 3. Escenarios demostrados

ANTES opera con MPLS y pierde conectividad remota al cortar su único acceso. DESPUÉS conserva alternativas ante fallas individuales de WAN, router o distribuidor. La caída de un switch retira el acceso cableado de sus puestos; el respaldo inalámbrico exige AP y autenticación disponibles.

La matriz de permisos diferencia HTTPS a la aplicación de acceso directo a BD, voz hacia PBX, DNS corporativo, invitados aislados y administración desde NOC. El resultado distingue «permitido por política» de «destino alcanzable».

La pérdida de un firewall central permite relevo por el miembro elegible. En B, perder pfsync genera una condición de sincronización sin inventar la desaparición de todos los caminos CARP. La pérdida de un host permite recuperar VMs críticas si hay quórum/réplica; la pérdida de ambos o de las condiciones necesarias bloquea la recuperación.

## 4. Concordancia física y lógica

A usa sus modelos/puertos Cisco y Palo Alto. B usa su mapa propio, con los distribuidores hEX/CRS310, dos enlaces LACP de 10G por pareja remota y el inventario de cuatro RJ45/dos SFP+ por DEC3852. El modelo B no hereda StackWise ni HSCI. Los enlaces de gestión no se utilizan como caminos de negocio.

La conexión teléfono-PC comparte un puerto de acceso. Las reservas IP Wi-Fi se activan por equipo, sin simular que el PC alimenta al teléfono o que una dirección reservada está activa permanentemente.

## 5. Indicadores y exportación

La barra muestra conectividad simulada del escenario. No equivale a disponibilidad anual medida. Los diagnósticos registran camino, regla y falla. Las fichas permiten consultar configuración educativa TXT y exportación técnica, separadas del resumen operativo; el JSON de datos no se presenta como configuración nativa de fabricante.

Los comandos de consulta y de control del simulador usan su propio entorno educativo. No se ejecutan imágenes de firmware, protocolos OSPF/IPsec reales, aplicaciones financieras ni llamadas SIP.

## 6. Resultado académico

Se entrega un prototipo operativo con fuentes versionadas y pruebas automatizadas. La validación acredita el comportamiento del modelo y su interfaz; tiempos físicos, rendimiento inspeccionado, conservación de llamadas/sesiones y cumplimiento normativo no se inventan a partir de una animación. La homologación física no forma parte de los entregables pendientes del caso ficticio.

Revisión WAN-3 del 25/10: [cuatro accesos en central y continuidad extremo a extremo](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Continuidad_Cuatro_WAN_25_oct_2026.md).
