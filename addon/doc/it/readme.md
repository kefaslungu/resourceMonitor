# Resource Monitor #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst and other NVDA contributors
* Scarica la [versione stabile][1]
* NVDA compatibility: 2017.4 to 2019.2

Questo componente aggiuntivo fornisce informazioni sulle prestazioni di
sistema, quali carico della CPU, utilizzo della memoria e molto altro.

# Tasti rapidi #

* NVDA+Shift+E: fornisce informazioni sul carico della cpu, sulla quantità
  di ram e sulla batteria di sistema se disponibili.
* NVDA+Shift+1: Fornisce informazioni sulla media del carico delle CPU, e
  informazioni dettagliate del carico di ciascuna CPU presente nel sistema.
* NVDA+Shift+2/5: Fornisce informazioni sulla quantità di Ram fisica e
  virtuale utilizzata e disponibile
* NVDA+Shift+3: riporta la dimensione totale e percentuale usata delle unità
  locali e rimovibili.
* NVDA+Shift+4: riporta la percentuale di carica della batteria, stato di
  carica, il tempo rimanente (se non in carica), e un messaggio di avviso se
  la carica è bassa o in uno stato critico. 
* NVDA+Shift+6: riporta l'Architettura della CPU 32/64-bit, la versione di
  Windows e service pack. 
* NVDA+Shift+7 riporta il tempo di attività del sistema.

If you have NvDA 2013.3 or later installed, you can change these shortcut
keys via input gestures dialog.

## Note d'utilizzo ##

Questo componente aggiuntivo non sostituisce applicazioni quali Task Manager
o altri software che forniscono informazioni di sistema. Inoltre si tenga
presente che:

* L'utilizzo della CPU è riportata per processori logici, non core
  fisici. Questo è evidente per i processori che utilizzano Hyper-Threading
  dove il numero di CPU è il doppio del numero di core della CPU.
* Se è in corso un notevole processo sul disco, come ad esempio la copia di
  file di grandi dimensioni, ci potrebbero essere dei ritardi nell'ottenere
  informazioni sull'utilizzo del disco.
* This add-on requires Windows 7 Service Pack 1 or later.

## Version 19.11

* Improved detection of Windows Insider Preview builds, especially for 20H1
  and beyond.

## Version 19.07

* Updated psutil dependency to 5.6.3.
* Internal changes to battery status announcement command.

## Version 18.12

* Internal changes to support future NVDA releases.

## Versione 18.10

* Il codice è stato reso più compatibile con Python 3. 
* Updated psutil dependency to 5.4.7.
* Nel ricavare la capacità del disco o della memoria in uso, NVDA non
  riporterà errore se si utilizza un computer o un servizio con più di un
  petabyte di RAM o di dimensione disco.
* I valori per l'utilizzo della memoria e dimensione disco sono indicati con
  un massimo di due cifre decimali (ad es. 4.00 GB invece di 4.0 GB). 
* Migliorato il rilevamento di Windows Insider Preview build. 

## Versione 18.04

La versione 18.04.x è l'ultima release per il supporto  a Windows 7 SP1 e
precedenti.

* L'ultima release di supporto per Windows Server 2003, Vista e Server 2008.
* Migliorata la rilevazione per le versioni di Windows 10 con la migliore
  distinzione dei rilasci delle anteprime public o Insider.

## Versione 17.12

* Aggiunto il supporto per i processori ARM a 64 bit di Windows 10. 

## Versione 17.09

Importante: la Versione 17.09.x è l'ultima versione che supporta Windows XP.

* Ultima versione per Windows XP. 
* Windows 10 build 16278 and later is recognized as Version 1709. A minor
  revision for this add-on will be released once Version 1709 stable build
  is released.

## Versione 17.07.1

* Reintroduce support for Windows XP (broken since version 17.02).

## Versione 17.05

* Riporta l'attività del sistema (il tempo passato dall'ultimo avvio;
  NVDA+Shift+7). 

## Versione 17.02

* Updated psutil dependency to 5.0.1.
* When checking disk usage, NVDA will no longer present an error dialog on
  some systems where a removable media is not properly recognized (such as
  when a card isn't inserted into a card reader).)

## Versione 16.08

Starting with version 16.08, add-on releases will be shown as
year.month.revision.

* Various revisions of Windows 10 are now properly recognized (such as 1607
  for build 14393).
* Windows 10 build revisions (after installing cumulative updates) are
  properly recognized (such as 14393.51).
* If using Insider Preview builds, this fact is recognized.

## Changes for 4.5 ##

* Add-on repository has moved to GitHub (can be found at
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 is properly recognized.

## Changes for 4.0 ##

* Updated psutil dependency to 2.2.1.
* Vastly improved performance when obtaining information on CPU load.
* Added support for recognition of Windows 10.
* In Windows 10, the build number of Windows will also be announced.
* You can use Add-ons Manager to access add-on help.

## Changes for 3.1 ##

* Resource Monitor officially supports Windows 8.1.
* Updated translations.

## Changes for 3.0 ##

* Updated psutil dependency to 1.2.1.
* Announcement of current Windows version, CPU architecture and service pack
  if any (NVDA+Shift+6).
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## Changes for 2.4 ##

* New languages: Chinese (simplified), Ukrainian.
* Updated translations.

## Changes for 2.3 ##

* Added Bulgarian translation.

## Changes for 2.2 ##

* Added following translations: Arabic, Aragonese, Croatian, Dutch, Finnish,
  French, Galician, German, Hungarian, Italian, Japanese, Korean, Nepali,
  Polish, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil
  and Turkish.

## Changes for 2.1 ##

* Updated psutil dependency to version 0.6.1.
* Fixed long delay when getting information of drives.
* Code cleanup.

## Changes for 2.0 ##

* added translation support and translation comments.

## Changes for 1.0 ##

* Initial Release

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
