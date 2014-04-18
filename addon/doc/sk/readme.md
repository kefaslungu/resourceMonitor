# Resource Monitor #

* Autori: Alex Hall, Joseph Lee, beqa gozalishvili a ďalší
* Verzia: [3.1][1]Version: [3.1][1]

Tento doplnok poskytuje informácie o zaťažení procesora, stave pamäte a o
iných zdrojoch.

Dôležité: Resource Monitor 3.1 nie je kompatibilný s verziou NVDA 2013.3 a
staršími. Ak používate NVDA 2013.3, alebo niektorú zo starších verzii,
nainštalujte si Resource monitor 3.0.

# Klávesové skratky #

* NVDA+Shift+E oznámy využitie pamäte ram, priemerné zaťaženie procesora a
  stav batérie, ak je dostupná.
* NVDA+Shift+1 oznámy vyťaženie procesora a jednotlivých jadier.
* NVDA+Shift+2/5 povie využitú a celkovú pamäť pre fyzickú a virtuálnu ram
  pamäť.
* NVDA+Shift+3 povie využité a celkové miesto pre pevné a pamäťové disky
  pripojené k počítaču.
* NVDA+Shift+4 oznámy stav batérie v percentách, stav napájania, zostávajúci
  čas (ak sa vybíja) a prípadne upozornenie ak je batéria vybytá alebo v
  kritickom stave.
* NVDA+Shift+6 prečíta architektúru procesora (32 alebo 64 bit), verziu
  Windows a Service packu.

Ak používate verziu NVDA 2013.3 alebo novšiu, môžete si skratky upraviť.

## Všimnite si ##

Tento doplnok nie je náhradou za správcu úloh a iné programy na zisťovanie
informácii v systéme Windows. Vezmite preto navedomie tieto skutočnosti:

* Využitie procesora je vypočítané pre logické procesory, nie pre fyzické
  jadrá. Toto je dôležité pri procesoroch, ktoré používajú viacero vláken,
  kde počet procesorov je dvojnásobný, ako počet jadier.
* Získanie informácie o stave procesora môže chvíľu trvať.

## Zmeny vo verzii 3.1 ##

* Resource monitor oficiálne podporuje Windows 8.1
* Aktualizované preklady.

## Zmeny vo verzii 3.0 ##

* Aktualizovaná knižnica psutil na verziu 1.2.1.
* Oznamovanie architektúri procesora (32 aebo 64 bit), verzie windows a
  Service Packu ((NVDA+Shift+6).
* Možnosť zmeniť klávesové skratky (NVDA 2013 a vyššie).
* Možnosť kopírovať údaje do schránky dvojitým stlačením danej skratky.

## Zmeny vo verzii 2.4 ##

* Nové jazyky: Ukrajinčina, zjednodušená Čínština
* Aktualizované preklady.

## Zmeny vo verzii 2.3 ##

* pridaný preklad do bulharčiny

## Zmeny vo verzii 2.2 ##

* Pridané preklady: Arabčina, Aragónčina, chorvátčina, holandčina, fínčina,
  francúzština, Galijcíjčina, nemčina, maďarčina, taliančina, japončina,
  kórejčina, nepálčina, poľština, brazílska portugalčina, ruština,
  slovenčina, slovinčina, španielčina, Tamilčina a turečtina.

## Zmeny vo verzii 2.1 ##

* Aktualizovaná knižnica psutil na verziu 0.6.1.
* Skrátený čas na zistenie kapacity a miesta na diskoch.
* Zmenená premenná %s na premenné so zmysluplnými názvami.
* drobné úpravy v kóde.

## Zmeny vo verzii 2.0 ##

* Podpora pre preklady vrátane komentárov pre prekladateľov.

## Zmeny vo verzii 1.0 ##

* prvé vydanie

[[!tag stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm
