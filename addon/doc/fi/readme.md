# Resurssienvalvonta #

* Tekijät: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst sekä muut NVDA:n tekijät
* Lataa [vakaa versio][1]
* Yhteensopivuus: NVDA 2022.4 ja uudemmat

Tämä lisäosa antaa tietoja suorittimen kuormituksesta sekä muistin ja muiden
resurssien käytöstä.

# Pikanäppäimet

* NVDA+Vaihto+E: Lukee käytetyn RAM-muistin määrän, suorittimen
  keskimääräisen kuormituksen sekä akun tiedot, mikäli sellainen on
  käytettävissä.
* NVDA+Vaihto+1: Lukee suorittimen keskimääräisen kuormituksen, ja mikäli
  käytössä on moniydinsuoritin, myös ytimien kuormituksen.
* NVDA+Vaihto+2/5: Lukee sekä fyysisen että näennäisen RAM-muistin käytetyn
  ja kokonaismäärän.
* NVDA+Vaihto+3: Lukee kiintolevyjen ja siirrettävien asemien käytetyn ja
  kokonaistilan.
* NVDA+Vaihto+4: Lukee akun varauksen prosentteina, latauksen tilan,
  jäljellä olevan ajan (jos ei latauksessa) sekä varoituksen, mikäli
  varauksen taso on alhainen tai kriittinen.
* NVDA+Vaihto+6: Ilmoittaa suorittimen arkkitehtuurin sekä Windowsin ja
  Service Packin version.
* NVDA+Vaihto+7 ilmoittaa järjestelmän käynnissäoloajan.
* NVDA+Vaihto+8: Ilmoittaa langattoman verkon tiedot, kuten SSID-nimen ja
  signaalin voimakkuuden tai "SSID:tä ei löydy", jos verkkoa ei ole
  saatavilla.

Voit muuttaa näitä pikanäppäimiä Näppäinkomennot-valintaikkunasta.

## Huomautuksia käytöstä

Tämä lisäosa ei korvaa Windowsin tehtävienhallintaa tai muita
järjestelmätietoja näyttäviä ohjelmia. Huomaa lisäksi seuraavat seikat:

* Resurssitietoja ei voi kopioida leikepöydälle, jos lisäosaa käytetään
  suojatuissa ruuduissa.
* Suorittimen käyttö ilmoitetaan loogisille suorittimille, ei fyysisille
  ytimille. Tällä on merkitystä Hyper Threading -teknologiaa käyttävissä
  suorittimissa, joissa suorittimien määrä on kaksi kertaa ydinten
  määrä. Joissakin uudemmissa tietokoneissa Hyper Threading ei ole käytössä
  kaikilla suoritinytimillä.
* Levynkäyttötietoja haettaessa saattaa olla viivettä, mikäli levytoimintaa,
  kuten suurten tiedostojen kopiointia, on runsaasti.
* Suorittimen arkkitehtuuritietoja ilmoitettaessa "x86" ja "AMD64"
  viittaavat 32- ja 64-bittisiin (x64) Intel- ja AMD-suorittimiin.
* Tämä lisäosa edellyttää Windows 10:tä tai uudempaa.

Huomautus lisenssistä: tämä lisäosa käyttää Psutil-riippuvuutta, joka on
kolmilausekkeisen BSD-lisenssin alainen, joka on yhteensopiva GNU GPL
-lisenssin kanssa.

## Versio 23.09

* NVDA ei enää kirjoita lokiin käynnistyksen virheilmoituksia Windows Server
  -järjestelmissä, kun langaton verkkosovitin ei ole käytettävissä.

## Versio 23.06

* Korjattu tilanne, jossa Resurssienvalvonta ei toimi oikein langattoman
  verkkosovittimen puuttumisen vuoksi.

## Versio 23.05.1

WlanReporter-lisäosa sisältyy nyt Resurssienvalvontaan!

* Aiempi langattomien yhteyksien etsintätapa on korvattu Windowsin
  rajapinnalla, jota käytetään wlanReporter-lisäosassa:
  https://github.com/kvark128/WlanReporter/.

	* NVDA kertoo nyt SSID-nimen ja signaalin voimakkuuden jälkeen myös verkon
	  suojauksen tyypin.
	* NVDA ilmoittaa nyt langattoman verkon yhteyden muodostamisesta ja
	  katkaisusta.
	* NVDA ilmoittaa nyt, kun langattomat yhteydet otetaan käyttöön tai
	  poistetaan käytöstä.

## Versio 23.05

* Lisätty mahdollisuus yhdistetyn langattoman verkon tilan tunnistamiseen ja
  näyttämiseen.

	* Ilmoittaa yhdistetyn langattoman verkon SSID-nimen.
	* Ilmoittaa langattoman verkon signaalin voimakkuuden.
	* Ilmoittaa "SSID:tä ei löydy", mikäli langatonta verkkoa ei löydy.

