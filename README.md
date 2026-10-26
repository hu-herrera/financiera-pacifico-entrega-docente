# Financiera Pacífico - Entrega para revisión docente

**Estudiante:** Hugo Eduardo Herrera Inostroza

**Curso:** Proyecto de Título APT

**Corte:** 26 de octubre de 2026 - C5 A/B, WAN-3 y C5-RECUPERACION-1

[**Descargar el paquete de revisión en ZIP**](Entrega_Profesor_Financiera_Pacifico.zip)

## Entrega de avance: 30 de octubre de 2026

El docente solicita **video y PowerPoint por AVA** a más tardar el **viernes 30 de octubre de 2026**.

- [Presentación de avance en PowerPoint](Presentacion/Avance_Financiera_Pacifico_30_oct_2026.pptx).
- [Actualización del alcance, pendientes y planificación](Actualizacion_23_oct_2026.md).

La grabación y el envío por AVA están pendientes. El paquete refleja avances del proyecto académico y resultados del simulador.

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

La grabación se incorporará en la carpeta [Video/](Video/README.md).

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
