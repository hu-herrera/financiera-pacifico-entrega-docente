# Caso 6 - Financiera Pacífico

**Fuente:** Capstone_Ingenieria_Conectividad_Redes.xlsx. Transcripción de la fila 7 de las hojas indicadas. El archivo original se conserva sin modificar junto a este documento.

## 1. Antecedentes oficiales

| Campo | Ficha oficial |
|---|---|
| Empresa / industria | Financiera Pacífico / servicios financieros |
| Trabajadores | 780 |
| Sedes | 22: Casa Matriz, datacenter y 21 sucursales |
| Usuarios TI aproximados | 650 |
| Servicios críticos | Core financiero, sucursales y VoIP |
| Problema principal | Continuidad y seguridad entre sucursales |
| Presupuesto de referencia | CLP 160.000.000 |
| Horizonte | Cinco años |

## 2. Situación y requisitos

La hoja «Fichas de Casos» describe doble ISP en Casa Matriz, MPLS único en sucursales, OSPF y red 10.70.0.0/16. Los problemas conocidos son sucursales sin contingencia y cambios manuales. Se exige RTO de sucursal de hasta cinco minutos, cifrado y auditoría. El crecimiento esperado es de seis sucursales nuevas.

Los eventos del caso son una caída nacional de MPLS de tres horas y una auditoría que exige trazabilidad de cambios. El objetivo del cliente es modernizar la WAN con seguridad y continuidad.

La hoja «Datos Técnicos» incorpora switching L3 corporativo, firewall/VPN, NMS central, objetivos de disponibilidad 99,99 % core y 99,95 % sucursal, y métricas mínimas de convergencia, RTT, pérdida y disponibilidad.

## 3. Alcance de estos antecedentes

La ficha no especifica modelos ni cantidades por SKU, anchos de banda por sede, edades de equipos, precios unitarios ni métricas observadas. Tampoco acredita incumplimiento normativo ni que los equipos anteriores carezcan de VLAN, QoS o VPN.

## 4. Adaptación explícita del proyecto

El diseño académico adopta 23 sedes: Casa Matriz y 22 sucursales, incluyendo Hanga Roa y Base Frei. Mantiene 650 puestos informáticos y supone un teléfono por puesto. Los 650 usuarios TI aproximados de la ficha no se citan como si fueran un inventario físico oficial de 650 computadores.

Los dos MPLS centrales de 1 Gbps, dos ISP de 500 Mbps y un MPLS de 100 Mbps por sucursal son supuestos adoptados del ANTES. Los modelos, direcciones de detalle y capacidades son definiciones técnicas del equipo, documentadas en el informe y los entregables. Las seis aperturas futuras permanecen separadas del inventario actual.

## 5. Ajuste presupuestario autorizado como criterio docente

La retroalimentación de la primera entrega señala que CLP 160.000.000 es una referencia inicial y permite fundamentar una solución superior. Esto habilita la evaluación académica de las alternativas; no representa aprobación de compra de una organización real.