## Versio 23.02

* Edellyttää NVDA 2022.4:ää tai uudempaa.
* Windows 10 21H2 (marraskuun 2021 päivitys/koontiversio 19044) tai uudempi
  vaaditaan.

## Versio 23.01

* Edellyttää NVDA 2022.3:ea tai uudempaa.
* Windows 10 tai uudempi vaaditaan, koska Microsoft ei enää tue Windows
  7:ää, 8:aa tai 8.1:tä tammikuusta 2023 alkaen.
* Päivitetty psutil-riippuvuus versioksi 5.9.4.
* Suorittimen arkkitehtuuri (x86/AMD64/ARM64) ilmoitetaan osana Windowsin
  versiotietoja.
* NVDA ei enää ilmoita suoritinytimen kuormitusta yhden ytimen
  järjestelmissä, koska keskimääräinen suorittimen kuormitus on sama kuin
  ytimen kuormitus.

## Versio 22.03

Versio 22.03 is the last stable version to support Windows 7 Service Pack 1,
8, and 8.1.

* Edellyttää NVDA 2021.3:ea tai uudempaa.
* Varoitus näytetään yritettäessä asentaa lisäosaa Windows 7:ään, 8:aan tai
  8.1:een.
* Päivitetty psutil-riippuvuus versioksi 5.9.0.

## Versio 22.01

* Edellyttää NVDA 2021.2:ta tai uudempaa.

## Versio 21.10

* NVDA 2021.1 tai uudempi vaaditaan tähän lisäosaan vaikuttavien
  NVDA-muutosten takia.

## Versio 21.08

* Windowsin vähimmäisversiovaatimus on nyt sidottu NVDA-versioihin.
* Windowsin koontiversiot 20348 ja 22000 tunnistetaan Windows Server
  2022:ksi ja Windows 11:ksi.
* Windows-versiota, kuten "Windows 10", ei käytetä
  Insider-esiversioissa. Sen sijaan NVDA ilmoittaa "Windows Insider".
* Suorittimen arkkitehtuuri (x64 tai ARM64) ilmoitetaan osana Windowsin
  versiotietoja 64-bittisissä järjestelmissä.

## Versio 21.04

* Edellyttää NVDA 2020.4:ää tai uudempaa.
* Päivitetty psutil-riippuvuus versioksi 5.8.0.
* Kun lisäosan komentoja painetaan kahdesti resurssitietojen kopioimiseksi
  leikepöydälle, NVDA ilmoittaa kopioitavan resurssiyhteenvedon.

## Versio 21.01

* Päivitetty psutil-riippuvuus versioksi 5.7.3.
* Windowsin versioilmoitusta lyhennetty.
* Windows 8.1:ssä koontiversio.tarkennus ilmoitetaan osana Windowsin
  versiota samalla tavalla kuin Windows 10:ssä.

## Versio 20.09

* Järjestelmän käynnissäoloaika ilmoitetaan nyt päivinä, tunteina,
  minuutteina ja sekunteina.
* Windows Server Insider-esikoontiversio 20201 tai sitä uudempi tunnistetaan
  oikein Server Insider -koontiversioksi.

## Versio 20.07

* Windows 10:n versio 20H2 tunnistetaan oikein Windowsin versiotietoja
  haettaessa (NVDA+Vaihto+6).
* Yksinkertaistettu Windows 10:n versioviestiä painettaessa NVDA+Vaihto+6,
  esim. Windows 10verVVKK:n:n asemesta Windows 10 VVKK.

## Versio 20.06

* Ratkaistu useita koodaustyylin ongelmia sekä mahdollisia bugeja Flake8:n
  kanssa.

## Versio 20.04

* Päivitetty psutil-riippuvuus versioksi 5.7.0.

## Versio 20.01

* NVDA 2019.3 tai uudempi vaaditaan laajamittaisen Python 3:n käytön takia.

## Versio 19.11

* Windows Insider -esiversioiden tunnistusta paranneltu, erityisesti
  20H1:ssä ja uudemmissa.

## Versio 19.07

* Päivitetty psutil-riippuvuus versioksi 5.6.3.
* Sisäisiä muutoksia akun tilan ilmoittavaan komentoon.

## Versio 18.12

* Sisäisiä muutoksia tulevien NVDA-versioiden tukemiseksi.

## Versio 18.10

* Koodista on tehty yhteensopivampaa Python 3:n kanssa.
* Päivitetty psutil-riippuvuus versioksi 5.4.7.
* NVDA ei enää ilmoita virheistä haettaessa tietoa levyn kapasiteetista ja
  muistin käytöstä , mikäli käytetään  tietokonetta tai palvelua, jossa
  RAM-muistin määrä tai levyn koko ylittää yhden petatavun.
