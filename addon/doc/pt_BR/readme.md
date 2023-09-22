# Monitor de Recursos (Resource Monitor) #

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst and other NVDA contributors
* Baixe a [versão estável][1]
* NVDA compatibility: 2022.4 and later

Este complemento fornece informações sobre carga da CPU, uso de memória e
outras informações de uso de recursos.

# Atalhos

* NVDA+Shift+E: apresenta uso da ram (memória), carga média do processador,
  e informações de bateria caso disponível.
* NVDA+Shift+1: apresenta a carga média do processador e caso se tratem de
  CPUs multinúcleo (multicore) mostra a carga de cada núcleo.
* NVDA+Shift+2/5: apresenta espaço usado e total das memórias ram física e
  virtual.
* NVDA+Shift+3: apresenta espaço usado e o total das unidades fixas e
  removíveis.
* NVDA+Shift+4: apresenta porcentagem da bateria, status de carga, tempo
  restante (se não estiver carregando) e alerta caso a bateria esteja baixa
  ou crítica.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service
  pack numbers.
* NVDA+Shift+7: apresenta o tempo de atividade do sistema (tempo desde a
  inicialização).
* NVDA+Shift+8: presents information on the wireless connection, ssid name
  and strength, or no ssid if there is none available.

You can change these shortcut keys via input gestures dialog.

## Notas de uso

Este complemento não substitui o gerenciador de tarefas e outros programas
de informações de sistema para Windows. Note também o seguinte:

* Resource information cannot be copied to clipboard if running the add-on
  in secure screens.
* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores. On some newer computers, not all CPU
  cores will have hyper-threading enabled.
* Se houver atividade intença de disco, como ao copiar arquivos grandes,
  pode haver lentidão ao obter informações de uso do disco.
* When announcing processor architecture information, "x86" and "AMD64"
  refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 or later.

Nota sobre a licença: este complemento usa Psutil, licenciado sob a Licença
BSD de 3 cláusulas, que é compatível com a GNU General Public License.

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

## Versão 22.01

* Requer NVDA 2021.2 ou posteriores.

## Versão 21.10

* O NVDA 2021.2 ou posterior é necessário devido a mudanças no NVDA que
  afetam este complemento.

## Versão 21.08

* O requisito mínimo de versão do Windows agora está vinculado às versões do
  NVDA.
* As compilações do Windows 20348 e 22000 são reconhecidas como Windows
  Server 2022 e Windows 11, respectivamente.
* Nas compilações do Insider Preview, a versão do Windows, como "Windows
  10", não será usada. Em vez disso, o NvDA anunciará "Windows Insider".
* Em sistemas de 64-bit, a arquitetura do processador (x64 ou ARM64) será
  anunciada como parte das informações de versão do Windows.

## Versão 21.04

* Requer NVDA 2020.4 ou posterior.
* Atualizada dependência psutil para 5.8.0.
* Ao pressionar duas vezes os comandos do complemento para copiar a
  informação do recurso para a área de transferência, o NVDA anunciará o
  resumo do recurso que está sendo copiado.

## Versão 21.01

* Atualizada dependência psutil para 5.7.3.
* Mensagem encurtada da versão do Windows.
* No Windows 8.1, compilação.revisão será anunciado como parte da mensagem
  da versão do Windows, semelhante ao Windows 10.

## Versão 20.09

* O tempo de atividade do sistema agora é dado em dias, horas, minutos,
  segundos.
* A compilação do Windows Server Insider Preview 20201 ou posterior é
  devidamente reconhecida como uma compilação do Server Insider.

## Versão 20.07

* O Windows 10 versão 20H2 é reconhecido corretamente ao obter informações
  sobre a versão do Windows (NVDA+Shift+6).
* Mensagem simplificada da versão do Windows 10, ou seja, Windows 10 AAMM em
  vez de Windows 10verAAMM ao pressionar NVDA+Shift+6.

## Versão 20.06

* Foram resolvidos muitos problemas de estilo de codificação e possíveis
  erros com o Flake8.

## Versão 20.04

* Atualizada dependência psutil para 5.7.0.

## Versão 20.01

* Requer NVDA 2019.3 ou posterior devido ao uso ostensivo de Python 3.

## Versão 19.11

* Melhorada detecção de compilações do Windows Insider Preview,
  especialmente a 20H1 e posteriores.

## Versão 19.07

* Atualizada dependência psutil para 5.6.3.
* Alterações internas do comando status da bateria.

