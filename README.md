# Financiera Pacífico - Entrega para revisión docente

**Estudiante:** Hugo Eduardo Herrera Inostroza

**Curso:** Proyecto de Título APT

**Corte:** 28 de octubre de 2026 - C5 A/B, WAN-3 y C5-OPERACION-2; versión de defensa con 13 escenas

[**Descargar el paquete de revisión en ZIP**](Entrega_Profesor_Financiera_Pacifico.zip)

## Entrega de avance: 30 de octubre de 2026

El docente solicita **video y PowerPoint por AVA** a más tardar el **viernes 30 de octubre de 2026**.

- [Presentación de avance en PowerPoint](Presentacion/Avance_Financiera_Pacifico_30_oct_2026.pptx).
- [Actualización del alcance, pendientes y planificación](Actualizacion_23_oct_2026.md).

El paquete presenta el estado del proyecto al corte indicado, con resultados del simulador y documentación técnica de respaldo.

## Orden de lectura

1. [Caso oficial transcrito](00_Caso_Oficial.pdf) y [archivo original del Capstone](00_Caso_Original_Capstone.xlsx).
2. [Informe de diagnóstico y propuesta de solución](01_Informe_Diagnostico_Propuesta.pdf).
3. Entregables numerados:

   - [Entregable 1](02_Entregables/Entregable_1.pdf).
   - [Entregable 2](02_Entregables/Entregable_2.pdf).
   - [Entregable 3](02_Entregables/Entregable_3.pdf).
   - [Entregable 4](02_Entregables/Entregable_4.pdf).
   - [Entregable 5](02_Entregables/Entregable_5.pdf).
   - [Entregable 6](02_Entregables/Entregable_6.pdf).
   - [Entregable 7](02_Entregables/Entregable_7.pdf).

4. [Bitácora de evolución y cierre](03_Bitacora.pdf).

## Video de demostración

La demostración audiovisual corresponde al hito académico del 30 de octubre; el material técnico de apoyo está descrito en la [actualización de avance](Actualizacion_23_oct_2026.md).

## Anexos técnicos de los entregables

- [Topologías ANTES/A/B](Anexos/Topologias_ANTES_A_B.pdf).
- [Presupuesto e inventario Excel](Anexos/Presupuesto_Inventario.xlsx).
- [Direcciones y puertos por sede A/B](Anexos/Inventario_IPAM_Puertos.md).
- [Fuentes técnicas y precios](Anexos/Fuentes_Tecnicas_y_Precios.md).
- [Manifiesto de integridad](MANIFIESTO.sha256).

[Acceso al simulador del proyecto](https://hu-herrera.github.io/fina/).

Este repositorio contiene únicamente documentación académica de revisión y sus anexos técnicos. Los documentos distinguen la ficha oficial, los supuestos adoptados y los resultados del prototipo. El informe incluye correspondencia con las observaciones de la primera entrega. Los estados previos de la bitácora son históricos y no sustituyen el cierre vigente.

La [revisión WAN-2](Anexos/Revision_WAN_24_oct_2026.md) cierra la sustitución de distribuidores también en A. Ambas opciones usan 45 hEX E50UG y un CRS310; el PPT, inventario y presupuesto reflejan el cambio.

[Cierre vigente del 25 de octubre: capacidad y evidencia posterior de E6/E7](Anexos/Cierre_25_oct_2026.md).

**Revisión WAN-3 vigente:** [cuatro accesos también en Casa Matriz y costos conciliados](Anexos/Continuidad_Cuatro_WAN_25_oct_2026.md).

## Recuperación del datacenter y entrega técnica - 26 de octubre

La escena 10 de la presentación integrada muestra qué datos recupera el host alternativo, qué operaciones requieren conciliación y cuándo se bloquea un reinicio por falta de condiciones. El complemento utiliza los dos hosts y BKP-01 existentes, sin nuevas compras ni cambios de presupuesto.

- [Guía de operación y recuperación en PDF](Anexos/Operacion_Recuperacion_Datacenter_C5.pdf).
- [Procedimiento consultable](Anexos/Operacion_Recuperacion_Datacenter_C5.md).
- [Resultados reproducibles A/B con operaciones ficticias](Anexos/Ejercicios_Recuperacion_C5.json).

Se entrega preparación técnica y procedimiento; la financiera opera, mantiene, valida los datos y autoriza la reapertura. Electricidad y climatización se consideran infraestructura existente a su cargo. No se declara implantación de una aplicación bancaria ni medición física de RTO/RPO.

## Cierre documental del 27 de octubre

Se concilian el flujo anual, los importes WAN del informe, el cierre de la bitácora y los escenarios E4/E6. La escena 10 distingue firewall, recuperación de servicios y conciliación. El inventario y los totales WAN-3 se conservan.

- [Evidencia, cortes y reproducción pública](Anexos/Evidencia_Pruebas_27_oct_2026.md).
- [Fuentes académicas editables](Fuentes/).
- [Verificación pública automatizada](https://github.com/hu-herrera/financiera-pacifico-entrega-docente/actions/workflows/verificacion-publica.yml).

El ZIP contiene los mismos archivos que el manifiesto publicado. El manifiesto se regenera después de cualquier modificación de los documentos o anexos.

## Versión de defensa del 28 de octubre

La presentación web agrega la escena 13 «Para finalizar». Protocolos, comandos, reglas y servicios comparten el estado de tráfico. El ejercicio de recuperación calcula resultados a partir de eventos con tiempo virtual.

- [Matriz de protocolos, comandos y efectos](Anexos/Matriz_Protocolos_Comandos.md).
- [Evidencia vigente del cierre operativo](Anexos/Cierre_Operativo_28_oct_2026.md).

Las pruebas anteriores conservan sus cortes históricos. El ZIP y el manifiesto reflejan el cierre vigente. Pendientes: grabar, revisar y enviar video/PPT por AVA.
