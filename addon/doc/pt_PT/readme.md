# Monitor de Recursos

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst and other NVDA contributors

Este extra fornece informações sobre carga da CPU, uso de memória e outras informações de uso de recursos.

## Teclas de atalho:

All commands support speech on demand mode.

* NVDA+Shift+E apresenta A memória ram usada, a carga média do processador e as informações da bateria, se disponíveis.
* NVDA+Shift+1: apresenta a carga média do processador e se estiverem presentes CPU's com vários núcleos, a carga de cada núcleo.
* NVDA+Shift+2/5: apresenta o espaço utilizado e o espaço total tanto para a memória  física como para a virtual.
* NVDA+Shift+3 Apresenta o espaço usado e total das unidades estáticas e removíveis.
* NVDA+Shift+4 Apresenta a percentagem da bateria, o estado da carga, o tempo restante (se não estiver a carregar) e um aviso se a bateria estiver fraca ou crítica.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service pack numbers.
* NVDA+Shift+7 apresenta o tempo de actividade do sistema.
* NVDA+Shift+8: presents information on the wireless connection, ssid name and strength, or no ssid if there is none available.

You can change these shortcut keys via input gestures dialog.

## Notas de utilização:

Este extra não substitui o gestor de tarefas e outros programas de informações do sistema para o Windows. Observe também o seguinte:

* Resource information cannot be copied to clipboard if running the add-on in secure screens.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* Se houver uma grande actividade do disco, como copiar ficheiros grandes, pode haver atrasos ao obter informações de uso do disco.
* When announcing processor architecture information, "x86" and "AMD64" refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 22H2 (2022 Update/build 19045) or later.
* Installing the add-on on Windows 10/11 LTSC is not supported.