## Versão 18.12

* Alterações internas para suportar futuras versões de NVDA.

## Versão 18.10

* O código ficou mais compatível com o Python 3.
* Atualizada dependência psutil para 5.4.7.
* Ao obter capacidade de disco e uso de memória, o NVDA não mais dará erros
  se estiver usando um computador ou um serviço com mais de um petabyte de
  RAM ou tamanho de disco.
* Os valores para uso de memória e disco são mostrados com até duas casas
  decimais (por exemplo, 4,00 GB em vez de 4,0 GB).
* Detecção aprimorada de compilações (builds) do Windows Insider Preview.

## Versão 18.04

Versão 18.04.x é a última versão a suportar versões anteriores ao Windows 7
SP1.

* Última versão para suporte ao Windows Server 2003, Vista e Server 2008.
* Melhor detecção de versões do Windows 10 e distinção entre compilações
  (builds) públicas e Insider Preview.

## Versão 17.12

* Adicionado suporte para processadores ARM 64-bit no Windows 10.

## Versão 17.09

Importante: A versão 17.09.x é a última versão que suporta o Windows XP.

* Última versão a executar em Windows XP.
* Windows 10 compilação 16278 e posteriores são reconhecidas como versão
  1709. Uma versão menor deste complemento será lançada assim que a
  compilação estável da versão 1709 for lançada.

## Versão 17.07.1

* Reintroduzido suporte a Windows XP (quebrado desde a versão 17.02).

## Versão 17.05

* Anúncio do tempo de atividade do sistema (o tempo passado desde a última
  inicialização; NVDA+Shift+7).

## Versão 17.02

* Atualizada dependência psutil para 5.0.1.
* Ao verificar o uso de discos, o NVDA não vai mais apresentar uma mensagem
  de erro em alguns sistemas onde uma mídia removível não é reconhecida
  apropriadamente (por exemplo quando um cartão não está inserido num leitor
  de cartões).

## Versão 16.08

Começando na versão 16.08, os lançamentos do complemento serão mostrados
como ano.mês.revisão.

* Agora são reconhecidas apropriadamente várias revisões do Windows 10 (ex.:
  1607 para a compilação 14393).
* Compilações revisadas do Windows 10 (após instalar atualizações
  cumulativas) são reconhecidas apropriadamente (exemplo, 14393.51).
* Se usando compilações Insider Preview, tal fato é reconhecido.

## Mudanças na 4.5

* Repositório do complemento movido para o GitHub (pode ser encontrado em
  https://github.com/josephsl/resourcemonitor).
* O Windows Server 2016 é reconhecido adequadamente.

## Mudanças na 4.0

* Atualizada dependência psutil para 2.2.1.
* Aprimorado largamente o desempenho ao obter informações de carga da CPU.
* Adicionado suporte ao reconhecimento de Windows 10.
* No Windows 10, o número de compilação também será anunciado.
* Você pode usar o gestor de complementos para acessar a ajuda do
  complemento.

## Mudanças na 3.1

* O Monitor de Recursos suporta oficialmente Windows 8.1.
* Atualizadas traduções.

## Mudanças na 3.0

* Atualizada dependência psutil para 1.2.1.
* Anunciar versão atual de Windows, arquitetura da CPU e service pack se
  houver (NVDA+Shift+6).
* Capacidade de alterar as teclas de atalho do complemento (NVDA 2.13.3 ou
  superior).
* Capacidade de copiar as informações dum recurso individual para a área de
  transferência pressionando duas vezes o comando do recurso.

## Mudanças na 2.4

* Novos idiomas: Chinês (simplificado), Ucraniano.
* Atualizadas traduções.

## Mudanças na 2.3

* Adicionada tradução Búlgara.

## Mudanças na 2.2

* Acrescentadas as seguintes traduções: Árabe, Alemão, Aragonês, Coreano,
  Croata, Eslovaco, Esloveno, Espanhol, Finlandês, Francês, Galego,
  Holandês, Húngaro, Japonês, Italiano, Nepalês, Português (Brasil), Russo,
  Tâmil e Turco.

## Mudanças na 2.1

* Atualizada dependência psutil para versão 0.6.1.
* Corrigida lentidão ao obter informações sobre unidades de disco.
* Enxugamento de código.

## Mudanças na 2.0

* adicionado suporte a traduções e comentários para tradutores.

## Mudanças na 1.0

* Versão Inicial

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
