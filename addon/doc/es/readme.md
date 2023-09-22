# Resource Monitor #

* Autores: Alex Hall, Joseph Lee, Kefas Lungu, beqa gozalishvili, Tuukka
  Ojala, Ethin Probst y otros colaboradores de NVDA
* Descargar [versión estable][1]
* Compatibilidad con NVDA: de 2022.4 en adelante

Este plugin nos da información acerca de la carga de la CPU, de la
utilización de la memoria y de otra información de uso de recursos.

# Atajos de teclado

* NVDA+Shift+E: Presenta la ram utilizada, la carga promedio del procesador,
  e información de la batería si está disponible.
* NVDA+Shift+1: Presenta la carga promedio del procesador y el promedio de
  la carga de cada uno de los núcleos si los hay.
* NVDA+Shift+2/5: Presenta el espacio utilizado y total de la RAM física y
  virtual.
* NVDA+Shift+3: Presenta el espacio utilizado y el total de las unidades
  estáticas y extraíbles.
* NVDA+Shift+4: Presenta el porcentaje de la batería, el estado de la carga,
  el tiempo restante (si no se está cargando), y una advertencia si la
  batería está baja o crítica.
* NVDA+Shift+6: Presenta la Arquitectura de la CPU y la versión de Windows y
  el número del Service Pack.
* NVDA+Shift+7: presenta el tiempo de actividad del sistema.
* NVDA+shift+8: presenta información sobre la conexión inalámbrica, nombre
  de SSID e intensidad, o sin nombre si no hay ninguno disponible.

Puedes cambiar estos atajos desde el diálogo Gestos de entrada.

## Notas de uso

Este complemento no sustituye al administrador de tareas y a otros programas
de información del sistema para Windows. También ten en cuenta lo siguiente:

* No se puede copiar la información de recursos al portapapeles si el
  complemento se ejecuta en pantallas seguras.
* El uso de la CPU se da para procesadores lógicos, y no núcleos
  físicos. Esto es perceptible para los procesadores que utilizan Hyper
  Threading donde el número de CPUs es el doble del número de núcleos de
  CPU. En algunos ordenadores más modernos, no todos los núcleos de CPU
  tienen activado el Hyper Threading.
* Si hay una actividad pesada de disco tal como el copiado de ficheros
  grandes, podría haber retrasos al obtener información de uso de disco.
* Al anunciar la información de arquitectura del procesador, "x86" y "AMD64"
  se refieren a procesadores (Intel y AMD) de 32 y 64 bits, respectivamente.
* Este complemento necesita Windows 10 o posterior.

Nota sobre licencias: este complemento usa Psutil, liberado bajo la licencia
3-Clause BSD, que es compatible con la Licencia Pública General GNU.

## Versión 23.09

* NVDA ya no registrará mensajes de error al iniciar en sistemas Windows
  Server cuando los módulos de red inalámbrica no estén disponibles.

## Versión 23.06

* Se ha corregido una situación en la que Resource Monitor no funcionaba
  adecuadamente a causa de falta de disponibilidad de los módulos de red
  inalámbrica.

## Versión 23.05.1

¡El complemento Wlan Reporter para NVDA ahora forma parte de Resource
Monitor!

* Se ha sustituido el método antiguo para comprobar las conexiones
  inalámbricas por la API de Windows de Wlan Reporter:
  https://github.com/kvark128/WlanReporter/ .

	* Tras verbalizar el nombre de la red y su intensidad, NVDA también
	  indicará el tipo de seguridad de la red.
	* NVDA ahora avisará al conectarse y desconectarse de una red inalámbrica.
	* NVDA ahora avisará al activar o desactivar las conexiones inalámbricas.

## Versión 23.05

* se ha añadido la capacidad de detectar y presentar el estado de la red
  inalámbrica conectada.

	* Anuncia el nombre del SSID inalámbrico conectado.
	* Anuncia la intensidad del SSID
	* Anuncia SSID no encontrado si no se detecta ninguno.

## Versión 23.02

* Se requiere NVDA 2022.4 o posterior.
* Se requiere Windows 10 21H2 (actualización de noviembre de 2021 /
  compilación 19044) o posterior.

## Versión 23.01

* Se requiere NVDA 2022.3 o posterior.
* Se requiere Windows 10 o posterior, ya que Microsoft no soporta Windows 7,
  8 y 8.1 a partir de enero de 2023.
* Actualizada la dependencia psutil a 5.9.4.
* NVDA anunciará la arquitectura real del procesador (x86 / AMD64 / ARM64)
  como parte de la información de versión de Windows.
* En sistemas de un solo núcleo, NVDA ya no anunciará la carga del núcleo de
  CPU, ya que coincide con la carga media de la CPU.

## Versión 22.03

La versión 22.03 es la última versión estable que soporta Windows 7 Service
Pack 1, 8 y 8.1.

* Se requiere NVDA 2021.3 o posterior.
* Se mostrará un mensaje de aviso al intentar instalar el complemento en
  Windows 7, 8 y 8.1.
* Actualizada la dependencia psutil a 5.9.0.

## Versión 22.01

