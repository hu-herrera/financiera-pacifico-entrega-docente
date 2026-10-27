# Entregable 6 — Pruebas y criterios de aceptación

**Financiera Pacífico · edición C5 A/B, revisión WAN-3 · cierre documental 27 de octubre de 2026**

## Registro histórico del 25 de octubre

93 pruebas Node aprobadas en `node --test tests/*.test.cjs` (registro del 25/10). La pasada completa de navegador del commit 377af3c aprobó 151 casos. Se conservan sus alcances por separado. QoS verifica clasificación autorizada y reparto bajo congestión; VPN verifica identidades y coherencia de extremos; HA verifica ocho escenarios aislados y bloqueos por quórum/fencing/réplica. No hay certificación física atribuida al software.

[Detalle de afinamiento](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md) · [Política y cálculo de video](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Admision_Video_C5.md) · [CI del navegador](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md).

La regresión nueva comprueba 30 terminales remotos + 3 centrales, la frontera 33/34 remotos y rechazo de video en contingencia. El cálculo no aplica admisión en una plataforma real. Las cifras que siguen conservan la trazabilidad de las pasadas anteriores, sin sumarlas como casos distintos.

## 1. Evidencia registrada del corte anterior

La validación académica se realiza sobre el modelo y la aplicación web. El código de red validado corresponde al commit [`228ec2674d2b784b4cb67dab1128e969f681d3aa`](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md); el cierre documental posterior es [`62e832d`](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md).

| Comprobación | Resultado registrado | Interpretación |
|---|---|---|
| Pruebas de lógica Node | 78 aprobadas | Reglas, cálculos y consistencia del modelo |
| Pasada general de navegador | 144 aprobadas | Interfaz y escenarios de regresión |
| Pasada final C5/presentación | 31 aprobadas | Últimos ajustes de dispositivos, A/B y presentación |
| Caminos adicionales A/B | 1.351 comprobaciones | Fallas de enlaces/equipos y combinaciones seleccionadas |
| Archivos generados | 21 comprobaciones aprobadas | Fuentes y salidas sincronizadas |
| GitHub Actions del commit de red | Simulador, LAN/LACP y Pages aprobados | Validación automatizada y despliegue |

Las 31 pruebas finales vuelven a comprobar parte del alcance de la pasada general; no se suman a 144 como casos distintos. Las 1.351 comprobaciones de caminos tampoco se presentan como 1.351 pruebas de navegador. Ver [detalle de revisión](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md) y [ejecuciones CI](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md).

## 2. Matriz de aceptación funcional

| ID | Escenario | Resultado que se verifica |
|---|---|---|
| T01 | ANTES sin fallas | Puestos y servicios alcanzables según política |
| T02 | ANTES: pérdida de MPLS remoto | La sucursal pierde el único camino; no aparece respaldo ficticio |
| T03 | DESPUÉS: pérdida de un transporte | Existe otro camino elegible, con su degradación correspondiente |
| T04 | Pérdida de un distribuidor WAN | Se pierden sus dos transportes; el otro dominio sigue disponible |
| T05 | Pérdida de un router | Uso del otro router si sus enlaces y servicios están disponibles |
| T06 | Pérdida de un switch | Puestos de ese switch pierden cable; Wi-Fi requiere AP/AAA disponibles |
| T07 | ACL y aislamiento | APP permitida, BD restringida, invitados aislados y gestión desde NOC |
| T08 | Firewall central activo caído | Relevo por el miembro elegible y caminos coherentes |
| T09 | Sincronización OPNsense caída | Alarma de sincronización separada del servicio CARP |
| T10 | Host DC-01/DC-02 caído | VMs críticas recuperables con quórum, réplica y aislamiento |
| T11 | Dos hosts o quórum insuficiente | No se inventa recuperación de servicios |
| T12 | CM completa caída | Dependencias centrales e Internet full tunnel indisponibles |
| T13 | Puertos/IP por variante | No hay extremos duplicados, máscaras erróneas ni enlaces heredados de A en B |
| T14 | Configuración/presentación | Estado guardado aislado por sede/variante; escenas limpias y restauración al salir |
| T15 | Presupuesto e inventario | Totales y cantidades A/B coinciden entre JSON, presentación y anexos |

## 3. Reproducibilidad

Los siguientes comandos pertenecen al repositorio de desarrollo privado. Se conservan como trazabilidad de las pasadas históricas; no se ejecutan desde el repositorio público `fina`, que contiene solamente los archivos de funcionamiento:

```bash
node --test tests/*.test.cjs
node network/c5-design.cjs --check
node network/c5-budget.cjs --check
node network/build-c5-browser.cjs --check
node scripts/build-c5-security.cjs --check
node scripts/build-client-presentation.cjs --check
npx playwright test tests/c5-simulator.spec.cjs tests/c5-device-views.spec.cjs tests/client-presentation.spec.cjs --browser chromium
```

La configuración del proyecto y los workflows conservan las versiones/condiciones de ejecución. Antes de repetir se limpia el escenario y se registra variante, sede, origen/destino, falla, regla ACL, camino esperado y resultado observado. [Tests](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md) · [workflows](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md).

## 4. Objetivos y límites de medición