* Muistin ja levyn käytön arvot näytetään enintään kahdella desimaalilla
  (esim. 4.00 Gt aiemman 4.0 Gt sijaan).
* Windows Insider -esiversioiden tunnistusta paranneltu.

## Versio 18.04

Versio 18.04.x on viimeinen julkaisu, joka tukee 7 SP1:tä vanhempia
Windows-versioita.

* Viimeinen Windows Server 2003:a, Vistaa ja Server 2008:aa tukeva versio.
* Parempi Windows 10 -versioiden tunnistaminen sekä julkisten ja
  Insider-esiversioiden erottaminen toisistaan.

## Versio 17.12

* Lisätty tuki 64-bittisille ARM-suorittimille Windows 10:ssä.

## Versio 17.09

Tärkeää: 17.09.x on viimeinen Windows XP:tä tukeva versio.

* Viimeinen Windows XP:ssä ajettava versio.
* Windows 10:n koontiversio 16278 ja uudemmat tunnistetaan versioksi
  1709. Tästä lisäosasta julkaistaan pieni päivitys, kun version 1709 vakaa
  koontiversio on julkistettu.

## Versio 17.07.1

* Palautettu Windows XP:n tuki (ollut rikki versiosta 17.02 lähtien).

## Versio 17.05

* Järjestelmän käynnissäoloajan ilmoittaminen (edellisestä käynnistyksestä
  kulunut aika; NVDA+Shift+7).

## Versio 17.02

* Päivitetty psutil-riippuvuus versioksi 5.0.1.
* NVDA ei näytä enää virheilmoitusta levynkäyttötietoja tarkistettaessa
  järjestelmissä, joissa siirrettävää tietovälinettä ei tunnistettu oikein
  (esim. kun muistikorttia ei ole asetettu kortinlukijaan).

## Versio 16.08

Lisäosan versionumerot ovat Versiosta 16.08 alkaen muotoa
vuosi.kuukausi.tarkistusversio.

* Windows 10:n eri versiot tunnistetaan nyt oikein (kuten 1607
  koontiversiossa 14393).
* Windows 10:n koontiversiot tunnistetaan oikein kumulatiivisten päivitysten
  asentamisen jälkeen (kuten 14393.51).
* Insider-esiversiot tunnistetaan oikein.

## Muutokset versiossa 4.5

* Lisäosan koodivarasto on muuttanut GitHubiin (löytyy osoitteesta
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 tunnistetaan asianmukaisesti.

## Muutokset versiossa 4.0

* Päivitetty psutil-riippuvuus versioksi 2.2.1.
* Suorituskykyä paranneltu huomattavasti suorittimen kuormituksen tietoja
  haettaessa.
* Lisätty tuki Windows 10:n tunnistamiselle.
* Windows 10:n versiota ilmoitettaessa kerrotaan myös koontiversio.
* Ohje on käytettävissä Lisäosien hallinnasta.

## Muutokset versiossa 3.1

* Resurssienvalvonta tukee virallisesti Windows 8.1:tä.
* Käännöksiä päivitetty.

## Muutokset versiossa 3.0

* Päivitetty psutil-riippuvuus versioksi 1.2.1.
* Suorittimen arkkitehtuurin sekä Windowsin ja Service Packin version
  ilmoittaminen (NVDA+Shift+6).
* Mahdollisuus vaihtaa lisäosan pikanäppäimiä (NVDA:n 2013.3-versiossa tai
  uudemmassa).
* Mahdollisuus kopioida yksittäisen resurssin tiedot leikepöydälle
  painamalla komentoja kahdesti.

## Muutokset versiossa 2.4

* Uusia kieliä: kiina (yksinkertaistettu), ukraina
* Käännöksiä päivitetty.

## Muutokset versiossa 2.3

* Lisätty bulgariankielinen käännös.

## Muutokset versiossa 2.2

* Lisätty seuraavat käännökset: arabia, aragonia, brasilianportugali,
  espanja, galego, hollanti, italia, japani, korea, kroatia, nepali, puola,
  ranska, saksa, slovakki, slovenia, suomi, tamili, turkki, unkari ja
  venäjä.

## Muutokset versiossa 2.1

* Päivitetty psutil-riippuvuus versioksi 0.6.1.
* Korjattu pitkä viive asemien tietoja haettaessa.
* Koodia siivottu.

## Muutokset versiossa 2.0

* Lisätty käännösten tuki ja käännöskommentteja.

## Muutokset versiossa 1.0

* Ensimmäinen versio

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
