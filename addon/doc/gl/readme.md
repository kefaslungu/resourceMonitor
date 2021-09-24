# Resource Monitor #

* Autores: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala e outros
  colaboradores do NVDA
* Descargar [versión estable][1]
* Compatibilidade con NVDA: 2021.1 en diante

Este plugin danos información acerca da carga da CPU, do uso da memoria e
outras informacións de uso dos recursos.

# Atallos de teclado

* NVDA+Shift+E: presenta a ram utilizada, a carga media do procesador, e
  información da batería se está dispoñible.
* NVDA+Shift+1: presenta a carga media do procesador e CPU multicor se están
  presentes a carga de cada núcleo.
* NVDA+Shift+2/5: presenta o espazo utilizado e total da ram tanto física
  coma virtual.
* NVDA+Shift+3: presenta o espazo usado e total das unidades estáticas e
  extraíbles .
* NVDA+Shift+4: presenta a porcentaxe da batería, o estado da carga, o tempo
  restante (se non se está a cargar), e un aviso se a batería está débil ou
  crítica.
* NVDA+Shift+6: presenta a arquitectura da CPU 32/64 bits e a versión de
  Windows e os números de service pack.
* NVDA+Shift+7: presenta o tempo de actividade do sistema.

Se tes NVDA 2013.3 ou posterior instalado, podes cambiar estas teclas de
atallo mediante o diálogo de xestos de entrada.

## Notas de uso

Este complemento non substitúe ó xestor de tarefas e a outros programas de
información do sistema para Windows. Ademais, ten en conta o seguinte:

* O Uso da CPU dase para os procesadores lóxicos, non para os núcleos
  físicos. Isto é perceptible para os procesadores que usan Hyper Threading
  onde o número de CPUs é o dobre do número de núcleos de CPU.
* Se hai unha actividade pesada de disco coma o copiado de ficheiros longos,
  podería haber retrasos ao obter información de uso do disco.
* Este complemento require Windows 7 Service Pack 1 ou posterior.

Nota sobre a licenza: este complemento utiliza Psutil, licenciado baixo a
3-Clause BSD License que é compatible coa GNU General Public License.

## Versión 21.10

* Requírese NVDA 2021.2 ou posterior debido a cambios en NVDA que afectan a
  este complemento.

## Versión 21.08

* O requerimento de versión mínima de Windows agora está vinculado ás
  versións de NVDA.
* As compilacións 20348 e 22000 de windows recoñécense como Windows Server
  2022 e Windows 11, respectivamente.
* Nas compilacións Insider Preview, a publicación de Windows como "Windows
  10" non se usará. No seu lugar, NVDA anunciará "windows Insider".
* En sistemas de 64 bits, a arquitectura do procesador (x64 ou ARM64)
  anunciarase como parte da información da versión de Windows.

## Versión 21.04

* Requírese NVDA 2020.4 ou posterior.
* Actualizada a dependencia psutil á 5.8.0.
* Ó premer ordes do complemento dúas veces para copiar a informacion do
  recurso ó portapapeis, NVDA anunciará o resumo do recurso que se está a
  copiar.

## Versión 21.01

* Actualizada a dependencia psutil á 5.7.3.
* Encurtada a mensaxe de versión de Windows.
* En Windows 8.1, compilación.revisión anunciarase como parte da mensaxe de
  versión de windows, de xeito similar a Windows 10.

## Versión 20.09

* O tempo de actividade do sistema agora proporciónase en días, horas,
  minutos, segundos.
* A compilación 20201 de Insider Preview para Windows Server ou posterior
  recoñécese correctamente como unha compilación Insider de Server.

## Versión 20.07

* Recoñécese axeitadamente a versión 20H2 de Windows 10 ao obter a
  información de versión de Windows (NVDA+Shift+6).
* Simplificada a mensaxe de versión de Windows 10, p.ex. Windows 10 AAMM no
  canto de Windows 10verAAMM, ao premer NVDA+Shift+6.

## Versión 20.06

* Resoltas varias incidencias de estilo do código e erros potenciais con
  Flake8.

## Versión 20.04

* Actualizada a dependencia psutil á 5.7.0.

## Versión 20.01

* Requírese NVDA 2019.3 ou posterior debido ó uso extensivo de Python 3.

## Versión 19.11

* Mellorada a detección de compilacións Windows Insider Preview,
  especialmente para 20H1 e posteriores.

## Versión 19.07

* Actualizada a dependencia psutil á 5.6.3.
* Cambios internos ao comando de anunciado do estado da batería.

## Versión 18.12

* Cambios internos para soportar versións futuras do NVDA.

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

## Cambios para 4.5

* O repositorio do complemento moviuse a GitHub (pode atoparse en
  https://github.com/josephsl/resourcemonitor).
* Recoñécese apropriadamente Windows Server 2016.

## Cambios para 4.0

* Actualizado psutil dependency a 2.2.1.
* Mellorado enormemente o rendemento ó obter información na carga da CPU.
* Engadido soporte para o recoñecemento do Windows 10.
* En Windows 10, tamén se anunciará o número de compilación do Windows.
* Podes ir o Administrador de Complementos para acceder á axuda do
  complemento.

## Cambios para 3.1

* Resource Monitor soporta oficialmente Windows 8.1.
* Actualízanse as traduccións.

## Cambios para 3.0

* Actualizada dependencia psutil para 1.2.1.
* Anuncio da versión actual de Windows, arquitectura da CPU e do service
  pack se o hai(NVDA+Shift+6).
* Capacidade de cambiar os atallos de teclado do complemento (NVDA 2.013,3
  ou posterior).
* Habilidade para copiar información dun recurso individual ó portapapeis
  premendo Ordes de recurso dúas veces.

## Cambios para 2.4

* Novas linguas: Chinese (simplificado), Ucranián.
* Actualízanse as traduccións.

## Cambios para 2.3

* Engadida a traducción ó búlgaro.

## Cambios para 2.2

* Seguintes traducións Engadidas: Árabe, aragonés, croata, holandés,
  finlandés, francés, galego, alemán, húngaro, italiano, xaponés, coreano,
  nepalés, polaco, portugués (Brasil), ruso, eslovaco, esloveno, español,
  Tamil e turco.

## Cambios para 2.1

* Actualizada dependencia sutil á versión 0.6.1.
* Correxido retraso grande ó opter información das unidades.
* Limpeza do Código.

## Cambios para 2.0

* engadido o soporte para traduccións e comentarios das traduccións.

## Cambios para 1.0

* Versión inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
