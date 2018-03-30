# Resource Monitor #

* Autores: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala y otros
  colaboradores de NVDA
* Descargar [versión estable][1]

Este plugin nos da información acerca de la carga de la CPU, de la
utilización de la memoria y de otra información de uso de recursos.

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
* NVDA+Shift+7 presenta el tiempo de actividad del sistema.

Si tienes NVDA 2013.3 o una versión posterior, puedes cambiar estas teclas
de acceso directo.

## Notas de uso ##

Este complemento no sustituye al administrador de tareas y a otros programas
de información del sistema para Windows. También ten en cuenta lo siguiente:

* El uso de la CPU se da para procesadores lógicos, y no núcleos
  físicos. Esto es perceptible para los procesadores que utilizan Hyper
  Threading donde el número de CPUs es el doble del número de núcleos de
  CPU.
* Si hay una actividad pesada de disco tal como el copiado de ficheros
  grandes, podría haber retrasos al obtener información de uso de disco.
* El soporte para Windows XP de este complemento finalizará el 31 de
  diciembre de 2017. El soporte para Windows Server 2003, Windows Vista y
  Windows Server 2008 finalizará el 30 de junio de 2018.

## Versión 18.04

La versión 18.04.x es la última que soporta versiones de Windows anteriores
a la 7 SP1.

* Última versión en soportar Windows Server 2003, Vista y Server 2008.
* Mejor detección de versión de Windows 10 y distinción entre compilaciones
  public e Insider para pruebas.

## Versión 17.12

* Añadido el soporte para procesadores ARM de 64 bits en Windows 10.

## Versión 17.09

Importante: la versión 17.09.x es la última que soporta Windows XP.

* Última versión que se ejecuta en Windows XP.
* El Windows 10 compilación 16278 y posterior se reconoce como Versión
  1709. Se lanzará una revisión menor de este complemento una vez la versión
  1709 stable build se libere.

## Versión 17.07.1

* Se reintroduce el soporte para Windows XP (roto desde la versión 17.02).

## Versión 17.05

* Anunciado del tiempo de funcionamiento del sistema (tiempo transcurrido
  desde el último arranque; NVDA+Shift+7).

## Versión 17.02

* Actualizado psutil dependency a 5.0.1.
* Cuando se verifica el uso de disco, NVDA ya no presenta un diálogo de
  error en algunos sistemas donde no se reconoce apropiadamente un medio
  extraíble (tal como cuando una tarjeta no se inserta en un lector de
  tarjetas).)

## Versión 16.08

Comenzando con la versión 16.08, las versiones del complemento se mostrarán
como año.mes.revisión.

* Ahora se reconocen apropiadamente varias revisiones de Windows 10 (tales
  como 1607 para la compilación 14393).
* Las compilaciones de revisiones de Windows 10 (después de instalar
  actualizaciones acumulativas) se reconocen apropiadamente (tales como
  14393.51).
* Si se utilizan compilaciones Insider Preview, este hecho se reconoce.

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

[1]: https://addons.nvda-project.org/files/get.php?file=rm
