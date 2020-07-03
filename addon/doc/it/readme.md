# Resource Monitor #

* Autori: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala e altri
  collaboratori di NVDA
* Scarica la [versione stabile][1]
* NVDA compatibility: 2019.3 to 2020.2

Questo componente aggiuntivo fornisce informazioni sulle prestazioni di
sistema, quali carico della CPU, utilizzo della memoria e molto altro.

# Tasti rapidi #

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

If you have NvDA 2013.3 or later installed, you can change these shortcut
keys via input gestures dialog.

## Note d'utilizzo ##

Questo componente aggiuntivo non sostituisce applicazioni quali Task Manager
o altri software che forniscono informazioni di sistema per Windows. Inoltre
si tenga presente che:

* L'utilizzo della CPU è riportato per processori logici, non core
  fisici. Questo è evidente per i processori che utilizzano Hyper-Threading
  dove il numero di CPU è il doppio del numero di core della CPU.
* Se è in corso un notevole processo sul disco, come ad esempio la copia di
  file di grandi dimensioni, ci potrebbero essere dei ritardi nell'ottenere
  informazioni sull'utilizzo del disco.
* Questo add-on richiede Windows 7 Service Pack 1 o superiore.

## Version 20.07

* Windows 10 Version 20H2 is properly recognized when obtaining Windows
  version information (NVDA+Shift+6).
* Simplified Windows 10 version message i.e. Windows 10 YYMM instead of
  Windows 10verYYMM when pressing NVDA+Shift+6.

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

## Novità nella versione 4.5 ##

* Il repository dell'add-on è stato spostato su GitHub (lo si trova
  all'indirizzo https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 è riconosciuto correttamente.

## Novità nella versione 4.0 ##

* Aggiornata la dipendenza psutil alla versione 2.2.1.
* Performance molto migliorate nell'acquisizione delle informazioni sul
  carico della CPU.
* Aggiunto il supporto al riconoscimento di Windows 10.
* In Windows 10, verrà anche vocalizzato il numero di build.
* Per accedere alla guida, si può utilizzare il gestore componenti
  aggiuntivi.

## Novità nella versione 3.1 ##

* Resource Monitor supporta ufficialmente Windows 8.1.
* Traduzioni aggiornate.

## Novità nella versione 3.0 ##

* Aggiornata la dipendenza psutil alla versione 1.2.1.
* Vocalizzazione della versione corrente di Windows, dell'architettura della
  CPU e del service pack se presente  (NVDA+Shift+6).
* Possibilità di cambiare i tasti rapidi dell'add-on (NVDA 2013.3 o
  superiore).
* Possibilità di copiare ciascuna informazione sulle risorse negli appunti
  digitando i comandi due volte.

## Novità nella versione 2.4 ##

* Nuove lingue: Cinese (semplificato), Ucraino.
* Traduzioni aggiornate.

## Novità nella versione 2.3 ##

* Aggiunta la traduzione in bulgaro.

## Novità nella versione 2.2 ##

* Aggiunte le seguenti traduzioni: Arabo, Aragonese, Croato, Olandese,
  Finlandese, Francese, Galiziano, Tedesco, Ungherese, Italiano, Giapponese,
  Coreano, Nepalese, Polacco, Portoghese (Brasile), Russo, Slovacco,
  Sloveno, Spagnolo, Tamil e Turco.

## Novità nella versione 2.1 ##

* Aggiornata la dipendenza psutil alla versione 0.6.1.
* Corretto un grosso ritardo che si verificava quando si acquisivano
  informazioni sui drives.
* Pulizia del codice.

## Novità nella versione 2.0 ##

* aggiunto il supporto e i commenti alle traduzioni.

## Novità nella versione 1.0 ##

* Versione iniziale

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
