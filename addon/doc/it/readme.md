# Resource Monitor #

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst and other NVDA contributors
* Scarica la [versione stabile][1]
* NVDA compatibility: 2022.4 and later

Questo componente aggiuntivo fornisce informazioni sulle prestazioni di
sistema, quali carico della CPU, utilizzo della memoria e molto altro.

# Tasti rapidi

* NVDA+Shift+E: fornisce informazioni sulla quantità di ram utilizzata, sul
  carico medio della cpu e sulla batteria, se disponibile.
* NVDA+Shift+1: Fornisce informazioni sul carico medio delle CPU e, se sono
  presenti processori multicore, informazioni dettagliate sul carico di
  ciascuna CPU presente nel sistema.
* NVDA+Shift+2/5: Fornisce informazioni sulla quantità di Ram fisica e
  virtuale utilizzata e totale.
* NVDA+Shift+3: riporta la dimensione totale e la percentuale di utilizzo
  delle unità disco locali e rimovibili.
* NVDA+Shift+4: riporta la percentuale di carica della batteria, lo stato di
  carica, il tempo rimanente (se non in carica), e un messaggio di avviso se
  la carica è bassa o molto bassa.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service
  pack numbers.
* NVDA+Shift+7 riporta il tempo di attività del sistema.
* NVDA+Shift+8: presents information on the wireless connection, ssid name
  and strength, or no ssid if there is none available.

You can change these shortcut keys via input gestures dialog.

## Note d'utilizzo

Questo componente aggiuntivo non sostituisce applicazioni quali Task Manager
o altri software che forniscono informazioni di sistema per Windows. Inoltre
si tenga presente che:

* Resource information cannot be copied to clipboard if running the add-on
  in secure screens.
* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores. On some newer computers, not all CPU
  cores will have hyper-threading enabled.
* Se è in corso un notevole processo sul disco, come ad esempio la copia di
  file di grandi dimensioni, ci potrebbero essere dei ritardi nell'ottenere
  informazioni sull'utilizzo del disco.
* When announcing processor architecture information, "x86" and "AMD64"
  refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 or later.

Nota sulla licenza: questo componente aggiuntivo utilizza Psutil, concesso
con licenza 3-Clause BSD compatibile con GNU General Public License.

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

## Novità nella versione 21.10

* NVDA 2021.1 o successive sono richiesti per modifiche a NVDA che
  interessano questo componente aggiuntivo.

## Novità nella versione 21.08

* Il requisito minimo di rilascio di Windows è ora legato alle versioni di
  NVDA.
* Le build di Windows 20348 e 22000 sono riconosciute rispettivamente come
  Windows Server 2022 e Windows 11.
* Nelle build di Insider Preview, la versione di Windows come "Windows 10"
  non verrà utilizzata. NVDA annuncerà "Windows Insider".
* Sui sistemi a 64 bit, l'architettura del processore (x64 o ARM64) verrà
  annunciata come parte delle informazioni sulla versione di Windows.

## Novità nella versione 21.04

* E' richiesto NVDA 2020.4 o successive.
* Aggiornato psutil alla versione 5.8.0.
* Quando si premono due volte i comandi aggiuntivi per copiare le
  informazioni negli appunti, NVDA annuncerà il riepilogo delle informazioni
  copiate.

## Novità nella versione 21.01

* Aggiornato psutil alla versione 5.7.3.
* Messaggio abbreviato sulla versione di Windows.
* Su Windows 8.1, build.revision verrà annunciato come parte del messaggio
  di versione di Windows, simile a Windows 10.

## Novità nella versione 20.09

* Il tempo di attività del sistema è ora fornito come giorni, ore, minuti,
  secondi.
* Windows Server Insider Preview build 20201 o superiore è correttamente
  riconosciuto come una Server Insider build.

## Novità nella versione 20.07

* Windows 10 Versione 20H2 è riconosciuto correttamente quando si ottengono
  le informazioni sulla versione di Windows (NVDA+Shift+6).
* Semplificato il messaggio sulla versione di Windows: Windows 10 AAMM
  invece di Windows 10verAAMM quando si preme NVDA+Shift+6.

## Novità nella versione 20.06

* Risolti molti problemi con lo stile del codice e bug potenziali con
  Flake8.

## Novità nella versione 20.04

* Aggiornata la dipendenza psutil alla versione 5.7.0.

## Novità nella versione 20.01

* E' richiesto NVDA 2019.3 o superiore a causa dell'utilizzo massiccio di
  Python 3.

## Novità nella versione 19.11

* Migliorato il rilevamento delle  Windows Insider Preview builds, ,
  specialmente per le versioni 20H1 e superiori..

## Novità nella versione 19.07

* Aggiornata la dipendenza psutil alla versione 5.6.3.
* Modifiche interne al comando per la vocalizzazione dello stato della
  batteria.

