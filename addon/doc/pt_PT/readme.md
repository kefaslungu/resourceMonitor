# Monitor de Recursos #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst and other NVDA contributors
* Baixar [versão estável][1]
* NVDA compatibility: 2019.3 to 2020.4

Este extra fornece informações sobre carga da CPU, uso de memória e outras
informações de uso de recursos.

# Teclas de atalho: #

* NVDA+Shift+E: presents used ram, average processor load, and battery info
  if available.
* NVDA+Shift+1: presents the average processor load and if multicore CPU's
  are present the load of each core.
* NVDA+Shift+2/5: presents the used and total space for both physical and
  virtual ram.
* NVDA+Shift+3: presents the used and total space of the static and
  removable drives.
* NVDA+Shift+4: presents battery percentage, charging status, remaining time
  (if not charging), and a warning if the battery is low or critical.
* NVDA+Shift+6: presents CPU Architecture 32/64-bit and Windows version and
  service pack numbers.
* NVDA+Shift+7: presents the system's uptime.

If you have NVDA 2013.3 or later installed, you can change these shortcut
keys via input gestures dialog.

## Notas de utilização: ##

Este extra não substitui o gestor de tarefas e outros programas de
informações do sistema para o Windows. Observe também o seguinte:

* O uso da CPU é dado para processadores lógicos, e não para núcleos
  físicos. Isso é notável para os processadores que usam o Hyper-Threading,
  onde o número de CPU é o dobro do número de núcleos da CPU.
* Se houver uma grande actividade do disco, como copiar ficheiros grandes,
  pode haver atrasos ao obter informações de uso do disco.
* This add-on requires Windows 7 Service Pack 1 or later.

## Version 20.09

* System uptime is now given as days, hours, minutes, seconds.
* Windows Server Insider Preview build 20201 or later is properly recognized
  as a Server Insider build.

## Version 20.07

* Windows 10 Version 20H2 is properly recognized when obtaining Windows
  version information (NVDA+Shift+6).
* Simplified Windows 10 version message i.e. Windows 10 YYMM instead of
  Windows 10verYYMM when pressing NVDA+Shift+6.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Updated psutil dependency to 5.7.0.

## Version 20.01

* NVDA 2019.3 or later is required due to extensive use of Python 3.

## Version 19.11

* Improved detection of Windows Insider Preview builds, especially for 20H1
  and beyond.

## Version 19.07

* Updated psutil dependency to 5.6.3.
* Internal changes to battery status announcement command.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.10

* Code has been made more compatible with Python 3.
* Updated psutil dependency to 5.4.7.
* When obtaining disk capacity and memory usage, NVDA will no longer give
  errors if using a computer or a service with more than a petabyte of RAM
  or disk size.
* Values for memory and disk usage are shown with up to two decimal places
  (e.g. 4.00 GB instead of 4.0 GB).
* Improved detection of Windows Insider Preview builds.

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

## Mudanças para 4.5 ##

* O repositório do extra foi movido para o GitHub (pode ser encontrado em
  https://github.com/josephsl/resourcemonitor).
* O Windows Server 2016 é devidamente reconhecido.

## Alterações para 4.0 ##

* Dependência psutil actualizada para 2.2.1.
* Melhorado o desempenho na rapidez ao obter informações sobre a carga da
  CPU.
* Adicionado suporte para o reconhecimento do Windows 10.
* No Windows 10, o número de compilação do Windows também será anunciado.
* Agora, pode usar o gestor de extras para obter ajuda.

## Mudanças para 3.1 ##

* O monitor de recursos passou a suportar oficialmente o Windows 8.1.
* Traduções actualizadas

## Alterações para 3.0 ##

* Dependência psutil actualizada para 1.2.1.
* Anúncio da versão actual do Windows, arquitetura da CPU e pacote de
  serviço, se houver (NVDA + Shift + 6).
* Possibilidade de alterar as teclas de atalho do add-on (NVDA 2013.3 ou
  posterior).
* Capacidade de copiar informações de recursos individuais para a área de
  transferência ao pressionar os comandos de recursos duas vezes.

## Mudanças para 2.4 ##

* Novos idiomas: chinês (simplificado), ucraniano.
* Traduções actualizadas

## Alterações para 2.3 ##

* Adicionada a tradução búlgara.

## Mudanças para 2.2 ##

* Adicionadas as seguintes traduções: árabe, aragonês, croata, holandês,
  finlandês, francês, galego, alemão, húngaro, italiano, japonês, coreano,
  nepalês, polaco, português (Brasil), russo, eslovaco, esloveno, espanhol,
  tâmil e turco.

## Mudanças para 2.1 ##

* Dependência psutil actualizada para a versão 0.6.1.
* Corrigido grande atraso ao obter informações de unidades.
* Limpeza de códigoCode cleanup.

## Mudanças para 2.0 ##

* Foi adicionado o Suporte de tradução e respectivos comentários.

## Alterações para 1.0 ##

* Lançamento inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
