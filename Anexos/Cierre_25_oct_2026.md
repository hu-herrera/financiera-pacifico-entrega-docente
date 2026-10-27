# Cierre del diseño y evidencia para la grabación

25 de octubre de 2026. Complemento vigente de los entregables 6 y 7 y del PowerPoint de avance. Los PDF mantienen sus cortes fechados; este anexo registra la evidencia y decisión posterior. No cambia inventario, enlaces ni presupuesto WAN-2.

## Capacidad resuelta como política del diseño

Hasta 30 terminales remotos y tres en Casa Matriz con cámara simultánea. El cálculo conserva tráfico general/voz, full tunnel, una reserva del 10 % y utilización máxima del 70 %. Exige 759,142 Mbps de bajada y 965,627 de subida central, frente al principal supuesto de 1.000 por sentido. Se cuentan terminales, no reuniones. Se mantiene además el máximo de dos terminales por sucursal continental y uno por sede pequeña del perfil C5. Los 42 remotos del pico anterior exigían 1.088,199 de subida y no se admiten simultáneamente.

El coordinador limita participantes con cámara y utiliza audio para el excedente. En contingencia se suspende el video y se pausan copias/actualizaciones. La réplica crítica utiliza capacidad restante; una réplica postergada aumenta el riesgo de pérdida de datos. Se recalcula antes de seis aperturas o crecimiento. Es una política propuesta y un cálculo de diseño, sin admisión automática en una aplicación real.

## Evidencia de software

| Comprobación | Resultado y corte |
|---|---|
| Node completo | 93 aprobadas el 25/10 mediante `node --test tests/*.test.cjs` |
| Navegador completo | 151 aprobadas, commit privado 377af3c, CI 40140351278 |
| Admisión de video | Tres casos dentro de las 93: perfil elegido, frontera de capacidad y rechazo en contingencia |
| QoS | Clasificación autorizada, rechazo de DSCP falsificado y reparto bajo congestión |
| VPN | Coherencia de identidades y extremos propuestos, sin credenciales operativas |
| HA | Ocho escenarios aislados con condiciones de quórum, fencing y réplica |

Los conteos tienen alcances y fechas distintos. No se suman las pasadas como casos únicos ni se deduce uptime de un porcentaje de pruebas aprobadas. El código y los logs completos permanecen en el repositorio privado. La aplicación pública conserva solo sus archivos de funcionamiento.

## Alcance y cierre

RTO/RPO y disponibilidad son objetivos del diseño académico. Los resultados del prototipo son simulados. Certificados operativos, homologación de equipos y mediciones físicas quedan fuera de esta entrega y no son pendientes para grabar.

Para el hito del 30 de octubre se contempla la presentación audiovisual de los avances y resultados obtenidos. Las actividades técnicas concluidas se distinguen de las tareas de exposición y de las verificaciones físicas que quedan fuera del alcance del prototipo.

[Simulador vigente](https://hu-herrera.github.io/fina/).

[Revisión WAN-3 vigente: cuatro accesos en central y costos conciliados](Continuidad_Cuatro_WAN_25_oct_2026.md).