| Variable | Tratamiento de esta entrega |
|---|---|
| Disponibilidad 99,99/99,95 % | Meta anual de diseño; no se deriva del porcentaje de conectividad del mapa |
| RTO sucursal≤300 s | Objetivo del caso; se demuestra elegibilidad del camino, sin cronometrar convergencia física |
| RPO hosts 60 s / recuperación 300 s | Objetivos de réplica/reinicio, condicionados por capacidad y quórum |
| Mbps, jitter, latencia y pérdida | Hipótesis/perfiles del modelo; no mediciones de un operador |
| Conservación de llamadas/sesiones | No certificada por un ping exitoso posterior |
| Seguridad | Reglas y caminos comprobados; no auditoría de cumplimiento normativo |
| Homologación física | Fuera de los entregables académicos de este caso ficticio |

Las pasadas anteriores están registradas como resultados declarados. El anexo de evidencia distingue qué ejecuciones pueden comprobarse públicamente y qué logs permanecen fuera de la entrega pública. Los ensayos de hardware de protocolos históricos corresponden a una implementación real hipotética, no a un segundo prototipo exigido para entregar hoy.

## 5. Hallazgos cerrados en la revisión final

Se corrigieron modelos visibles en WAN-A/B, distribuidores MikroTik de B, mapa de interfaces DEC3852, comportamiento al perder pfsync, LACP de 10G y 44 DAC, IP/VIP de interfaces, máscara BKP/24, indicador superior, estado/modelo de AP y caché de presentación. También se comprobaron IPAM, ACL, retorno, fallas dobles y HA de hosts. Las cifras económicas se conservan conciliadas con E7.



## 6. Indicadores y registro de evaluación

| Indicador | Objetivo / método | Evidencia disponible |
|---|---|---|
| Disponibilidad | Core 99,99 %; sucursal 99,95 % anual | Objetivo de ficha; el mapa solo calcula conectividad de un escenario |
| Conmutación de sucursal | ≤300 s ante falla recuperable y respaldo elegible | Cambio de camino del modelo; sin cronometraje físico |
| Retorno al principal | Estabilidad antes de volver; evitar oscilaciones | Espera didáctica 5 s del escenario E7, no 5 min reales |
| RTT | Registrar por transporte, origen/destino y estado | Valor/perfil del modelo; sin RTT observado de producción |
| Pérdida | Paquetes perdidos/enviados y ventana explícita | Fallas y degradación modeladas; sin historial de operador |
| Jitter | Variación de retardo por flujo de voz | Parámetro a evaluar con tráfico de voz; no medición real |
| Utilización | Demanda/caudal útil por sentido, referencia 70 % | Dimensionamiento calculado; picos de video superan el principal CM |
| Calidad VoIP | Éxito de registro/señalización y calidad con codec definido | Dependencia/permiso PBX comprobados; no MOS ni llamada real inventados |
| Recuperación de VM | Objetivo 300 s; RPO 60 s y datos utilizables | Elegibilidad y bloqueos por réplica/quórum/fencing |
| Incidentes | Contar eventos por sede/tipo y restablecimiento | Eventos de prueba; no se deduce tasa de incidentes de la empresa |

No se asigna un RTT/jitter/MOS medido a un ensayo que solo evalúa caminos. Para repetir una prueba se registra estado inicial, acción, resultado esperado/observado, registro y corte de software. Los resultados simulados se separan de los objetivos del diseño.

## 7. Regresión de la revisión WAN-2 (24-10-2026)

Se ejecutan 79 pruebas de lógica sobre la revisión que sustituye también los distribuidores de A por MikroTik. Se añade una comprobación de todos los puertos WAN A/B, VLAN de gestión separada y continuidad al perder cada distribuidor. Los resultados de navegador de esta revisión y los comandos constan en docs/revision-wan-distribuidores-2026-10-24.md. Estas pasadas vuelven a verificar el prototipo y no se suman a los registros históricos como casos únicos.

## Presentación dinámica del 25 de octubre

[Detalle y evidencia](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md): 15 pruebas de presentación y 27 del simulador/dispositivos aprobadas localmente. Los ejemplos ahora preparan estado inicial, aplican fallos y evalúan el resultado mediante el mismo motor. La secuencia puede pausarse y repetirse. Seguridad, recuperación y reparto QoS tienen historias visuales propias. Los 42 casos corresponden a esta pasada seleccionada; no se suman como nuevos casos a las 151 pruebas de navegador del corte anterior.

Revisión WAN-3 del 25/10: [cuatro accesos en central y continuidad extremo a extremo](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Continuidad_Cuatro_WAN_25_oct_2026.md).


## 8. Verificación pública del cierre del 27 de octubre

El anexo [Evidencia de pruebas](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/blob/main/Anexos/Evidencia_Pruebas_27_oct_2026.md) identifica SHA, comandos, alcance y resultado. La carpeta [Verificacion](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/tree/main/Verificacion) permite ejecutar las comprobaciones públicas de modelo, documentos e interfaz contra un corte explícito de `fina`. Los logs nuevos se consultan en [GitHub Actions](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/actions/workflows/verificacion-publica.yml). Estas comprobaciones no se suman a las pasadas históricas ni acreditan los 71/161 mencionados en el mensaje de 5779eeb.
