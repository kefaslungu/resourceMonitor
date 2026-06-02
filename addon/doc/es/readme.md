# Resource Monitor

* Autores: Alex Hall, Joseph Lee, Kefas Lungu, beqa gozalishvili, Tuukka Ojala, Ethin Probst y otros colaboradores de NVDA

Este plugin nos da información acerca de la carga de la CPU, de la utilización de la memoria y de otra información de uso de recursos.

## Atajos de teclado

Todas las órdenes soportan el modo de voz a petición.

* NVDA+Shift+E: Presenta la ram utilizada, la carga promedio del procesador, e información de la batería si está disponible.
* NVDA+Shift+1: Presenta la carga promedio del procesador y el promedio de la carga de cada uno de los núcleos si los hay.
* NVDA+Shift+2/5: Presenta el espacio utilizado y total de la RAM física y virtual.
* NVDA+Shift+3: Presenta el espacio utilizado y el total de las unidades estáticas y extraíbles.
* NVDA+Shift+4: Presenta el porcentaje de la batería, el estado de la carga, el tiempo restante (si no se está cargando), y una advertencia si la batería está baja o crítica.
* NVDA+Shift+6: Presenta la Arquitectura de la CPU y la versión de Windows y el número del Service Pack.
* NVDA+Shift+7: presenta el tiempo de actividad del sistema.
* NVDA+shift+8: presenta información sobre la conexión inalámbrica, nombre de SSID e intensidad, o sin nombre si no hay ninguno disponible.

Puedes cambiar estos atajos desde el diálogo Gestos de entrada.

## Notas de uso

Este complemento no sustituye al administrador de tareas y a otros programas de información del sistema para Windows. También ten en cuenta lo siguiente:

* No se puede copiar la información de recursos al portapapeles si el complemento se ejecuta en pantallas seguras.
* El uso de la CPU se da para procesadores lógicos, y no núcleos físicos. Esto es perceptible para los procesadores que utilizan Hyper Threading donde el número de CPUs es el doble del número de núcleos de CPU. En algunos ordenadores más modernos, no todos los núcleos de CPU tienen activado el Hyper Threading.
* Si hay una actividad pesada de disco tal como el copiado de ficheros grandes, podría haber retrasos al obtener información de uso de disco.
* Al anunciar la información de arquitectura del procesador, "x86" y "AMD64" se refieren a procesadores (Intel y AMD) de 32 y 64 bits, respectivamente.
* Este complemento necesita Windows 10 22H2 (Actualización de 2022 /compilación 19045) o posterior.
* No se soporta la instalación del complemento en Windows 10/11 LTSC.