* Se requiere NVDA 2021.2 o posterior.

## Versión 21.10

* Se requiere NVDA 2021.1 o posterior a causa de cambios en NVDA que afectan
  a este complemento.

## Versión 21.08

* El requisito mínimo de versión de Windows ahora está vinculado a la
  versión de NVDA.
* Las compilaciones de Windows 20348 y 22000 se reconocen como Windows
  Server 2022 y Windows 11, respectivamente.
* En compilaciones de prueba Insider, no se usarán versiones de Windows como
  "Windows 10". En su lugar, NVDA anunciará "Windows Insider".
* En sistemas de 64 bits, se anunciará la arquitectura del procesador (X64 o
  ARM64) como parte de la información de versión de Windows.

## Versión 21.04

* Se requiere NVDA 2020.4 o posterior.
* Actualizada la dependencia psutil a 5.8.0.
* Al pulsar las órdenes del complemento dos veces rápidamente para copiar la
  información del recurso al portapapeles, NVDA anunciará un resumen del
  recurso que se copia.

## Versión 21.01

* Actualizada la dependencia psutil a 5.7.3.
* Acortado el mensaje de versión de Windows.
* En Windows 8.1, se anunciará compilación.revisión como parte del mensaje
  de versión de Windows, similar a Windows 10.

## Versión 20.09

* El tiempo que lleva iniciado el sistema se expresa en días, horas, minutos
  y segundos.
* Se reconoce la compilación preliminar Windows Server Insider versión 20201
  y posteriores como una compilación de Server Insider.

## Versión 20.07

* Al obtener información sobre la versión de Windows (NVDA+shift+6), se
  reconoce adecuadamente la versión 20H2 de Windows 10.
* Simplificado el mensaje de versión de Windows 10 al pulsar
  NVDA+shift+6. Ahora será Windows 10 AAMM en vez de Windows 10 ver AAMM.

## Versión 20.06

* Se han resuelto muchos problemas de estilo del código y fallos potenciales
  con Flake8.

## Versión 20.04

* Actualizada la dependencia psutil a 5.7.0.

## Versión 20.01

* Se requiere NVDA 2019.3 o posterior debido al uso extenso de Python 3.

## Versión 19.11

* Se ha mejorado la detección de compilaciones de Windows Insider,
  especialmente para la 20H1 y posteriores.

## Versión 19.07

* Actualizada la dependencia psutil a 5.6.3.
* Cambios internos en la orden de anuncio del estado de la batería.

## Versión 18.12

* Cambios internos para dar soporte a futuras versiones de NVDA.

## Versión 18.10

* El código se ha hecho más compatible con Python 3.
* Actualizada la dependencia psutil a 5.4.7.
* Al obtener la capacidad de disco o el uso de la memoria, NVDA ya no dará
  errores si se utiliza un ordenador o servicio con más de un petabyte de
  ram o disco.
* Los valores de uso de la memoria y de disco se muestran con hasta dos
  cifras decimales (por ejemplo, 4.00 GB en vez de 4.0 GB).
* Se ha mejorado la detección de compilaciones de Windows Insider.

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

## Cambios para 4.5

* El repositorio del complemento se ha movido a GitHub (puede encontrarse en
  https://github.com/josephsl/resourcemonitor).
* Se reconoce apropiadamente Windows Server 2016.

## Cambios para 4.0

* Actualizado psutil dependency a 2.2.1.
* Mejorado enormemente el rendimiento al obtener información en la carga de
  la CPU.
* Añadido el soporte para reconocimiento de Windows 10.
* En Windows 10, también se anunciará el número de compilación de Windows.
* Puedes utilizar el Administrador de Complementos para acceder a la ayuda
  del complemento.

## Cambios para 3.1

* Resource Monitor soporta oficialmente Windows 8.1.
* Se actualizan las traducciones.

## Cambios para 3.0

* Actualizada dependencia psutil a 1.2.1.
* Anunciado de la versión de Windows, la arquitectura de la CPU y el service
  pack  actual en su caso (NVDA+Shift+6).
* Posibilidad de cambiar los atajos de teclado de los complementos (NVDA
  2013.3 o posterior).
* Posibilidad de copiar la información individual de recursos al
  portapapeles pulsando órdenes de recursos dos veces.

## Cambios para 2.4

* Nuevos idiomas: Chino (simplificado), Ucraniano.
* Se actualizan las traducciones.

## Cambios para 2.3

* Añadida la traducción al búlgaro.

## Cambios para 2.2

* Añadidas siguientes traducciones: árabe, aragonés, croata, holandés,
  finlandés, francés, gallego, alemán, japonés húngaro, italiano, coreano,
  nepalí, polaco, portugués (Brasil), ruso, eslovaco, esloveno, español,
  tamil y turco.

## Cambios para 2.1

* Actualizada dependencia sutíl a la versión 0.6.1.
* Corregidos los grandes retrasos al optenerse información de unidades.
* Limpieza de código.

## Cambios para 2.0

* añadido el soporte para traducciones y los comentarios de las
  traducciones.

## Cambios para 1.0

* Versión inicial

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
