# Resource Monitor #

* Autores: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala e outros
  colaboradores do NVDA
* Descargar [versión estable][1]
* Compatibilidade con NVDA: da 2017.4 á 2019.2

Este plugin danos información acerca da carga da CPU, do uso da memoria e
outras informacións de uso dos recursos.

# Atallos de teclado #

* NVDA+Shift+E Presenta a ram utilizada, a carga media do procesador, e
  información da batería se está dispoñible,
* NVDA+Shift+1 Presenta a carga media do procesador e CPU multicor se están
  presentes a carga de cada núcleo.
* NVDA+Shift+2/5 Presenta o espazo utilizado e total da ram tanto física
  coma virtual,
* NVDA+Shift+3 Presenta o espazo usado e total das unidades estáticas e
  extraíbles .
* NVDA+Shift+4 Presenta a porcentaxe da batería, o estado da carga, o tempo
  restante (se non se está a cargar), e un aviso se a batería está débil ou
  crítica.
* NVDA+Shift+6 Presenta a arquitectura da CPU 32/64-bit e a versión de
  Windows e as cifras do service pack.
* NVDA+Shift+7 presenta o tempo de actividade do sistema.

Se tes NVDA 2013.3 ou posterior instalado, podes cambiar estas teclas de
acceso.

## Notas de uso ##

Este complemento non substitúe ó xestor de tarefas e a outros programas de
información do sistema para Windows. Ademais, ten en conta o seguinte:

* O Uso da CPU dase para os procesadores lóxicos, non para os núcleos
  físicos. Isto é perceptible para os procesadores que usan Hyper Threading
  onde o número de CPUs é o dobre do número de núcleos de CPU.
* Se hai unha actividade pesada de disco coma o copiado de ficheiros longos,
  podería haber retrasos ao obter información de uso do disco.
* O soporte para o Windows XP deste complemento rematou o 31 de decembro do
  2017. O soporte para o Windows Server 2003, o Windows Vista e o Windows
  Server 2008 rematou o 30 de xunio do 2018.

## Versión 18.10

* Fíxose o código máis compatible con Python 3.
* Actualizada a dependencia psutil á versión Actualizado psutil dependency a
  5.0.1.5.4.7.
* Ao obter a capacidade de disco e o uso de memoria, NVDA xa non dará máis
  erros cando se utilice un computador ou servizo con máis dun petabyte de
  RAM ou tamaño de disco.
* Os valores do uso da memoria e do disco amósanse con ata dous lugares
  decimais (p.ex. 4.00 GB no canto de 4.0 GB).
* Mellorada a detección de compilacións Windows Insider Preview.

## Versión 18.04

A versión 18.04.x é a derradeira que soporta versións de Windows anteriores
á 7 SP1.

* Derradeira versión en soportar Windows Server 2003, Vista e Server 2008.
* Mellor detección da versión de Windows e distinción entre compilacións
  públicas e Insider de probas.

## Versión 17.12

* Engadido o soporte para procesadores ARM de 64 bits en Windows 10.

## Versión 17.09

Importante: a versión 17.09.x é a derradeira que soporta o Windows XP.

* Derradeira versión que se executa no Windows XP.
* O Windows 10 compilación 16278 e posterior recoñécese coma Versión
  1709. lanzarase unha revisión menor deste complemento unha vez a versión
  1709 stable build se libere.

## Versión 17.07.1

* Reintrodúcese o soporte para o Windows XP (rompido dende a versión 17.02).

## Versión 17.05

* Anunciado do tempo de funcionamiento do sistema (tempo transcorrido dende
  o último arranque; NVDA+Shift+7).

## Versión 17.02

* Actualizado psutil dependency a 5.0.1.
* Cando se verifica o uso de disco, NVDA xa non presenta un diálogo de erro
  nalgúns sistemas onde non se recoñece apropriadamente un medio extraíble
  (como cando unha tarxeta non se inserta nun lector de tarxetas).)

## Versión 16.08

Comezando ca versión 16.08, as versións do complemento amosaranse como
ano.mes.revisión.

* Agora recoñécense apropriadamente varias revisións do Windows 10 (como
  1607 para a compilación 14393).
* As compilacións de revisións do Windows 10 (despois de instalar
  actualizacións acumulativass) recoñécense apropriadamente (como 14393.51).
* Se usas compilacións Insider Preview, este feito recoñécese.

## Cambios para 4.5 ##

* O repositorio do complemento moviuse a GitHub (pode atoparse en
  https://github.com/josephsl/resourcemonitor).
* Recoñécese apropriadamente Windows Server 2016.

## Cambios para 4.0 ##

* Actualizado psutil dependency a 2.2.1.
* Mellorado enormemente o rendemento ó obter información na carga da CPU.
* Engadido soporte para o recoñecemento do Windows 10.
* En Windows 10, tamén se anunciará o número de compilación do Windows.
* Podes ir o Administrador de Complementos para acceder á axuda do
  complemento.

## Cambios para 3.1 ##

* Resource Monitor soporta oficialmente Windows 8.1.
* Actualízanse as traduccións.

## Cambios para 3.0 ##

* Actualizada dependencia psutil para 1.2.1.
* Anuncio da versión actual de Windows, arquitectura da CPU e do service
  pack se o hai(NVDA+Shift+6).
* Capacidade de cambiar os atallos de teclado do complemento (NVDA 2.013,3
  ou posterior).
* Habilidade para copiar información dun recurso individual ó portapapeis
  premendo Ordes de recurso dúas veces.

## Cambios para 2.4 ##

* Novas linguas: Chinese (simplificado), Ucranián.
* Actualízanse as traduccións.

## Cambios para 2.3 ##

* Engadida a traducción ó búlgaro.

## Cambios para 2.2 ##

* Seguintes traducións Engadidas: Árabe, aragonés, croata, holandés,
  finlandés, francés, galego, alemán, húngaro, italiano, xaponés, coreano,
  nepalés, polaco, portugués (Brasil), ruso, eslovaco, esloveno, español,
  Tamil e turco.

## Cambios para 2.1 ##

* Actualizada dependencia sutil á versión 0.6.1.
* Correxido retraso grande ó opter información das unidades.
* Limpeza do Código.

## Cambios para 2.0 ##

* Engadido o soporte para traduccións e comentarios das traduccións.

## Cambios para 1.0 ##

* Versión inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
