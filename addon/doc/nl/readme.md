# Resource Monitor #

* Auteurs: Alex Hall, Joseph Lee, beqa gozalishvili en anderen
* Stabiele versie: [versie 2.4][1]
* Ontwikkelversie: [versie 3.0-dev][2]

Deze add-on geeft informatie over CPU gebruik, RAM-geheugen, schijfruimte en
batterijstatus.

# Sneltoetsen #

* NVDA+Shift+E Geeft gebruikt RAM-geheugen, CPU gebruik en batterijstatus
  indien beschikbaar
* NVDA+Shift+1 Geeft de gemiddelde processorbelasting en de belasting van
  elke kern
* NVDA+Shift+2 Geeft de totale en gebruikte ruimte van fysiek en virtueel
  RAM-geheugen
* NVDA+Shift+3 Geeft de gebruikte en totale ruimte voor vaste en
  verwisselbare schijven van deze computer
* NVDA+Shift+4 Geeft batterijpercentage, oplaad status, resterende tijd (als
  er niet wordt opgeladen) en een waarschuwing als de batterij bijna leeg is
* NVDA+Shift+6 Presents currently installed Windows version, CPU bit (32 or
  64-bit) and service pack if any (version 3.0-dev).

## Opmerkingen voor gebruik ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper Threading where number of CPU's
  is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## Veranderingen voor 3.0-dev ##

* Updated psutil dependency to 1.2.1.
* Added a command (NVDA+Shift+6) to report the version of Windows you are
  using, CPU bit and service packs if any.
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## Veranderingen voor 2.4 ##

* Nieuwe vertalingen: Chinees (vereenvoudigd), Oekraïens.
* Vertalingen bijgewerkt.

## Veranderingen voor 2.3 ##

* Bulgaarse vertaling toegevoegd.

## Veranderingen voor 2.2 ##

* De volgende vertalingen toegevoegd: Arabicsch, Aragonees, Croatisch,
  Nederlands, Fins, Frans, Galatian, Duits, Hongaars, Italiaans, Japans,
  Koreaans, Nepali, Pools, Portugees (Brazilië), Russisch, Slowaaks,
  Sloveens, Spaans, Tamil en Turks

## Veranderingen voor 2.1 ##

* Psutil afhankelijkheid bijgewerkt naar versie 0.6.1
* Vertraging bij het opvragen van schijf-informatie opgelost
* %s vervangen door variabele namen
* Opruimen van de code

## Veranderingen voor 2.0 ##

* Ondersteuning voor vertalingen en commentaar voor vertalers toegevoegd

## Veranderingen voor 1.0 ##

* Eerste versie

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
