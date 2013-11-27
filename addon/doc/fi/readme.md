# Resurssienvalvonta #

* Tekijät: Alex Hall, Joseph Lee, beqa gozalishvili sekä muut NVDA:n tekijät
* Vakaa versio: [2.4][1]
* Kehitysversio: [3.0-dev][2]

Tämä lisäosa antaa tietoja suorittimen kuormituksesta, muistin käytöstä sekä
akun ja levyn käytön tilasta.

# Pikanäppäimet #

* NVDA+Shift+E lukee käytetyn RAM-muistin määrän, suorittimen keskimääräisen
  kuormituksen ja akun tiedot, mikäli sellainen on käytössä,
* NVDA+Shift+1 lukee suorittimen ja ydinten keskimääräisen kuormituksen,
* NVDA+Shift+2/5 lukee sekä fyysisen että näennäisen RAM-muistin käytetyn ja
  kokonaismäärän,
* NVDA+Shift+3 lukee kiintolevyjen ja siirrettävien asemien käytetyn ja
  kokonaistilan,
* NVDA+Shift+4 lukee akun varauksen prosentteina, latauksen tilan, jäljellä
  olevan ajan (jos ei latauksessa) sekä varoituksen, mikäli varauksen taso
  on alhainen tai kriittinen,
* NVDA+Shift+6 ilmoittaa Windowsin ja Service Packin version sekä
  suorittimen bittisyyden (32 tai 64) (versio 3.0-dev).

## Huomautuksia käytöstä ##

Tämä lisäosa ei korvaa Windowsin tehtävienhallintaa tai muita
järjestelmätietoja näyttäviä ohjelmia. Huomaa lisäksi seuraavat seikat:

* Suorittimen käyttö ilmoitetaan loogisille suorittimille, ei fyysisille
  ytimille. Tällä on merkitystä Hyper Threading -teknologiaa käyttävissä
  suorittimissa, joissa suorittimien määrä on kaksi kertaa ydinten määrä.
* Suoritinkäytön tietoja haettaessa saattaa olla pieni viive.

## Muutokset versiossa 3.0-dev ##

* Päivitetty psutil-riippuvuus versioksi 1.2.1.
* Lisätty komento (NVDA+Shift+6) käyttämäsi Windowsin ja Service Packin
  version sekä suorittimen  bittisyyden ilmoittamiseksi.
* Mahdollisuus vaihtaa lisäosan pikanäppäimiä (NVDA:n 2013.3-versiossa tai
  uudemmassa).
* Mahdollisuus kopioida yksittäisen resurssin tiedot leikepöydälle
  painamalla komentoja kahdesti.

## Muutokset versiossa 2.4 ##

* Uusia kieliä: kiina (yksinkertaistettu), ukraina
* Käännöksiä päivitetty.

## Muutokset versiossa 2.3 ##

* Lisätty bulgariankielinen käännös.

## Muutokset versiossa 2.2 ##

* Lisätty seuraavat käännökset: arabia, aragonia, brasilianportugali,
  espanja, galego, hollanti, italia, japani, korea, kroatia, nepali, puola,
  ranska, saksa, slovakki, slovenia, suomi, tamili, turkki, unkari ja
  venäjä.

## Muutokset versiossa 2.1 ##

* Päivitetty psutil-riippuvuus versioksi 0.6.1.
* Korjattu pitkä viive asemien tietoja haettaessa.
* Korvattu %s:t {helpoillaMuuttujaNimillä}.
* Koodia hieman siivottu.

## Muutokset versiossa 2.0 ##

* Lisätty käännösten tuki ja käännöskommentteja.

## Muutokset versiossa 1.0 ##

* Ensimmäinen versio

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
