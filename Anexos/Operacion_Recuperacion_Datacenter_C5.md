# Operación y recuperación del datacenter C5

Financiera Pacífico · 28-10-2026 · Revisión C5-OPERACION-2

## 1. Qué entregamos y quién lo opera

El proyecto entrega diseño, parámetros de configuración, pruebas del modelo y procedimientos para preparar y recuperar los servicios centrales. La financiera asigna administradores, custodia credenciales y datos, ejecuta los cambios y mantiene la operación. Este anexo concreta la recuperación local del perfil C5 vigente en A y B. No despliega una aplicación bancaria, un motor de respaldo ni un clúster real.

Se conservan los dos hosts y BKP-01 existentes. No se compra otro datacenter ni se altera el presupuesto. La ampliación de DC-02 a 64 GiB y 3840 GB útiles ya estaba contemplada. Los estudios históricos C4/DC3 de tres hosts no sustituyen este perfil. Electricidad, climatización y autonomía son infraestructura existente bajo responsabilidad de la financiera; su disponibilidad es una dependencia del diseño de red.

| Equipo | Gestión | Función y condición |
|---|---|---|
| DC-01, Dell R740 | 10.80.0.11 | Preferido para aplicación y PostgreSQL; 64 GiB y 2000 GB útiles |
| DC-02, Dell R740 | 10.80.0.12 | Preferido para PBX, DNS/NTP, AAA y gestión; 64 GiB y 3840 GB útiles después de la ampliación prevista |
| BKP-01, Dell R540 | 10.70.200.50 | Repositorio de 8000 GB útiles y servicio qdevice/qnetd previsto; no ejecuta las VMs críticas |

Dos NIC por equipo: una hacia cada switch central; bond activo/reserva. Los hosts transportan servicios VLAN50 y gestión VLAN130. BKP-01 usa VLAN50. La gestión no constituye un acceso remoto independiente. BKP-01 combina respaldo y voto: su falla afecta ambas funciones. Dos hosts vivos conservan mayoría; perder un host y BKP-01 excede la recuperación automática planteada.

## 2. Perfil de preparación técnica

| Parámetro | Preparación que corresponde al integrador | Comprobación de operación |
|---|---|---|
| Hipervisor | Perfil Proxmox VE con almacenamiento ZFS local compatible y nombres DC-01/DC-02 | Versiones compatibles, espacio, salud de discos y capacidad disponible |
| Red | VLAN, bond activo/reserva, gateway, permisos de gestión y servicios según las fichas C5 | Pérdida de cada NIC/switch sin anunciar un servicio inaccesible como disponible |
| Mayoría | Dos votos de hosts y qdevice externo a esos hosts en BKP-01 | Estado esperado de 2/3 votos y comunicación con el testigo; no forzar votos durante una partición |
| Aislamiento | Configuración de HA y mecanismo de fencing/watchdog compatible | Evidencia de aislamiento del host anterior antes de reiniciar su VM en otro |
| Réplica | Tareas para las VMs y discos protegidos, destinos, calendario objetivo de 60 s y avisos de error | Último punto completado, duración, antigüedad y tareas fallidas; el calendario no garantiza el RPO |
| Recursos | 52 GiB para VMs críticas y 4 GiB de hipervisor en el host superviviente; pausar NMS según el perfil | CPU, RAM y espacio suficientes; capacidad de CPU/IO no medida en este prototipo |
| Copias | Catálogo de VMs, datos, configuración, claves y procedimientos recuperables por el equipo autorizado | Retención, integridad, espacio, restauración y custodia separados de la réplica |

Los 1600 GB replicados y el margen de 20 % caben aritméticamente en el host menor de 2000 GB. Esto no demuestra rendimiento ni espacio libre real. Los 8 TB del repositorio no acreditan cualquier retención o crecimiento de cinco años. La financiera conserva su política de copias y debe contrastar tamaño, cambios, retención y espacio de restauración con esa capacidad; este complemento no inventa una política financiada adicional.

Réplica de VM y respaldo tienen funciones distintas. La réplica permite reiniciar desde un punto reciente; también puede propagar corrupción o borrados. Una copia de seguridad conserva puntos anteriores bajo su política. Su verificación de integridad no reemplaza probar el arranque y la consistencia de aplicación/BD. No se da por instalado Proxmox Backup Server: su documentación se usa como referencia de verificación, sin cambiar la herramienta de backup existente de la financiera.

## 3. Ejecución de recuperación con tiempo virtual

