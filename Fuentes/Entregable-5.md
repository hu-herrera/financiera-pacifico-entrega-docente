# Entregable 5 - Prototipo y demostración de la WAN

**Financiera Pacífico - C5 A/B - cierre operativo 28 de octubre de 2026**

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
| VPN simulada | Autenticación, estados IKE/Child SA, contadores, renovación y extremos por transporte |
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

Los comandos consultan o modifican el estado que utiliza el motor de tráfico. OSPF incorpora adyacencias y áreas; la VPN incorpora autenticación y asociaciones simuladas, contadores y renovación. DHCP, DNS, HTTPS, SIP/RTP y operaciones idempotentes se comprueban desde el PC. El motor simula sus estados y dependencias; no ejecuta firmware ni intercambios de paquetes de un sistema operativo de red.

## 6. Resultado académico

Se entrega un prototipo operativo con fuentes versionadas y pruebas automatizadas. La validación acredita el comportamiento del modelo y su interfaz; tiempos físicos, rendimiento inspeccionado, conservación de llamadas/sesiones y cumplimiento normativo no se inventan a partir de una animación. La homologación física no forma parte de los entregables pendientes del caso ficticio.

Revisión WAN-3 del 25/10: [cuatro accesos en central y continuidad extremo a extremo](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Continuidad_Cuatro_WAN_25_oct_2026.md).

## 7. Cierre operativo del 28 de octubre

La presentación web tiene 13 escenas: la escena 12 conserva crecimiento y QoS, y la 13 añade «Para finalizar», conclusión y preguntas. Las consolas permiten modificar interfaces, procesos OSPF, validación VPN, reglas y servicios; los resultados afectan el acceso a la aplicación. Las configuraciones guardadas incluyen protocolos y permanecen aisladas por alternativa.

La recuperación usa eventos con reloj virtual. Para el caso base, el fallo en t=157 s conserva la copia de t=120 s completada en t=124 s: 12 de 15 operaciones están presentes y 3 requieren conciliación. El RTO observado es 50 s y el RPO observado 30 s de tiempo virtual. Cambiar el instante del fallo o el intervalo de réplica cambia los registros recuperables.

La [matriz de protocolos y comandos](../Anexos/Matriz_Protocolos_Comandos.md) y el [guion de 13 escenas](../Video/Guion_13_Escenas.md) fijan el recorrido de defensa de esta versión.
