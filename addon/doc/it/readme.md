# Resource Monitor

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst and other NVDA contributors

Questo componente aggiuntivo fornisce informazioni sulle prestazioni di sistema, quali carico della CPU, utilizzo della memoria e molto altro.

## Tasti rapidi

All commands support speech on demand mode.

* NVDA+Shift+E: fornisce informazioni sulla quantità di ram utilizzata, sul carico medio della cpu e sulla batteria, se disponibile.
* NVDA+Shift+1: Fornisce informazioni sul carico medio delle CPU e, se sono presenti processori multicore, informazioni dettagliate sul carico di ciascuna CPU presente nel sistema.
* NVDA+Shift+2/5: Fornisce informazioni sulla quantità di Ram fisica e virtuale utilizzata e totale.
* NVDA+Shift+3: riporta la dimensione totale e la percentuale di utilizzo delle unità disco locali e rimovibili.
* NVDA+Shift+4: riporta la percentuale di carica della batteria, lo stato di carica, il tempo rimanente (se non in carica), e un messaggio di avviso se la carica è bassa o molto bassa.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service pack numbers.
* NVDA+Shift+7 riporta il tempo di attività del sistema.
* NVDA+Shift+8: presents information on the wireless connection, ssid name and strength, or no ssid if there is none available.

You can change these shortcut keys via input gestures dialog.

## Note d'utilizzo

Questo componente aggiuntivo non sostituisce applicazioni quali Task Manager o altri software che forniscono informazioni di sistema per Windows. Inoltre si tenga presente che:

* Resource information cannot be copied to clipboard if running the add-on in secure screens.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* Se è in corso un notevole processo sul disco, come ad esempio la copia di file di grandi dimensioni, ci potrebbero essere dei ritardi nell'ottenere informazioni sull'utilizzo del disco.
* When announcing processor architecture information, "x86" and "AMD64" refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 22H2 (2022 Update/build 19045) or later.
* Installing the add-on on Windows 10/11 LTSC is not supported.
