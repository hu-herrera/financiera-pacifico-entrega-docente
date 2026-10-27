# Entregable 2 — Evaluación de alternativas y decisión técnica

**Financiera Pacífico · edición C5 A/B, revisión WAN-3 · cierre documental 27 de octubre de 2026**

## 1. Criterios de decisión

Las opciones se comparan para las mismas 23 sedes y los mismos 650 puestos. Se evalúan continuidad, seguridad, cobertura supuesta, costo a cinco años, escalabilidad y operación. Los pesos heredados del análisis son 25 %, 20 %, 20 %, 15 %, 10 % y 10 %, respectivamente; son prioridades del diseño, no resultados de laboratorio.

## 2. Alternativas de transporte

| Arquitectura | Evaluación | Tratamiento |
|---|---|---|
| MPLS reforzado | Permite conservar la infraestructura, pero exige otro acceso y mantiene dependencia terrestre | Alternativa estudiada |
| MPLS + Internet/móvil | Facilita migración y reversión | Uso transitorio durante el despliegue propuesto |
| Multitransporte sin MPLS | Diversifica caminos con VPN hacia CM | Arquitectura objetivo adoptada |

En DESPUÉS hay cero MPLS y cero OneWeb. Todas las sedes, incluida CM, utilizan Starlink, Amazon Leo, Entel 5G y WOM 4G. Son **92 servicios WAN**: 23×4. La revisión WAN-3 corrige el corte anterior que limitaba central a dos satelitales. GTD permanece fuera de la selección vigente.

Leo, los caudales simétricos agregados, cobertura extrema, comodatos y descuentos se aceptan como premisas del caso ficticio. No se presentan como ofertas obtenidas. Cuatro marcas no demuestran cuatro infraestructuras físicamente independientes. La agregación de gateways Starlink la suministra el operador dentro del supuesto comercial; no se atribuye esa capacidad a una antena doméstica individual.

## 3. Dos opciones de equipamiento

| Función | A · Cisco/Palo Alto | B · MikroTik/OPNsense |
|---|---|---|
| Routers remotos | 44 C1121X-8P instalados; siete reutilizados y 37 nuevos | 42 CCR2004-16G-2S+ nuevos y dos RB5009UG+S+IN nuevos en S22 |
| Switches remotos | 44 C9200L, 17 reutilizados y 27 nuevos | 44 CRS328-24P-4S+RM nuevos |
| Switches centrales | Dos C9200L-48P-4X-E existentes | Se reutilizan los mismos dos C9200L centrales |
| Firewalls centrales | Dos PA-1410 activo/pasivo | Dos DEC3852 con OPNsense, CARP/pfsync/XMLRPC |
| Distribución WAN GbE | 45 MikroTik hEX E50UG en bridge VLAN | 45 MikroTik hEX E50UG en bridge VLAN |
| Distribución WAN-A central 2,5G | Un CRS310-8G+2S+IN | Un CRS310-8G+2S+IN |
| Unión switches remotos | StackWise con kits y cables presupuestados | Dos enlaces LACP de 10G por pareja, 44 DAC XS+DA0001; RSTP/VRRP según función |
| Inspección de Internet | Centralizada | Centralizada |
| NGFW en sucursal | Cero | Cero |
| Servicios y servidores | Hosts existentes con HA de VMs | Mismo alcance de HA |

WAN-A y WAN-B identifican el grupo de transportes, no un modelo de equipo. En ambas alternativas los distribuidores son MikroTik, sin C1300 en esa función. Los hEX operan como distribución L2, sin NAT, DHCP ni terminación IPsec. No se presupone que B elimine todos los equipos Cisco existentes: mantiene el switching central y los AP del diseño.

## 4. Licencias y soporte

A incluye SEC y VPERF en los 37 routers nuevos, suscripción inicial de switching donde corresponde y ATP/soporte de 60 meses en los dos PA-1410. IP Base y Network Essentials incluidos no se cobran otra vez. SEC sola no justifica el caudal cifrado del paquete VPERF. Los derechos existentes de los siete routers reutilizados son un supuesto del inventario.

B no incorpora suscripciones obligatorias recurrentes de router, switch o firewall en el modelo económico. La reserva de operación sigue existiendo: ausencia de suscripción no implica mantenimiento gratuito ni equivalencia automática de soporte, rendimiento o inspección entre fabricantes.

## 5. Comparación económica

| CLP con IVA supuesto | A | B |
| --- | --- | --- |
| Inversión inicial | 793.126.897 | 281.194.478 |
| WAN mensual | 11.010.123 | 11.010.123 |
| Costo del alcance a 60 meses | 1.503.734.277 | 966.801.858 |

B reduce el desembolso inicial estimado en CLP 511.932.419 frente a A y el costo del alcance a 60 meses en CLP 536.932.419. Es una comparación de alternativas con el mismo supuesto WAN; no demuestra ahorro contractual ni ROI frente al ANTES. E7 contiene las partidas y exclusiones.

## 6. Revisión de ciclo de vida y justificación de selección

Consulta documental: 23-10-2026. Se excluyen de nuevas compras ISR 4451 y Catalyst 3850 del ejemplo inicial. No se confunde un anuncio de retiro de una familia/SKU con todos los productos que comparten «ISR1100» en el nombre.

| Equipo | Resultado de la revisión | Decisión del diseño |
|---|---|---|
| C1121X-8P | El aviso Cisco ISR1100/ISR1100X consultado lo identifica como producto de migración, no como SKU retirado de esa tabla | Mantener la comparación A con SEC/VPERF y derechos por nodo; no inventar fecha de soporte hasta 2031 |
| C9200L | El listado oficial consultado contiene avisos de versiones y licencias; estos no equivalen a retirar todo el hardware C9200L | Reutilizar 17 remotos y dos centrales; adquirir 27 remotos del modelo previsto |
| PA-1410 | PA-1400 aparece como reemplazo del PA-800 en el listado de ciclo de vida consultado | Mantener dos centrales con ATP/soporte 60 meses presupuestados |
| MikroTik CCR2004/RB5009/CRS328/hEX/CRS310 | Modelos con fichas oficiales usadas para puertos y funciones | Mantener B como opción con funciones incluidas; no equiparar su soporte a SmartNet/soporte premium |
| DEC3852 | Ficha oficial de appliance con puertos asignados al diseño y OPNsense | Mantener par CARP/pfsync; no atribuirle sintaxis ni HSCI de Palo Alto |

La ausencia de un aviso de fin de venta no es una garantía de soporte durante todo el horizonte. La selección académica queda fundamentada por función, precio y reutilización; una adquisición hipotética exigiría derechos de actualización/reemplazo y versión de software adecuados al período. No se deja una homologación física como tarea pendiente de la entrega.

Fuentes de esta revisión: Cisco ISR1000 (ficha y avisos por SKU), Cisco Catalyst 9200 (listado de fin de vida), Palo Alto (Hardware End-of-Life Dates), fichas MikroTik y Deciso/OPNsense. Las URL completas y fuentes de precios se incluyen en el anexo «Fuentes técnicas y precios».

## 7. Decisión presentada

Se entregan ambas alternativas con el mismo alcance y fallas. B presenta el menor costo estimado; A conserva mayor continuidad con Cisco. La selección presupuestaria mantiene los objetivos de seguridad y disponibilidad del diseño. Las pruebas del navegador acreditan el modelo, sin medir rendimiento físico.

Revisión WAN-3 del 25/10: [cuatro accesos en central y continuidad extremo a extremo](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Continuidad_Cuatro_WAN_25_oct_2026.md).
