# Guion de defensa - 13 escenas

Financiera Pacífico · versión de grabación C5-OPERACION-2 · 28 de octubre de 2026

Abrir el simulador y pulsar Presentar. Elegir una alternativa y mantenerla durante el recorrido. El modo automático recorre las 13 escenas; permite pausa y repetición. Ensayar una vez antes de grabar para ajustar la narración al ritmo elegido. La web no graba voz ni video.

## 1. Continuidad operativa

El proyecto aborda la continuidad y seguridad de la comunicación entre las sedes de Financiera Pacífico. Trabajamos sobre un escenario de 23 sedes y 650 puestos. Seguiremos una solicitud para mostrar qué ocurre cuando una dependencia falla y cómo responde la propuesta.

## 2. Operación de la red anterior

En condiciones normales, una sucursal puede comunicarse con otra a través de central. Cada sucursal depende de un enlace MPLS y de sus equipos de acceso. Que el camino funcione ahora no demuestra que tenga una alternativa ante una falla.

## 3. Pérdida del enlace

Cortamos el único acceso remoto de la sucursal. El computador puede seguir encendido y la red local puede conservar conectividad, pero la comunicación con los servicios centrales queda interrumpida.

## 4. Diagnóstico

El enlace no es la única dependencia. El router decide la salida y el switch conecta los puestos. La mejora debe cubrir esas funciones y mantener un camino completo hasta la aplicación, incluyendo la respuesta.

## 5. Propuesta

La propuesta incorpora dos routers y dos switches por sucursal, accesos WAN alternativos y un par de firewalls centrales. Cada equipo adicional responde a una falla concreta. Los permisos se mantienen al cambiar de transporte.

## 6. Contingencia WAN

Interrumpimos los accesos de forma sucesiva. El motor busca un camino utilizable entre sucursal y central; no basta con que el terminal del proveedor siga encendido. El respaldo móvil permite una operación con menor capacidad. Al agotar los cuatro accesos, se pierde el camino central.

## 7. Router alternativo

Apagamos R1. La nueva comunicación debe evitarlo y utilizar R2. En las consolas podemos comprobar interfaces, vecinos OSPF, rutas y asociaciones VPN, y modificar su configuración para observar el efecto sobre el tráfico.

## 8. Acceso del puesto

Al perder el switch del puesto, el cable deja de servir. El PC puede utilizar el AP superviviente si tiene cobertura, autenticación y una dirección de contingencia. El teléfono necesita su propia radio y alimentación.

## 9. Seguridad

La aplicación admite HTTPS desde los puestos autorizados. La base de datos recibe conexiones desde la aplicación; los colaboradores no acceden directamente a ella. La voz, los invitados y la administración conservan permisos específicos. Una ruta disponible no concede permisos adicionales.

## 10. Firewall, aplicación y datos

Primero observamos el relevo del firewall. Después comprobamos las condiciones de recuperación del servidor: host alternativo, mayoría, aislamiento y copia utilizable. El ejercicio genera operaciones y réplicas con un reloj virtual. En el caso base, doce de quince operaciones están en la copia y tres requieren conciliación. El resultado de la ejecución es RTO 50 s y RPO 30 s virtuales. Los objetivos del diseño son 300 s y 60 s. Sin las condiciones necesarias, el modelo bloquea la recuperación.

## 11. Inversión

Comparamos A, con Cisco y Palo Alto, y B, con MikroTik y OPNsense. La inversión inicial es de aproximadamente 793,1 y 281,2 millones de pesos, respectivamente. A cinco años, el alcance suma aproximadamente 1.503,7 y 966,8 millones, incluyendo la WAN y las reservas de operación. Ambas alternativas superan la referencia original de 160 millones.

## 12. Crecimiento y operación

Las seis aperturas futuras se evalúan en una fase posterior. Crecer exige dimensionar los enlaces. En contingencia, QoS conserva prioridades para aplicación y voz, mientras las copias y el video se limitan. El reparto no aumenta la capacidad del enlace.

## 13. Para finalizar

Para finalizar, la propuesta busca sostener la atención mediante caminos alternativos, acceso controlado y recuperación de los servicios centrales. Cada decisión debe responder a una dependencia identificada y a una necesidad de operación. Presentamos dos alternativas de inversión para evaluar junto con su soporte y mantenimiento. Muchas gracias; quedamos disponibles para preguntas y pruebas sobre el simulador.

## Demostraciones libres para preguntas

1. En S06/R1: consultar `show ip ospf neighbor`; ejecutar `sim ospf area 9`; comprobar que se utiliza R2. Restaurar con `sim ospf area 0` y «Volver al principal».
2. En S06/R1 y R2: ejecutar `sim vpn certificate invalid`; probar HTTPS y observar que no hay un borde autenticable. Restaurar ambos con `sim vpn certificate valid`.
3. Desde el PC: `nslookup app.financiera.test` y `curl https://app.financiera.test`. En central: `sim service dns down`; repetir por nombre y después por IP para diferenciar las dependencias. Restaurar DNS.
4. Registrar una operación: `sim transaction prueba-001`; repetir el ID y comprobar que no se duplica.
5. En el explorador de recuperación: variar el instante del fallo y el intervalo de réplica; comparar operaciones conservadas, conciliación y eventos.

Las pruebas libres pueden hacerse después del recorrido. El cierre permanece visible y «Explorar detalles» conserva acceso a herramientas. Salir de Presentar restaura el estado anterior a la sesión.

## Antes del envío

Revisar que se lean las IP y resultados, que el audio sea claro y que el archivo final abra completo. Entregar el video y el PowerPoint por AVA y comprobar su recepción antes del viernes 30 de octubre de 2026. La grabación y el envío todavía deben ejecutarse.
