# Matriz operativa de protocolos y comandos

Financiera Pacífico · C5-OPERACION-2 · 28 de octubre de 2026

Esta matriz delimita la versión para la defensa. Las consultas muestran estados del modelo; los cambios modifican el camino y los servicios. El motor es una simulación funcional de estados y dependencias, sin ejecutar firmware ni intercambios de paquetes IKE, OSPF o SIP en una red externa.

## 1. Acceso a las consolas

Seleccionar sede, abrir su topología y pulsar un equipo. La pestaña CLI acepta `help`. Desde PC 001 también se puede abrir la consola local: `console r1`, `console r2`, `console sw1` o `console sw2`; en central, `console fwa` y `console fwb`.

Las consultas compatibles con IOS, PAN-OS y RouterOS se normalizan sobre el mismo modelo. Los controles `sim` pertenecen al simulador. No son configuración nativa de fabricante. Los comandos no implementados se rechazan.

## 2. Matriz de operación

| Función | Consultas o acciones | Efecto comprobable |
|---|---|---|
| Interfaces | `show interfaces`, `show ip interface brief`; `configure terminal`, `interface <nombre>`, `shutdown`, `no shutdown`, `end` | Retira/restaura el enlace y afecta vecinos y rutas; el otro extremo observa el enlace caído |
| OSPF | `show ip ospf neighbor`, `show ip protocols`, `show ip route`; `router ospf 1`, `shutdown`; `sim ospf area 9` | Área incompatible o proceso apagado retira adyacencias y rutas; puede utilizar R2 |
| Reconvergencia | `clear ip ospf process`, `sim advance 4` | Mantiene adyacencias retiradas durante 4 segundos virtuales |
| IKEv2/IPsec | `show crypto ikev2 sa`, `show crypto ipsec sa` | Asociaciones simuladas, identidades, SPI, vida restante y contadores de transmisiones autorizadas |
| Autenticación VPN | `sim vpn identity equivocada.test`, `sim vpn identity auto`; `sim vpn certificate invalid/valid`; `sim vpn trust invalid/valid` | Un borde no autenticable queda fuera del camino; sin otro borde utilizable se bloquea el servicio |
| Propuesta ESP | `sim vpn esp down/up` | Una propuesta incompatible impide utilizar ese borde |
| Renovación VPN | `clear crypto sa`, `sim advance 3`; avanzar 3600 s para renovación | Retira asociaciones; renueva SPI y registra eventos al renegociar |
| VLAN | `show vlan brief`; `interface Vlan10`, `shutdown`, `no shutdown` | El estado de la SVI afecta el acceso del segmento; no modifica la autorización de las ACL |
| Vecindad L2/L3 | `show mac address-table`, `show arp` | Inventario de puestos activos y vecinos directamente conectados del equipo; no presenta PCs detrás de un router como vecinos ARP directos |
| StackWise / RSTP / LACP | `show switch`, `show spanning-tree`, `show etherchannel summary`; `sim lacp down/up` | Muestra miembros, partición y agregados; perder todos los caminos del agregado impide reenviar por él |
| VRRP de B | `show vrrp brief`; `sim vrrp priority <0..254>` | La elección del gateway considera prioridad y disponibilidad del camino; se refleja en el recorrido |
| Seguimiento WAN | `show track`, `show ip sla statistics` | Distingue transporte disponible de overlay seleccionado; no inventa RTT de una sonda física |
| ACL | `show access-lists`; `sim acl ALLOW-USERS-APP down/up` | Deshabilitar el permiso HTTPS bloquea la aplicación; no elimina la denegación por defecto |
| NAT central | `show ip nat translations` | Los flujos autorizados hacia Internet crean traducciones de dirección/puerto; el tráfico privado no se traduce |
| Sesiones y registros | `show session all`, `show logging`, `show clock` | Identificador, resultado, regla, bytes contabilizados y eventos de la ejecución |
| QoS | Explorador de congestión; `show policy-map interface` | Clasifica flujos autorizados y muestra el reparto calculado en el último ejercicio |
| Guardado | `write memory`, `show startup-config`, `show running-config` | Guarda interfaces y configuración de protocolos por alternativa; distingue cambios sin guardar |

## 3. Servicios desde el puesto

| Comando | Prueba |
|---|---|
| `ipconfig /release` y `ipconfig /renew` | Libera la dirección y ejecuta el ciclo DHCP del modelo para recuperarla |
| `nslookup app.financiera.test` | Consulta el DNS corporativo; falla si el nombre no existe o el servicio no responde |
| `curl https://app.financiera.test` | Comprueba DNS, camino, permiso HTTPS y aplicación/BD; usar la IP permite separar DNS de conectividad |
| `sip register` y `sip call` | Requiere PBX, registro y permisos de señalización/RTP; representa una llamada, sin transportar audio |
| `sim transaction prueba-001` | Confirma una operación en la aplicación simulada; repetir el ID no duplica el registro |
| `sim service dns down/up` en central | Impide/restaura resolución; el acceso por IP sigue siendo una comprobación independiente |
| `sim service database down/up` en central | La aplicación deja de confirmar operaciones aunque exista un camino de red |
| `sim service aaa down/up` en central | Afecta la autenticación del acceso Wi-Fi |

Equivalencias de consulta: PAN-OS `show vpn ike-sa` / `show vpn ipsec-sa`; RouterOS `/routing ospf neighbor print`, `/ip ipsec active-peers print`, `/ip ipsec installed-sa print`, `/ip route print` y `/interface vrrp print`.

## 4. Recuperación y tiempo virtual

El reloj avanza con `sim advance <segundos>` o con el botón del explorador. Es independiente del ritmo de la animación y de la duración del video.

En el ejercicio base se genera una operación cada 10 s, se inicia una réplica cada 60 s y esta tarda 4 s en completarse. El fallo ocurre en t=157 s. La copia de t=120 s terminó en t=124 s y contiene 12 de las 15 operaciones. Las tres posteriores requieren conciliación. El RPO observado es 150−120=30 s. El RTO observado es la suma de detección, aislamiento, arranque y comprobación HTTPS: 5+5+30+10=50 s virtuales.

Estos tiempos proceden de los eventos y parámetros del modelo. No son mediciones de servidores. Ante falta de mayoría, aislamiento, copia válida o aplicación, la recuperación se bloquea y su RTO queda sin resultado exitoso. Los objetivos del diseño permanecen en RTO 300 s y RPO 60 s.

## 5. Reproducción

Con ambos repositorios descargados como directorios hermanos `fina` y `entrega`:

```bash
node --test entrega/Verificacion/modelo.test.cjs entrega/Verificacion/protocolos.test.cjs
```

La configuración Playwright de la entrega ejecuta los escenarios de interfaz y las pruebas de operación. El anexo de cierre registra el SHA y los resultados de la pasada vigente.

Referencias de sintaxis: [Cisco OSPF](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/command/iro-cr-book/ospf-s1.html), [PAN-OS VPN](https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/troubleshooting/test-vpn-connectivity), [RouterOS OSPF](https://help.mikrotik.com/docs/spaces/ROS/pages/331612216/routing+ospf), [RouterOS IPsec](https://help.mikrotik.com/docs/spaces/ROS/pages/11993097/IPsec).
