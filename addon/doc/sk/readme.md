# Resource monitor #

* Autori: Alex Hall, Joseph Lee, beqa gozalishvili a ďalší
* Stabilná verzia: [verzia 2.4][1]
* Vývojová verzia: [verzia 3.0-dev][2]

Tento doplnok poskytuje informácie o zaťažení procesora, stave pamäte, o
stave napájania a mieste na diskoch..

# Klávesové skratky #

* NVDA+Shift+E oznámy využitie pamäte ram, priemerné zaťaženie procesora a
  stav batérie, ak je dostupná,
* NVDA+Shift+1 oznámy vyťaženie procesora a jednotlivých jadier,
* NVDA+Shift+2/5 povie využitú a celkovú pamäť pre fyzickú a virtuálnu ram
  pamäť,
* NVDA+Shift+3 povie využité a ceľkové miesto pre pevné a pamäťové disky
  pripojené k počítaču,
* NVDA+Shift+4 oznámy stav batérie v percentách, stav napájania, zostávajúci
  čas (ak sa vybíja) a prípadne upozornenie ak je batéria vybytá alebo v
  kritickom stave,
* NVDA+Shift+6 prečíta verziu operačného systému, či ide o 32-bit alebo
  64-bitový systém a nainštalovaný Service Pack (ak nejaký je). (Týka sa
  verzie 3.0-dev).

## Všimnite si ##

Tento doplnok nie je náhradou za správcu úloh a iné programy na zisťovanie
informácii v systéme Windows. Vezmite preto navedomie tieto skutočnosti:

* Využitie procesora je vypočítané pre logické procesory, nie pre fyzické
  jadrá. Toto je dôležité pri procesoroch, ktoré používajú viacero vláken,
  kde počet procesorov je dvojnásobný, ako počet jadier.
* There might be a short delay when getting processor usage information.

## Zmeny vo verzii 3.0 - dev ##

* Updated psutil dependency to 1.2.1.
* Pridaná skratka NVDA+Shift+6 na zistenie verzie operačného systému,
  informáciu o tom, č ide o 32-bitový alebo 64-bitový systém a o používanom
  Service Packu (ak sa používa).
* Možnosť zmeniť klávesové skratky (NVDA 2013 a vyššie).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## Zmeny vo verzii 2.4 ##

* Nové jazyky: Ukrajinčina, zjednodušená Čínština
* Aktualizované preklady.

## Zmeny vo verzii 2.3 ##

* pridaný preklad do bulharčiny

## Zmeny vo verzii 2.2 ##

* Pridané preklady: Arabčina, Aragončina, chorvátčina, holandčina, fínčina,
  francúzština, Galijcijčina, nemčina, maďarčina, taliančina, japončina,
  kórejčina, nepálčina, poľština, Brazílska portugalčina, ruština,
  slovenčina, slovinčina, španielčina, Tamilčina a turečtina.

## Zmeny vo verzii 2.1 ##

* Aktualizovaná knižnica psutil na verziu 0.6.1.
* Skrátený čas na zistenie kapacity a miesta na diskoch.
* Zmenená premenná %s na premenné so zmysluplnými názvami.
* drobné úpravy v kóde

## Zmeny vo verzii 2.0 ##

* Podpora pre preklady vrátane komentárov pre prekladateľov.

## Zmeny vo verzii 1.0 ##

* prvé vydanie

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
