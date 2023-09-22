# Monitor de Recursos #

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst and other NVDA contributors
* Baixar [versão estável][1]
* NVDA compatibility: 2022.4 and later

Este extra fornece informações sobre carga da CPU, uso de memória e outras
informações de uso de recursos.

# Teclas de atalho:

* NVDA+Shift+E apresenta A memória ram usada, a carga média do processador e
  as informações da bateria, se disponíveis.
* NVDA+Shift+1: apresenta a carga média do processador e se estiverem
  presentes CPU's com vários núcleos, a carga de cada núcleo.
* NVDA+Shift+2/5: apresenta o espaço utilizado e o espaço total tanto para a
  memória  física como para a virtual.
* NVDA+Shift+3 Apresenta o espaço usado e total das unidades estáticas e
  removíveis.
* NVDA+Shift+4 Apresenta a percentagem da bateria, o estado da carga, o
  tempo restante (se não estiver a carregar) e um aviso se a bateria estiver
  fraca ou crítica.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service
  pack numbers.
* NVDA+Shift+7 apresenta o tempo de actividade do sistema.
* NVDA+Shift+8: presents information on the wireless connection, ssid name
  and strength, or no ssid if there is none available.

You can change these shortcut keys via input gestures dialog.

## Notas de utilização:

Este extra não substitui o gestor de tarefas e outros programas de
informações do sistema para o Windows. Observe também o seguinte:

* Resource information cannot be copied to clipboard if running the add-on
  in secure screens.
* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores. On some newer computers, not all CPU
  cores will have hyper-threading enabled.
* Se houver uma grande actividade do disco, como copiar ficheiros grandes,
  pode haver atrasos ao obter informações de uso do disco.
* When announcing processor architecture information, "x86" and "AMD64"
  refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 or later.

Note on license: this add-on uses Psutil, licensed under 3-Clause BSD
License which is compatible with GNU General Public License.

## Version 23.09

* NVDA will no longer log startup error messages on Windows Server systems
  when wireless capability modules are unavailable.

## Version 23.06

* Situation where resourceMonitor doesn't work properly due to
  unavailability of wireless adapters has been fixed.

## Version 23.05.1

wlanReporter NVDA-addon is now part of resourceMonitor!

* The old way of checking for wireless connections has been replaced by the
  windows API from wlanReporter: https://github.com/kvark128/WlanReporter/ .

	* After speaking SSID name and strength, NVDA will also now tell you the
	  security type of your network.
	* NVDA will now alert you when you connect and disconnect from a wireless
	  network.
	* NVDA will now alert you when wireless connections is turned on or off.

## Version 23.05

* added the ability to detect and present the state of the connected
  wireless network.

	* Announces the name of the connected wireless SSID.
	* Announces the strength of the ssid
	* Announce SSID not found if None is detected.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.
* Updated psutil dependency to 5.9.4.
* NVDA will announce actual processor architecture (x86/AMD64/ARM64) as part
  of Windows version information.
* On single-core systems, NVDA will no longer announce CPU core load as
  average CPU load is the same as core load.

## Version 22.03

Version 22.03 is the last stable version to support Windows 7 Service Pack
1, 8, and 8.1.

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on
  on Windows 7, 8, and 8.1.
* Updated psutil dependency to 5.9.0.

## Version 22.01

* NVDA 2021.2 or later is required.

## Version 21.10

* NVDA 2021.1 or later is required due to changes to NVDA that affects this
  add-on.

## Version 21.08

* Minimum Windows release requirement is now tied to NVDA releases.
* Windows builds 20348 and 22000 are recognized as Windows Server 2022 and
  Windows 11, respectively.
* On Insider Preview builds, Windows release such as "Windows 10" will not
  be used. Instead NvDA will announce "Windows Insider".
* On 64-bit systems, processor architecture (x64 or ARM64) will be announced
  as part of Windows version information.

## Versão 21.04

* A versão do  NVDA 2020.4 ou posterior é necessária.
* Dependência psutil actualizada para 5.8.0.
* Ao pressionar duas vezes comandos adicionais para copiar informações de
  recursos para a área de transferência, o NVDA anunciará o resumo dos
  recursos que estão a ser copiados.

## Versão 21.01

* Dependência psutil actualizada para 5.7.3.
* Mensagem abreviada da versão do Windows.
* No Windows 8.1, build.revision será anunciado como parte da mensagem da
  versão Windows, como no Windows 10.

## Versão 20.09

* O tempo de funcionamento do sistema é agora dado em dias, horas, minutos e
  segundos.
* O Windows Server Insider Preview build 20201 ou posterior é devidamente
  reconhecido como um Servidor Insider build.

## Versão 20.07

* A versão 20H2 do Windows 10 é devidamente reconhecida ao obter a
  informação da versão do Windows (NVDA+Shift+6).
* Mensagem de versão simplificada do Windows 10, ou seja, Windows 10 YYYMM
  em vez de Windows 10verYYYMM ao premir NVDA+Shift+6.

