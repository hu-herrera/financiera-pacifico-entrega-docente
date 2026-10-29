# Coherencia de la presentación del 29 de octubre de 2026

La presentación web y el PowerPoint contienen las mismas 13 escenas. La tabla identifica las etapas internas de las demostraciones; no son láminas adicionales.

| N.º | Escena en web y PowerPoint | Etapas del ejemplo |
|---|---|---|
| 1 | Continuidad operativa | Contenido explicativo, sin ejemplo automático |
| 2 | La red anterior en operación | Situación; Camino inicial; Qué aprendemos |
| 3 | El corte de una conexión | Situación; Camino inicial; Fallo y respuesta; Qué aprendemos |
| 4 | Dependencias del acceso | Contenido explicativo, sin ejemplo automático |
| 5 | La red propuesta | Contenido explicativo, sin ejemplo automático |
| 6 | Una conexión alternativa | Situación; Camino inicial; Fallo y respuesta; Satelitales caídos; Último respaldo; Sin ningún acceso; Qué aprendemos |
| 7 | Un router alternativo | Situación; Camino inicial; Fallo y respuesta; Qué aprendemos |
| 8 | Respaldo Wi-Fi del puesto | Situación; Camino inicial; Fallo y respuesta; Qué aprendemos |
| 9 | Control de acceso con ACL | Trabajo autorizado; Acceso restringido; Invitado aislado |
| 10 | Firewall y recuperación del datacenter | Situación; Camino inicial; Fallo y respuesta; Qué aprendemos; Servidor alternativo; Qué datos vuelven; Antes de reabrir; Réplica antigua; Copia inconsistente; Límite del sitio |
| 11 | Inversión y alternativas | Contenido explicativo, sin ejemplo automático |
| 12 | Crecimiento y operación | Demanda concurrente; Reparto por prioridad; Operación degradada |
| 13 | Para finalizar | Contenido explicativo, sin ejemplo automático |

## Comportamiento revisado

El ejemplo WAN interrumpe transportes de S06 de forma sucesiva; los accesos centrales conservan su estado inicial. Leo se identifica como respaldo satelital. El ejemplo de recuperación reúne las comprobaciones y conserva los casos de copia antigua, inconsistente y pérdida de ambos hosts. QoS mantiene visible la asignación al pausar. Avanzar una etapa reproduce su animación de paquete aunque el relato permanezca en pausa.

La web toma títulos, mensajes y puntos del único índice ClientStory. El PowerPoint y el índice JSON conservan esa numeración. La verificación de interfaz recorre cada escena en A/B y compara sus títulos y etapas. La verificación documental contrasta los títulos con las 13 láminas del PPT y comprueba que sus imágenes estén incorporadas.

## Alcance y resultados

60 pruebas de modelo y 52 pruebas de interfaz aprobadas en el corte del 29 de octubre. Recorridos manual y automático comprobados en A/B, sin errores JavaScript. Resultados y capturas en Evidencia_Publica_29_oct_2026. Los cortes del 27 y 28 se conservan como evidencia histórica.

Los resultados describen el prototipo y sus eventos con tiempo virtual; no son mediciones de firmware ni de servidores físicos. El caso base de recuperación conserva 12 de 15 operaciones, con tres por conciliar, RTO virtual 50 s y RPO virtual 30 s. El presupuesto y el inventario no cambian.