## Novità nella versione 18.12

* Modifiche interne per supportare le future versioni di NVDA.

## Novità nella versione 18.10

* Il codice è stato reso più compatibile con Python 3.
* Aggiornata la dipendenza psutil alla versione 5.4.7.
* Nel ricavare la capacità del disco o della memoria in uso, NVDA non
  riporterà errori se si utilizza un computer o un servizio con più di un
  petabyte di RAM o di spazio disco.
* I valori per l'utilizzo della memoria e del disco sono indicati con un
  massimo di due cifre decimali (ad es. 4.00 GB invece di 4.0 GB).
* Migliorato il rilevamento delle Windows Insider Preview build.

## Novità nella versione 18.04

La versione 18.04.x è l'ultima release che supporta  le versioni precedenti
a Windows 7 SP1.

* Ultima versione che supporta Windows Server 2003, Vista e Server 2008.
* Miglior rilevamento delle versioni di Windows 10 e miglior distinzione tra
  le Public e Insider building.

## Novità nella versione 17.12

* Aggiunto il supporto per i processori ARM a 64 bit su Windows 10.

## Novità nella versione 17.09

Importante: la Versione 17.09.x è l'ultima versione che supporta Windows XP.

* Ultima versione per Windows XP.
* Windows 10 build 16278 e superiore è riconosciuta come Versione
  1709. Quando verrà rilasciata la versione stabile di Windows 10 1709,
  verrà rilasciato un aggiornamento minore per questo componente aggiuntivo.

## Novità nella versione 17.07.1

* Reintroduce il supporto per Windows XP (non funzionante dalla versione
  17.02).

## Novità nella versione 17.05

* Vocalizzazione dell'attività del sistema (il tempo trascorso dall'ultimo
  avvio; NVDA+Shift+7).

## Novità nella versione 17.02

* Aggiornata la dipendenza psutil alla versione 5.0.1.
* Quando si controlla l'utilizzo del disco, NVDA non mostrerà più una
  finestra di errore in alcuni sistemi, nei quali un'unità rimovibile non è
  riconosciuta correttamente (come quando una memory card non è inserita in
  un card reader).)

## Novità nella versione 16.08

A partire dalla versione 16.08, le versioni dell'add-on saranno mostrate
come anno.mese.revisione.

* Diverse revisioni di Windows 10 ora sono correttamente riconosciute (come
  la 1607 per la build 14393).
* Le build revisions di Windows 10 (dopo l'installazione di aggiornamenti
  cumulativi) sono riconosciute correttamente (ad esempio la 14393.51).
* Se si utilizzano le Insider Preview builds, questo fatto è riconosciuto.

## Novità nella versione 4.5

* Il repository dell'add-on è stato spostato su GitHub (lo si trova
  all'indirizzo https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 è riconosciuto correttamente.

## Novità nella versione 4.0

* Aggiornata la dipendenza psutil alla versione 2.2.1.
* Performance molto migliorate nell'acquisizione delle informazioni sul
  carico della CPU.
* Aggiunto il supporto al riconoscimento di Windows 10.
* In Windows 10, verrà anche vocalizzato il numero di build.
* Per accedere alla guida, si può utilizzare il gestore componenti
  aggiuntivi.

## Novità nella versione 3.1

* Resource Monitor supporta ufficialmente Windows 8.1.
* Traduzioni aggiornate.

## Novità nella versione 3.0

* Aggiornata la dipendenza psutil alla versione 1.2.1.
* Vocalizzazione della versione corrente di Windows, dell'architettura della
  CPU e del service pack se presente  (NVDA+Shift+6).
* Possibilità di cambiare i tasti rapidi dell'add-on (NVDA 2013.3 o
  superiore).
* Possibilità di copiare ciascuna informazione sulle risorse negli appunti
  digitando i comandi due volte.

## Novità nella versione 2.4

* Nuove lingue: Cinese (semplificato), Ucraino.
* Traduzioni aggiornate.

## Novità nella versione 2.3

* Aggiunta la traduzione in bulgaro.

## Novità nella versione 2.2

* Aggiunte le seguenti traduzioni: Arabo, Aragonese, Croato, Olandese,
  Finlandese, Francese, Galiziano, Tedesco, Ungherese, Italiano, Giapponese,
  Coreano, Nepalese, Polacco, Portoghese (Brasile), Russo, Slovacco,
  Sloveno, Spagnolo, Tamil e Turco.

## Novità nella versione 2.1

* Aggiornata la dipendenza psutil alla versione 0.6.1.
* Corretto un grosso ritardo che si verificava quando si acquisivano
  informazioni sui drives.
* Pulizia del codice.

## Novità nella versione 2.0

* aggiunto il supporto e i commenti alle traduzioni.

## Novità nella versione 1.0

* Versione iniziale

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