## Versão 20.06

* Resolvidos vários problemas de estilo de codificação e potenciais bugs com
  Flake8.

## Versão 20.04

* Dependência psutil actualizada para 5.7.0.

## Versão 20.01

* O NVDA 2019.3 ou posterior é necessário devido à utilização extensiva de
  Python 3.

## Versão 19.11

* Improved detection of Windows Insider Preview builds, especially for 20H1
  and beyond.

## Version 19.07

* Updated psutil dependency to 5.6.3.
* Internal changes to battery status announcement command.

## Version 18.12

* Internal changes to support future NVDA releases.

## Versão 18.10

* O código foi tornado mais compatível com python3.
* Dependência psutil actualizada para 5.4.7.
* Ao obter a capacidade de disco e o uso de memória, o NVDA não mais causará
  erros se estiver a usar um computador ou um serviço com mais de um
  petabyte de RAM ou tamanho de disco.
* Os valores para uso de memória e disco são mostrados com até duas casas
  decimais (por exemplo, 4,00 GB em vez de 4,0 GB).
* Detecção aprimorada de construções do Windows Insider Preview.

## Versão 18.04

A versão 18.04.x é a última versão a suportar versões anteriores ao Windows
7 SP1.

* Última versão para suporte ao Windows Server 2003, Vista e Server 2008.
* Melhor detecção de versões do Windows 10 e distinção entre versões
  públicas e beta privadas.

## Versão 17.12

* Adicionado suporte para processadores ARM de 64 bits no Windows 10.

## Versão 17.09

Importante: a versão 17.09.x é a última versão a suportar o Windows XP.

* Última versão para executar no Windows XP.
* O Windows 10 build 16278 e posterior é reconhecido como a Versão 1709. Uma
  revisão menor para este extra será lançada logo que a versão estável da
  versão 1709 seja lançada.

## Versão 17.07.1

* Reintroduz o suporte para o Windows XP (quebrado desde a versão 17.02).

## Versão 17.05

* Anúncio do tempo de actividade do sistema (tempo passado desde a última
  inicialização, NVDA + Shift + 7).

## Versão 17.02

* Dependência psutil actualizada para 5.0.1.
* Ao verificar o uso do disco, o NVDA deixará de apresentar uma caixa de
  diálogo de erro em alguns sistemas onde uma mídia removível não está
  devidamente reconhecida (como, por exemplo, quando um cartão não está
  inserido em um leitor de cartão).

## Versão 16.08

A partir da versão 16.08, os lançamentos adicionais serão mostrados como
ano.mês.revisão.

* Várias revisões do Windows 10 agora são devidamente reconhecidas (como a
  1607 para a compilação 14393).
* As revisões de compilação do Windows 10 (após a instalação de
  actualizações cumulativas) são devidamente reconhecidas (como a 14393.51).
* Se estiver usando versões de Insider Preview, esse fato é reconhecido.

## Mudanças para 4.5

* O repositório do extra foi movido para o GitHub (pode ser encontrado em
  https://github.com/josephsl/resourcemonitor).
* O Windows Server 2016 é devidamente reconhecido.

## Alterações para 4.0

* Dependência psutil actualizada para 2.2.1.
* Melhorado o desempenho na rapidez ao obter informações sobre a carga da
  CPU.
* Adicionado suporte para o reconhecimento do Windows 10.
* No Windows 10, o número de compilação do Windows também será anunciado.
* Agora, pode usar o gestor de extras para obter ajuda.

## Mudanças para 3.1

* O monitor de recursos passou a suportar oficialmente o Windows 8.1.
* Traduções actualizadas

## Alterações para 3.0

* Dependência psutil actualizada para 1.2.1.
* Anúncio da versão actual do Windows, arquitetura da CPU e pacote de
  serviço, se houver (NVDA + Shift + 6).
* Possibilidade de alterar as teclas de atalho do add-on (NVDA 2013.3 ou
  posterior).
* Capacidade de copiar informações de recursos individuais para a área de
  transferência ao pressionar os comandos de recursos duas vezes.

## Mudanças para 2.4

* Novos idiomas: chinês (simplificado), ucraniano.
* Traduções actualizadas

## Alterações para 2.3

* Adicionada a tradução búlgara.

## Mudanças para 2.2

* Adicionadas as seguintes traduções: árabe, aragonês, croata, holandês,
  finlandês, francês, galego, alemão, húngaro, italiano, japonês, coreano,
  nepalês, polaco, português (Brasil), russo, eslovaco, esloveno, espanhol,
  tâmil e turco.

## Mudanças para 2.1

* Dependência psutil actualizada para a versão 0.6.1.
* Corrigido grande atraso ao obter informações de unidades.
* Limpeza de códigoCode cleanup.

## Mudanças para 2.0

* Foi adicionado o Suporte de tradução e respectivos comentários.

## Alterações para 1.0

* Lançamento inicial

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
