# Resource Monitor #

* Autores: Alex Hall, Joseph Lee, beqa gozalishvili y otros colaboradores de
  NVDA
* Descargar [versión estable][1]

Este plugin nos da información acerca de la carga de la CPU, del uso de la
memoria y de otra información de uso de recursos.

Importante: Resource Monitor 3.1 no es compatible con NVDA 2013.3 o
anterior. Si utilizas  2013.3 o anterior, por favor utiliza Resource Monitor
3.0.

# Atajos de teclado #

* NVDA+Shift+E Presenta la ram utilizada, la carga promedio del procesador,
  e información de la batería si está disponible,
* NVDA+Shift+1 Presenta la carga promedio del procesador y el promedio de la
  carga de cada uno de los núcleos si los hay
* NVDA+Shift+2/5 Presenta el espacio utilizado y total de la RAM física y
  virtual,
* NVDA+Shift+3 Presenta el espacio utilizado y el total de las unidades
  estáticas y extraíbles.
* NVDA+Shift+4 Presenta el porcentaje de la batería, el estado de la carga,
  el tiempo restante (si no se está cargando), y una advertencia si
  la. batería está baja o crítica.
* NVDA+Shift+6 Presenta la Arquitectura 32/64-bit de la CPU y la versión de
  Windows y el número del Service Pack.

Si tienes NVDA 2013.3 o una versión posterior, puedes cambiar estas teclas
de acceso directo.

## Notas de uso ##

Este complemento no sustituye al administrador de tareas y a otros programas
de información del sistema para Windows. También ten en cuenta lo siguiente:

* El uso de la CPU se da para procesadores lógicos, y no núcleos
  físicos. Esto es perceptible para los procesadores que utilizan Hyper
  Threading donde el número de CPUs es el doble del número de núcleos de
  CPU.
* Podría haber un pequeño retraso al obtener información de uso del
  procesador.

## Cambios para 4.5 ##

* El repositorio del complemento se ha movido a GitHub (puede encontrarse en
  https://github.com/josephsl/resourcemonitor).
* Se reconoce apropiadamente Windows Server 2016.

## Cambios para 4.0 ##

* Actualizado psutil dependency a 2.2.1.
* Mejorado enormemente el rendimiento al obtener información en la carga de
  la CPU.
* Añadido el soporte para reconocimiento de Windows 10.
* En Windows 10, también se anunciará el número de compilación de Windows.
* Puedes utilizar el Administrador de Complementos para acceder a la ayuda
  del complemento.

## Cambios para 3.1 ##

* Resource Monitor soporta oficialmente Windows 8.1.
* Se actualizan las traducciones.

## Cambios para 3.0 ##

* Actualizada dependencia psutil a 1.2.1.
* Anunciado de la versión de Windows, la arquitectura de la CPU y el service
  pack  actual en su caso (NVDA+Shift+6).
* Posibilidad de cambiar los atajos de teclado de los complementos (NVDA
  2013.3 o posterior).
* Posibilidad de copiar la información individual de recursos al
  portapapeles pulsando órdenes de recursos dos veces.

## Cambios para 2.4 ##

* Nuevos idiomas: Chino (simplificado), Ucraniano.
* Se actualizan las traducciones.

## Cambios para 2.3 ##

* Añadida la traducción al búlgaro.

## Cambios para 2.2 ##

* Añadidas siguientes traducciones: árabe, aragonés, croata, holandés,
  finlandés, francés, gallego, alemán, japonés húngaro, italiano, coreano,
  nepalí, polaco, portugués (Brasil), ruso, eslovaco, esloveno, español,
  tamil y turco.

## Cambios para 2.1 ##

* Actualizada dependencia sutíl a la versión 0.6.1.
* Corregidos los grandes retrasos al optenerse información de unidades.
* Limpieza de código.

## Cambios para 2.0 ##

* añadido el soporte para traducciones y los comentarios de las
  traducciones.

## Cambios para 1.0 ##

* Versión inicial

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm [2]:
http://addons.nvda-project.org/files/get.php?file=rm-next
