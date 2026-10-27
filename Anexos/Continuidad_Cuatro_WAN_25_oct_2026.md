# Continuidad extremo a extremo: cuatro WAN también en central

25-10-2026. Revisión técnica WAN-3 y económica C5-ECO-3-CM-CUATRO-WAN.

## Problema y objetivo

El diseño anterior tenía cuatro transportes en cada sucursal y solo Starlink/Leo en Casa Matriz. Al caer ambos satelitales, los móviles remotos no alcanzaban central. Esto dejaba sin cumplir el objetivo de continuidad ante fallos parciales de proveedores, incluso cuando permanecía algún acceso operativo. El escenario E6 describía correctamente esa limitación, pero el diseño necesitaba corregirse.

Casa Matriz y las 22 sucursales ahora tienen Starlink, Leo, Entel 5G y WOM 4G. Una nueva comunicación conserva camino si queda un acceso utilizable en cada extremo, con sus equipos, políticas, VPN y servicios disponibles. Los proveedores de ambos extremos pueden ser distintos. Se comprueban también fallos de CPE, distribuidor y puertos; no se cuenta una interfaz de gestión como camino de datos.

## Plano físico y túneles

Se conservan los dos distribuidores centrales. WAN-A lleva Starlink/Entel en VLAN201/203; WAN-B lleva Leo/WOM en VLAN202/204. En ambos: ether1/2 para CPE, ether3/4 para firewalls y ether5 para gestión. No se mezcla VLAN130 con los trunks de proveedores.

A usa ethernet1/9 y ethernet1/1 con subinterfaces L3 etiquetadas. B usa RJ45-0/1 con VLAN y una IP por miembro más CARP VIP por servicio. Conserva RJ45-2 para gestión, RJ45-3 para sincronización y SFP+-X0/X1 para LAN. No se inventan puertos adicionales en DEC3852. Se mantienen dos dominios de distribución, un hEX central y un CRS310.

Cada router remoto considera cuatro WAN y cuatro extremos centrales: 16 candidatos por router, 32 por sucursal y 704 totales. Direcciones /30 reservadas en 10.253.N.0/25. El controlador comprueba que exista el candidato hacia el proveedor central seleccionado y que su extremo coincida. No se exige que ambos lados usen el mismo operador.

Las IP RFC5737 y la entrega alcanzable del servicio móvil central son supuestos del caso ficticio. El contrato académico requiere IP pública/entrega ruteada o mapeo compatible de UDP500/4500 al hub. CGNAT entrante sin ese mecanismo no satisface el diseño. No se afirma haber obtenido APN, dirección o tarifa corporativa reales. Las mensualidades se conservan como valores de planificación del escenario, sujetas a ese supuesto de alcance.

## Presupuesto conciliado

Se agregan un NX500 y un MR600 centrales a los mismos unitarios adoptados: 342.850 + 158.790 = 501.640 CLP; con contingencia del 15 %, el inicial aumenta 576.886 en ambas opciones. No se agregan distribuidores ni firewalls. Los CPE móviles pasan de 44 a 46, y los servicios de 90 a 92.

| Concepto CLP con IVA supuesto | A | B |
|---|---:|---:|
| Inicial | 793.126.897 | 281.194.478 |
| WAN mensual | 11.010.123 | 11.010.123 |
| WAN 60 meses | 660.607.380 | 660.607.380 |
| Alcance 60 meses | 1.503.734.277 | 966.801.858 |

La mensualidad agrega (15.900 + 15.990) × 0,9 = 28.701 CLP; a 60 meses, 1.722.060. Cambio total a 60 meses: 2.298.946 por alternativa. La revisión ECO-2 se conserva como antecedente, con su huella económica. No se cambia un costo silenciosamente.

## Conectividad y capacidad son comprobaciones distintas

La meta es máxima continuidad posible, sin aislamiento por la pérdida de un enlace o proveedor. Cuatro nombres de operadores no acreditan independencia de energía, torres, sitio o redes subyacentes, ni 100 % de disponibilidad anual.

Un camino móvil restante no demuestra capacidad suficiente para todos los usuarios simultáneos. Se suspenden video y cargas posponibles, se priorizan aplicación, voz y servicios, y se limita concurrencia a la capacidad disponible. La referencia WOM tiene subida máxima de 5 Mbps, muy inferior al perfil crítico agregado calculado de central: no se anuncia capacidad plena por ese último respaldo. Los supuestos de capacidad se mantienen explícitos en las fichas y QoS; no se suman enlaces para atribuir caudal a una sesión.

La disponibilidad de la aplicación requiere también hosts, réplica, mayoría, aislamiento y permisos. Los escenarios sin ningún acceso, sin peer coincidente o sin VLAN del proveedor deben fallar. RTO/RPO siguen como objetivos del diseño académico.

## Evidencia reproducible

- Suite Node completa, incluidas las seis pruebas nuevas de cuatro WAN.
- 4.950 combinaciones de subconjuntos no vacíos de WAN en ambos extremos por alternativa: 22 sucursales × 15 × 15; 9.900 comprobaciones en A/B. La evidencia de código se conserva en el repositorio privado.
- Navegador: pérdida individual de cada proveedor en las 23 sedes, 16 pares de últimos proveedores remota/central por alternativa, APP y voz, E6, WOM como único superviviente, cuatro enlaces caídos y ausencia de peer.
- El ejemplo WAN de la presentación muestra automáticamente Starlink, Leo, Entel, WOM y el agotamiento de los cuatro accesos. Cada etapa consulta el motor y la prueba HTTPS, con la misma política de permisos.

## Referencias de implementación

- PAN-OS: https://docs.paloaltonetworks.com/ngfw/help/10-1/network/network-interfaces/layer-3-subinterface
- OPNsense VLAN: https://docs.opnsense.org/manual/how-tos/vlan_and_lagg.html
- OPNsense CARP: https://docs.opnsense.org/manual/how-tos/carp.html

Estas referencias sustentan la separación por VLAN y el patrón de interfaces. No certifican la interoperabilidad o capacidad física del caso.

## Resultado de cierre

99 pruebas Node aprobadas. Pasada local de navegador C5/dispositivos/presentación: 44 casos aprobados. La matriz de 9.900 combinaciones está incluida en las pruebas Node, no son 9.900 pruebas de navegador. Excel recalculado y conciliado con ambos JSON. PowerPoint mantiene 14 láminas, tablas editables y nuevos importes. Los PDF numerados, IPAM y planos reflejan los cuatro accesos centrales.
