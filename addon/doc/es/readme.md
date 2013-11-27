# resource Monitor #

* Autores: Alex Hall, Joseph Lee, beqa gozalishvili y otros colaboradores de
  NVDA
* Versión estable: [versión 2.4][1]
* Versión de desarrollo: [versión 3.0-dev][2]

Este plugin nos da información acerca de la carga de la CPU, del uso de la
memoria, de la batería y del estado de uso del disco.

# Atajos de teclado #

* NVDA+Shift+E Presenta la ram utilizada, la carga media del procesador, e
  información de la batería si está disponible,
* NVDA+Shift+1 Presenta la carga media del procesador y la carga de cada uno
  de los núcleos,
* NVDA+Shift+2/5 Presenta el espacio utilizado y total de la RAM física y
  virtual,
* NVDA+Shift+3 Presenta el espacio utilizado y el total de las unidades
  estáticas y extraíbles en este ordenador,
* NVDA+Shift+4 Presenta el porcentaje de la batería, el estado de la carga,
  el tiempo restante (si no se está cargando), y una advertencia si la
  batería está baja o crítica,
* NVDA+Shift+6 Presenta la versión de Windows actualmente instalada, los
  bits de la CPU (32 o 64 bits) y el Service Pack si lo hay (versión
  3.0-dev).

## Notas de uso ##

Este complemento no sustituye al administrador de tareas y a otros programas
de información del sistema para Windows. También ten en cuenta lo siguiente:

* El uso de la CPU se da para procesadores lógicos, y no núcleos
  físicos. Esto es perceptible para los procesadores que utilizan Hyper
  Threading donde el número de CPUs es el doble del número de núcleos de
  CPU.
* Podría haber un pequeño retraso al obtener información de uso del
  procesador.

## Cambios para 3.0-dev ##

* Actualizada dependencia psutil a 1.2.1.
* Añadida una orden (NVDA+Shift+6) para informar de la versión de Windows
  que esté utilizando, bits de la CPU y service packs  si los hubiere.
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

* Añadidas las siguientes traducciones: alemán, aragonés, Coreano, croata,
  Eslovaco, esloveno, Español, finlandés, francés, Gallego, holandés,
  húngaro,Italiano, Nepalí, Portugués (Brasil), Ruso, Tamil y Turco.

## Cambios para 2.1 ##

* Actualizada dependencia sutíl a la versión 0.6.1.
* Corregidos los grandes retrasos al optenerse información de unidades.
* Substituido %s-es en {friendlyVariableNames}.
* Una pequeña limpieza en el código

## Cambios para 2.0 ##

* añadido el soporte para traducciones y los comentarios de las
  traducciones.

## Cambios para 1.0 ##

* Versión inicial

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