El motor genera operaciones y tareas de réplica durante la ejecución. En el caso base inicia una operación cada 10 s y una réplica cada 60 s; cada réplica tarda 4 s en completarse. El host falla en t=157 s. La copia con datos hasta t=120 s se completó en t=124 s y contiene 12 de 15 operaciones. OP-0013, OP-0014 y OP-0015 requieren conciliación. Una tarea en curso o fallida no sustituye la última completada.

El RPO observado es 150-120=30 s. La recuperación simula detección 5 s, aislamiento 5 s, arranque de VM 30 s y comprobación HTTPS 10 s, para un RTO observado de 50 s virtuales. Estos resultados cambian con los parámetros y con las condiciones del escenario; no son tiempos obtenidos de firmware o servidores físicos.

Ante réplica antigua, falta de mayoría, aislamiento no confirmado, copia inconsistente, aplicación fallida o pérdida de ambos hosts, no se anuncia recuperación exitosa. La falta de integridad impide afirmar qué operaciones están conservadas. Los indicadores de integridad son estados del modelo, no resultados de una verificación ZFS/PostgreSQL externa.

La interfaz comprueba por separado red, permisos y aplicación. El explorador permite variar el instante del fallo y el intervalo de réplica. Los 14 escenarios A/B están publicados en el JSON de recuperación y se reproducen con `node --test entrega/Verificacion/modelo.test.cjs entrega/Verificacion/protocolos.test.cjs`.

## 4. Procedimiento ante pérdida de un host

1. **Registrar y clasificar.** Abrir incidente con hora de detección, sedes afectadas, último servicio correcto y síntomas. Redes distingue pérdida de WAN, permiso denegado, host caído y aplicación detenida. Conservar registros; un ping correcto no cierra el incidente.
2. **Revisar mayoría y aislamiento.** Sistemas comprueba el clúster y el testigo. Confirmar que el host anterior no puede ejecutar simultáneamente la misma carga. Sin mayoría o aislamiento, detener la promoción y escalar; no reducir votos ni arrancar a ciegas otra instancia.
3. **Identificar el punto de datos.** Registrar el último punto de réplica completado y la hora del fallo. Revisar trabajos fallidos o incompletos, integridad y consistencia de aplicación. Calcular antigüedad. Sobre 60 s, registrar desviación y solicitar decisión de Sistemas y del responsable de negocio antes de aceptar esa pérdida potencial.
4. **Comprobar el destino.** Verificar RAM, CPU, almacenamiento, redes y dependencias. Priorizar APP, BD, PBX, DNS/NTP y AAA; pausar NMS según el perfil de contingencia. Evitar un segundo mantenimiento mientras solo quede un host.
5. **Recuperar de forma controlada.** Si HA ya reinició las VMs, verificar su estado y no duplicar el arranque manual. En una recuperación manual autorizada, utilizar el punto identificado y conservar el original para análisis. Este documento no ejecuta comandos de arranque ni cambios sobre equipos de producción.
6. **Validar antes de reabrir.** Sistemas verifica recuperación de PostgreSQL, consistencia y aplicación; Redes prueba el flujo HTTPS autorizado desde una sucursal y conserva los bloqueos de BD e invitados. Telefonía comprueba llamada y audio. Probar con datos autorizados de ensayo, sin generar movimientos financieros reales desde la demostración.
7. **Conciliar y comunicar.** El responsable de aplicación identifica operaciones posteriores al punto recuperado y contrasta identificadores y estados con sus registros autorizados. Una solicitud sin respuesta puede haber sido procesada; no repetirla sin comprobar su estado. Registrar autorización de reapertura y comunicar limitaciones a las sedes.
8. **Reparar y retornar.** Reparar el host, comprobar almacenamiento y sincronizar datos desde la instancia vigente. El retorno se planifica y verifica; no devolver automáticamente la carga a un host con una copia antigua. Cerrar el incidente con causas, tiempos y medidas correctivas.

RTO objetivo: 300 s para la recuperación local planteada. RPO objetivo: 60 s. El tiempo se mide desde el evento de referencia acordado hasta una operación de aplicación válida, no hasta un ping. Los puntos recuperados se contrastan con los registros transaccionales. Los resultados reales quedan sin medir; no se promete pérdida cero, conservación de llamadas ni continuidad de sesiones.

## 5. Comprobaciones de solo lectura para el administrador

