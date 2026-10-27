# Capacidad y admisión de video C5

25 de octubre de 2026. Decisión del diseño académico para las 23 sedes actuales.

Se conserva el principal central supuesto de 1.000/1.000 Mbps y el presupuesto WAN-2. El pico original de 42 terminales remotos y tres centrales exige 1.088,199 Mbps de subida y no se admite íntegro.

La política fija **hasta 30 terminales remotos con video y tres en CM**, contando dispositivos participantes y no salas ni reuniones. Se conservan 4/2,5 Mbps por terminal y full tunnel. La carga general y voz provienen del mismo perfil C5. Se cuenta una sola reserva del 10 % y utilización máxima del 70 %.

| Escenario | Bajada objetivo CM Mbps | Subida objetivo CM Mbps | Decisión |
|---|---:|---:|---|
| Normal sin video | 433,856 | 647,413 | Dentro de 1.000 por sentido |
| 30 terminales remotos + 3 centrales | 759,142 | 965,627 | Admitido por política académica |
| Pico anterior: 42 remotos + 3 centrales | 881,713 | 1.088,199 | Reducir participantes con cámara |

Se mantiene además el máximo del perfil C5 de dos terminales por sucursal continental y uno por sede pequeña; el límite agregado no autoriza concentrar 30 cámaras en una sola sucursal.

El límite matemático con tres centrales sería 33 remotos, casi sin margen adicional; se adopta 30. Estos objetivos ya contienen la reserva y el límite de utilización: no se descuentan otra vez del resultado. La fórmula de subida añade a la base sin video `(remotos × 6,5 + centrales × 2,5) × 1,1 / 0,7`. Para bajada se usa 4 por terminal central. La base JSON está redondeada a tres decimales, con esa misma precisión en la salida.

Operación propuesta: el coordinador limita participantes con cámara antes de iniciar y pasa el excedente a audio. En contingencia se suspende el video, se pausan copias y actualizaciones y se priorizan APP, voz y servicios. La réplica crítica solo consume capacidad restante; si se posterga, aumenta la antigüedad del dato y no se mantiene automáticamente la meta RPO. Ningún respaldo recibe capacidad de subida inventada. No se permite video nuevo hasta recuperar el principal estable.

Es una política y un cálculo de diseño. El simulador QoS demuestra reparto de capacidad por clases, **no implementa admisión automática ni controla una aplicación de reuniones**. El cálculo no demuestra codec real, calidad percibida ni capacidad contractual. Las seis aperturas y el crecimiento requieren nuevo dimensionamiento antes de habilitarse; no forman parte del límite de 30. No se amplían compras ni costos actuales.

Reproducción: `node network/c5-video-admission.cjs --check`. [Resultado generado](admision-video-c5.json). [Pruebas de límites y contingencia](../tests/c5-video-admission.test.cjs).
