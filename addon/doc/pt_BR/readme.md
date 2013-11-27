# Monitor de recursos #

* Autores: Alex Hall, Joseph Lee, beqa gozalishvili e outros colaboradores
  do NVDA
* Versão estável: [versão 2.4][1]
* Versão de desenvolvimento: [versão 3.0-dev][2]

Este plug-in fornece informações acerca de carga da CPU, uso de memória e
status de uso da bateria e do disco.

# Atalhos #

* NVDA+Shift+E mostra uso da RAM, carga média do processador e informações
  de bateria caso disponíveis,
* NVDA+Shift+1 Mostra a carga média do processador e a carga de cada núcleo,
* NVDA+Shift+2/5 Mostra espaço usado e total de ambas memórias física e
  virtual,
* NVDA+Shift+3 Mostra espaço usado e total das unidades fixas e removíveis
  do computador,
* NVDA+Shift+4 Mostra porcentagem da bateria, status de carga, tempo
  restante (se não estiver carregando) e alerta caso a bateria esteja baixa
  ou crítica,
* NVDA+Shift+6 apresenta a versão de Windows atualmente instalada, bits da
  CPU (32 ou 64-bit) e o service pack se houver (versão 3.0-dev).

## Notas de uso ##

Este complemento não substitui o gerenciador de tarefas e outros programas
de informações de sistema para Windows. Note também o seguinte:

* O uso de CPU é fornecido em processadores lógicos e não em núcleos
  físicos. Nota-se isso em processadores que usam Hyper-Threading em que o
  número de CPUs é o dobro do número de núcleos de CPU.
* There might be a short delay when getting processor usage information.

## Mudanças na 3.0-dev ##

* Updated psutil dependency to 1.2.1.
* Adicionado um comando (NVDA+Shift+6) para anunciar a versão de Windows
  sendo usada, bits da CPU e o service packs se houver.
* Capacidade de alterar as teclas de atalho do complemento (NVDA 2.13.3 ou
  superior).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## Mudanças na 2.4 ##

* Novos idiomas: Chinês (simplificado), Ucraniano.
* Atualizadas traduções.

## Mudanças na 2.3 ##

* Adicionada tradução Búlgara.

## Mudanças na 2.2 ##

* Acrescentadas as seguintes traduções: Árabe, Alemão, Aragonês, Coreano,
  Croata, Eslovaco, Esloveno, Espanhol, Finlandês, Francês, Gálata,
  Holandês, Húngaro, Japonês, Italiano, Nepalês, Português (Brasil), Russo,
  Tâmil e Turco.

## Mudanças na 2.1 ##

* Atualizada dependência psutil para versão 0.6.1.
* Corrigida lentidão ao obter informações sobre unidades de disco.
* Substituídos %ss por {nomesAmigáveisDeVariáveis}.
* Ligeiro enxugamento de código

## Mudanças na 2.0 ##

* Adicionado suporte a traduções e comentários para tradutores.

## Mudanças na 1.0 ##

* Primeira versão

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
