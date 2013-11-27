# resource Monitor #

* Autores: Alex Hall, Joseph Lee, beqa gozalishvili e outros colaboradores
  do NVDA
* Stable version: [versión 2.4][1]
* Versión de desenrolo: [versión 3.0-dev] [2]

Este plugin danos información acerca da carga da CPU, do uso da memoria, da
batería e do estado de uso do disco.

# Atallos de teclado #

* NVDA+Shift+E Presenta a ram utilizada, a carga media do procesador, e
  información da batería se está dispoñible,
* NVDA+Shift+1 Presenta a carga media do procesador e a carga de cada un dos
  núcleos,
* NVDA+Shift+2/5 Presenta o espazo utilizado e total da ram tanto física
  coma virtual,
* NVDA+Shift+3 Presenta o espazo usado e total das unidades estáticas e
  extraíbles  neste computador,
* NVDA+Shift+4 Presenta a porcentaxe da batería, o estado da carga, o tempo
  restante (se non se está cargando), e unha advertencia se a batería está
  baixa ou crítica,
* NVDA+Shift+6 Presenta a versión do Windows actualmente instalado, os bits
  da CPU (32 ou 64 bits) e service pack se o hai (versión 3.0-dev).

## Notas de uso ##

Este complemento non substitúe ó xestor de tarefas e a outros programas de
información do sistema para Windows. Ademais, ten en conta o seguinte:

* O Uso da CPU dase para os procesadores lóxicos, non para os núcleos
  físicos. Isto é perceptible para os procesadores que usan Hyper Threading
  onde o número de CPUs é o dobre do número de núcleos de CPU.
* Podería haber un pequeno retraso ó obter información sobre o uso do
  procesador.

## Cambios para 3.0-dev ##

* Actualizada dependencia psutil para 1.2.1.
* Engadidda unha orde (NVDA+Shift+6) para informar da versión do Windows que
  estás a usar, bits da CPU e service packs se os hai.
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

* Engadidas as seguintes traduccións: Alemán, Aragonés, Coreán, Croata,
  Eslovaco, Esloveno, Español, Finés, Francés, Galego, Holandés, Húngaro,
  Italiano, Nepalí, Portugués (Brasil), Ruso, Tamil e Turco.

## Cambios para 2.1 ##

* Actualizada dependencia sutil á versión 0.6.1.
* Correxido retraso grande ó opter información das unidades.
* Sustituido %s-es en {friendlyVariableNames}.
* Unha pequena limpeza do código

## Cambios para 2.0 ##

* Engadido o soporte para traduccións e comentarios das traduccións.

## Cambios para 1.0 ##

* Versión inicial

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
