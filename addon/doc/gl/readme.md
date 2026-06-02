# Resource Monitor

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst and other NVDA contributors

Este plugin danos información acerca da carga da CPU, do uso da memoria e outras informacións de uso dos recursos.

## Atallos de teclado

All commands support speech on demand mode.

* NVDA+Shift+E: presenta a ram utilizada, a carga media do procesador, e información da batería se está dispoñible.
* NVDA+Shift+1: presenta a carga media do procesador e CPU multicor se están presentes a carga de cada núcleo.
* NVDA+Shift+2/5: presenta o espazo utilizado e total da ram tanto física coma virtual.
* NVDA+Shift+3: presenta o espazo usado e total das unidades estáticas e extraíbles .
* NVDA+Shift+4: presenta a porcentaxe da batería, o estado da carga, o tempo restante (se non se está a cargar), e un aviso se a batería está débil ou crítica.
* NVDA+Shift+6: Presenta a arquitectura da CPU e a versión de Windows e os números de service pack.
* NVDA+Shift+7: presenta o tempo de actividade do sistema.
* NVDA+Shift+8: presents information on the wireless connection, ssid name and strength, or no ssid if there is none available.

Podes cambiar estas teclas de atallo mediante o diálogo de xestos de entrada.

## Notas de uso

Este complemento non substitúe ó xestor de tarefas e a outros programas de información do sistema para Windows. Ademais, ten en conta o seguinte:

* A información de recursos non se pode copiar ó portapapeis cando se executa o complemento en pantallas seguras.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* Se hai unha actividade pesada de disco coma o copiado de ficheiros longos, podería haber retrasos ao obter información de uso do disco.
* Ó anunciar a información sobre a arquitectura do procesador, "x86" e "AMD64" refírense a procesadores Intel e AMD de, respectivamente, 32 e 64 bits.
* This add-on requires Windows 10 22H2 (2022 Update/build 19045) or later.
* Installing the add-on on Windows 10/11 LTSC is not supported.
