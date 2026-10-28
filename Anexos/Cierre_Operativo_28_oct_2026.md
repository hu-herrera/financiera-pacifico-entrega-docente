# Cierre operativo para la defensa

Financiera Pacífico · C5-OPERACION-2 · 28 de octubre de 2026

## Versión

Simulador publicado: [`3598d23`](https://github.com/hu-herrera/fina/commit/3598d23fdc38b5a1a3f3c426eb6a380ca3c2682e). El commit probado `2dc5159` y el publicado comparten el árbol `0ee37564af2674aa653d0a6b31426bc0896a93aa`.

La presentación web conserva las 12 escenas de contenido y añade la escena 13 **Para finalizar**. La nueva conclusión queda visible al terminar el recorrido. El PowerPoint mantiene sus 14 láminas de avance y agrega una conclusión como lámina 15.

## Validación

| Comprobación | Resultado | Registro |
|---|---|---|
| Modelo, inventario, WAN y protocolos | 60 aprobadas; 0 fallidas | Evidencia_Publica_28_oct_2026/modelo.tap |
| Interfaz y operación A/B | 52 aprobadas; sin fallos ni omisiones | Evidencia_Publica_28_oct_2026/interfaz.json |
| Recorrido automático completo | 13 escenas en A y 13 en B; sin errores JavaScript | Evidencia_Publica_28_oct_2026/recorrido.json |
| Cierre visual | Escritorio y móvil, A/B | Imágenes final y final-mobile del directorio de evidencia |
| PPT | 15 láminas; tablas editables conservadas; revisión visual | Presentacion/Avance_Financiera_Pacifico_30_oct_2026.pptx |

Los conteos históricos de los anexos del 27 de octubre se mantienen como registros de sus cortes. El verificador público usa el SHA vigente.

## Operación comprobada

Los cambios de interfaces y OSPF modifican vecinos, rutas y el camino. Identidad, confianza, certificado o ESP inválidos impiden utilizar un borde VPN. Las asociaciones simuladas tienen SPI, vida, contadores y eventos. Los permisos siguen vigentes al conmutar. DHCP, DNS, HTTPS y SIP/RTP permiten distinguir falla de servicio de falta de camino. Una operación con el mismo identificador no se duplica. La configuración de protocolos se guarda por alternativa y la presentación conserva/restaura la sesión previa.

## Recuperación

El caso base ejecuta operaciones cada 10 s y réplicas cada 60 s, con 4 s para completarlas. Al fallar en t=157 s se selecciona la copia de t=120 s terminada en t=124 s. Conserva 12 de 15 operaciones y deja 3 por conciliar. El RPO observado es 30 s y el RTO observado 50 s del reloj virtual. Son resultados de los eventos y parámetros del modelo. Los objetivos del diseño siguen siendo 60 s y 300 s, respectivamente.

## Material para grabar

- [Guion de las 13 escenas](../Video/Guion_13_Escenas.md).
- [Matriz de protocolos y comandos](Matriz_Protocolos_Comandos.md).
- [Resultados completos de recuperación](Ejercicios_Recuperacion_C5.json).
- [Simulador](https://hu-herrera.github.io/fina/).

Pendiente de ejecución por el estudiante: grabar, revisar audio y legibilidad, enviar video y PPT por AVA y comprobar recepción antes del viernes 30 de octubre de 2026.
