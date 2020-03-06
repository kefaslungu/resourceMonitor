# Monitor de recursos #

* Autores: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst e outros colaboradores do NVDA
* Baixe a [versão estável][1]
* Compatibilidade com NVDA: 2019.3 e posteriores

Este complemento fornece informações sobre carga de CPU, uso de memória e
outras informações de uso de recursos.

# Atalhos #

* NVDA+Shift+E mostra uso da RAM, carga média do processador e informações
  de bateria caso disponíveis.
* NVDA+Shift+1 Mostra a carga média do processador e caso se tratem de CPUs
  multinúcleo mostra a carga de cada núcleo.
* NVDA+Shift+2/5 Mostra espaço usado e total das memórias RAM física e
  virtual.
* NVDA+Shift+3 Mostra espaço usado e o total das unidades fixas e
  removíveis.
* NVDA+Shift+4 Mostra porcentagem da bateria, status de carga, tempo
  restante (se não estiver carregando) e alerta caso a bateria esteja baixa
  ou crítica.
* NVDA+Shift+6 apresenta arquitetura da CPU (32/64-bit) e a versão de
  Windows com números do service pack.
* NVDA+Shift+7 apresenta o tempo desde a inicialização do sistema.

Caso tenha o NVDA 2013.3 ou posterior instalado, poderá alterar essas teclas
de atalho através do diálogo definir comandos (gestos de entrada).

## Notas de uso ##

Este complemento não substitui o gerenciador de tarefas e outros programas
de informações de sistema para Windows. Note também o seguinte:

* O uso de CPU é fornecido em processadores lógicos e não em núcleos
  físicos. Nota-se isso em processadores que usam Hyper-Threading, em que o
  número de CPUs é o dobro do número de núcleos de CPU.
* Se houver atividade intença de disco, como ao copiar arquivos grandes,
  pode haver lentidão ao obter informações de uso do disco.
* Este complemento requer Windows 7 Service Pack 1 ou posterior.

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
* Detecção aprimorada de construções — builds — do Windows Insider Preview.

## Versão 18.04

Versão 18.04.x é a última versão a suportar versões anteriores ao Windows 7
SP1.

* Última versão para suporte ao Windows Server 2003, Vista e Server 2008.
* Melhor detecção de versões do Windows 10 e distinção entre construções —
  builds — públicas e Insider Preview.

## Versão 17.12

* Adicionado suporte para processadores ARM 64-bit no Windows 10.

## Versão 17.09

Importante: A versão 17.09.x é a última versão que suporta o Windows XP.

* Última versão a rodar em Windows XP.
* Windows 10 compilação 16278 e posteriores são reconhecidos como versão
  1709. Uma versão menor deste complemento será lançada assim que a
  compilação estável da versão 1709 foi lançada.

## Versão 17.07.1

* Reintroduzido suporte a Windows XP (quebrado desde a versão 17.02).

## Versão 17.05

* Anúncio do tempo desde o início do sistema (o tempo passado desde a última
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
  cumulativas) são reconhecidas apropriadamente (ex. 14393.51).
* Se usando compilações Insider Preview, tal fato é reconhecido.

## Mudanças na 4.5 ##

* Repositório do complemento movido para o GitHub (pode ser encontrado em
  https://github.com/josephsl/resourcemonitor).
* O Windows Server 2016 é reconhecido adequadamente.

## Mudanças na 4.0 ##

* Atualizada dependência psutil para 2.2.1.
* Aprimorado largamente o desempenho ao obter informações de carga da CPU.
* Adicionado suporte ao reconhecimento de Windows 10.
* No Windows 10, o número de compilação também será anunciado.
* Você pode usar o gestor de complementos para acessar a ajuda do
  complemento.

## Mudanças na 3.1 ##

* O Monitor de Recursos suporta oficialmente Windows 8.1.
* Atualizadas traduções.

## Mudanças na 3.0 ##

* Atualizada dependência psutil para 1.2.1.
* Anunciar versão atual de Windows, arquitetura da CPU e service pack se
  houver (NVDA+Shift+6).
* Capacidade de alterar as teclas de atalho do complemento (NVDA 2.13.3 ou
  superior).
* Capacidade de copiar as informações dum recurso individual para a área de
  transferência pressionando duas vezes o comando do recurso.

## Mudanças na 2.4 ##

* Novos idiomas: Chinês (simplificado), Ucraniano.
* Atualizadas traduções.

## Mudanças na 2.3 ##

* Adicionada tradução Búlgara.

## Mudanças na 2.2 ##

* Acrescentadas as seguintes traduções: Árabe, Alemão, Aragonês, Coreano,
  Croata, Eslovaco, Esloveno, Espanhol, Finlandês, Francês, Galego,
  Holandês, Húngaro, Japonês, Italiano, Nepalês, Português do Brasil, Russo,
  Tâmil e Turco.

## Mudanças na 2.1 ##

* Atualizada dependência psutil para versão 0.6.1.
* Corrigida lentidão ao obter informações sobre unidades de disco.
* Enxugamento de código.

## Mudanças na 2.0 ##

* adicionado suporte a traduções e comentários para tradutores.

## Mudanças na 1.0 ##

* Primeira versão

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
