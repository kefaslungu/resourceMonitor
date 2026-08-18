# Resource Monitor

* Autores: Alex Hall, Joseph Lee, Kefas Lungu, beqa gozalishvili, Tuukka Ojala, Ethin Probst y otros colaboradores de NVDA

Este plugin nos da información acerca de la carga de la CPU, de la utilización de la memoria y de otra información de uso de recursos.

## Atajos de teclado

Todas las órdenes soportan el modo de voz a petición.

* NVDA+Shift+E: Presenta la ram utilizada, la carga promedio del procesador, e información de la batería si está disponible.
* NVDA+Shift+1: Presenta la carga promedio del procesador y el promedio de la carga de cada uno de los núcleos si los hay.
* NVDA+Shift+2/5: Presenta el espacio utilizado y total de la RAM física y virtual.
* NVDA+Shift+3: Presenta el espacio utilizado y el total de las unidades estáticas y extraíbles.
* NVDA+shift+4: presenta información sobre la conexión inalámbrica, nombre de SSID e intensidad, o sin nombre si no hay ninguno disponible.
* NVDA+Shift+6: Presenta la Arquitectura de la CPU y la versión de Windows y el número del Service Pack.
* NVDA+Shift+7: presenta el tiempo de actividad del sistema.
* Unassigned: presents information about the graphics processing unit (GPU; unavailable in secure mode).
* Unassigned: presents graphics processing unit (GPU memory usage information; unavailable in secure mode).

Puedes cambiar estos atajos desde el diálogo Gestos de entrada.

## Notas de uso

Este complemento no sustituye al administrador de tareas y a otros programas de información del sistema para Windows. También ten en cuenta lo siguiente:

* Apart from overall resource usage command (NVDA+Shift+E), pressing other commands twice will copy resource usage information to the clipboard.
* No se puede copiar la información de recursos al portapapeles si el complemento se ejecuta en pantallas seguras.
* El uso de la CPU se da para procesadores lógicos, y no núcleos físicos. Esto es perceptible para los procesadores que utilizan Hyper Threading donde el número de CPUs es el doble del número de núcleos de CPU. En algunos ordenadores más modernos, no todos los núcleos de CPU tienen activado el Hyper Threading.
* Si hay una actividad pesada de disco tal como el copiado de ficheros grandes, podría haber retrasos al obtener información de uso de disco.
* GPU information is given for Nvidia GPU's.
* Al anunciar la información de arquitectura del procesador, "x86" y "AMD64" se refieren a procesadores (Intel y AMD) de 32 y 64 bits, respectivamente.
* No se soporta la instalación del complemento en Windows 10/11 LTSC.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