Ejecutar desde una sesión administrativa autorizada del hipervisor correspondiente y conservar la salida en el registro privado del incidente. La versión y los identificadores de VM se obtienen del inventario real al desplegar. No se almacenan credenciales ni salidas sensibles en el repositorio público.

```text
pvecm status
ha-manager status
pvesr status
qm list
pvesm status
zpool status
journalctl -u corosync --since "-15 minutes"
journalctl -u pve-ha-lrm -u pve-ha-crm --since "-15 minutes"
```

Interpretación: mayoría y miembros; estado de recursos HA; últimas tareas de réplica; inventario de VMs; capacidad de almacenamiento; salud ZFS; eventos de clúster y HA. Ninguna salida aislada prueba consistencia bancaria. Las comprobaciones PostgreSQL y el endpoint de salud de APP se definen con su administrador y la versión instalada; este anexo no inventa un endpoint ni credenciales productivas.

## 6. Copia dañada o pérdida de ambos hosts

Si la réplica es inconsistente, detener la recuperación automática de esa carga, preservar evidencia y seleccionar una copia anterior válida. El administrador restaura una VM o BD en una red aislada, sin IP o salida productiva duplicada. Comprobar integridad, arranque, consistencia y registros disponibles; documentar el punto de recuperación y la conciliación pendiente. Solo después se autoriza el cambio a servicio. El simulador muestra la decisión de bloqueo y este procedimiento; no afirma haber ejecutado esa restauración.

Si fallan ambos hosts no queda cómputo local para ejecutar los servicios. Una copia en BKP-01 no elimina esa dependencia. La pérdida del edificio requiere otro sitio operativo y un alcance presupuestado aparte; no se considera resuelta por este complemento. La respuesta institucional a incidentes, las comunicaciones regulatorias y las decisiones sobre datos pertenecen a los responsables de la financiera.

## 7. Entrega, responsabilidades y registro

| Actividad | Preparación del proyecto/integrador | Operación de la financiera |
|---|---|---|
| Red y seguridad | IPAM, VLAN, VPN, permisos, redundancia y pruebas | Mantener configuración, accesos y proveedores |
| Recuperación local | Perfil, dependencias, escenarios y procedimiento | Implantar en su plataforma, ensayar, mantener y ejecutar |
| Copias y datos | Inventario protegido y requisitos de recuperación | Herramienta, retención, custodias, pruebas y conciliación |
| Alertas | Criterios: host caído, error/antigüedad de réplica, pérdida de mayoría, espacio e integridad | Recepción, investigación y escalamiento con responsable/suplente |
| Reapertura | Lista de comprobaciones y evidencia requerida | Sistemas valida; negocio autoriza y comunica |
| Energía y climatización | Dependencias identificadas | Disponibilidad, autonomía y mantenimiento existentes |

Cada ejercicio o incidente registra: identificador, responsables, versión del perfil, fallo y hora, host destino, votos, aislamiento, último punto completado, antigüedad, resultados de APP/BD/voz, operaciones por conciliar, autorización, hora de reapertura y retorno. Conservar tanto resultados esperados como desviaciones. Una lista marcada no sustituye las salidas o evidencias que la respaldan.

Para la entrega académica se aportan el modelo, sus eventos y resultados reproducibles y el procedimiento. No se exige montar otro laboratorio ni presentar certificaciones físicas para considerar completo este complemento. La eventual implantación productiva requiere adaptar el perfil a la plataforma real y aceptar sus pruebas.

## Referencias y trazabilidad

- Perfil vigente: datos públicos `network/c5-data.js`, sección `datacenter_ha` y equipos existentes; fichas A/B C5.
- Resultados del ejercicio: [Ejercicios_Recuperacion_C5.json](Ejercicios_Recuperacion_C5.json); motor público `network/c5-protocols.js` y `network/c5-model.js`.
- Proxmox VE, réplica y pérdida potencial desde el último punto: https://github.com/proxmox/pve-docs/blob/master/pvesr.adoc
- Proxmox VE, gestión HA y aislamiento: https://github.com/proxmox/pve-docs/blob/master/ha-manager.adoc
- Proxmox VE, clúster y qdevice: https://github.com/proxmox/pve-docs/blob/master/pvecm.adoc
- Proxmox Backup, verificación y avisos como referencia de operación: https://pbs.proxmox.com/docs/maintenance.html

Fuentes consultadas el 26-10-2026. La sintaxis se adapta a la versión instalada antes de la implantación; ninguna referencia certifica el hardware ni la plataforma del caso.
