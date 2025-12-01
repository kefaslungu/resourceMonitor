# Resurssienvalvonta

* Tekijät: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst sekä muut NVDA-yhteisön jäsenet

Tämä lisäosa antaa tietoja suorittimen kuormituksesta sekä muistin ja muiden resurssien käytöstä.

# Pikanäppäimet

Kaikki komennot tukevat pyydettäessä-puhetilaa.

* NVDA+Vaihto+E: Ilmoittaa käytetyn RAM-muistin määrän, suorittimen keskimääräisen kuormituksen sekä akun tiedot, mikäli sellainen on käytettävissä.
* NVDA+Vaihto+1: Ilmoittaa suorittimen keskimääräisen kuormituksen ja lisäksi ytimien kuormituksen, mikäli kyseessä on moniydinsuoritin.
* NVDA+Vaihto+2/5: Ilmoittaa sekä fyysisen että näennäisen RAM-muistin käytetyn ja kokonaismäärän.
* NVDA+Vaihto+3: Ilmoittaa kiintolevyjen ja siirrettävien asemien käytetyn ja kokonaistilan.
* NVDA+Vaihto+4: Ilmoittaa akun varauksen prosentteina, latauksen tilan, jäljellä olevan ajan (jos ei latauksessa) sekä varoituksen, mikäli varauksen taso on alhainen tai kriittinen.
* NVDA+Vaihto+6: Ilmoittaa suorittimen arkkitehtuurin sekä Windowsin ja Service Packin version.
* NVDA+Vaihto+7: Ilmoittaa järjestelmän käynnissäoloajan.
* NVDA+Vaihto+8: Ilmoittaa langattoman verkon tiedot, kuten SSID-nimen ja signaalin voimakkuuden tai "SSID:tä ei löydy", jos verkkoa ei ole käytettävissä.

Voit muuttaa näitä pikanäppäimiä Näppäinkomennot-valintaikkunasta.

## Huomautuksia käytöstä

Tämä lisäosa ei korvaa Windowsin tehtävienhallintaa tai muita järjestelmätietoja näyttäviä ohjelmia. Ota lisäksi huomioon seuraavat seikat:

* Resurssitietoja ei voi kopioida leikepöydälle, jos lisäosaa käytetään suojatuissa ruuduissa.
* Suorittimen käyttö ilmoitetaan loogisille suorittimille, ei fyysisille ytimille. Tällä on merkitystä Hyper Threading -teknologiaa käyttävissä suorittimissa, joissa suorittimien määrä on kaksi kertaa ydinten määrä. Joissakin uudemmissa tietokoneissa Hyper Threading ei ole käytössä kaikilla suoritinytimillä.
* Levynkäyttötietoja haettaessa saattaa olla viivettä, mikäli levytoimintaa, kuten suurten tiedostojen kopiointia, on runsaasti.
* Suorittimen arkkitehtuuritietoja ilmoitettaessa "x86" ja "AMD64" viittaavat 32- ja 64-bittisiin (x64) Intel- ja AMD-suorittimiin.
* Vaikka tämä lisäosa tukee rajoitetusti Windows 8.1:tä, Windows 10 22H2:n (2022-päivitys/koontiversio 19045) tai uudemman käyttö on suositeltavaa.
* Tämän lisäosan asentamista ei tueta Windows 10:n/11:n LTSC-versioissa.

## Versio 25.09

* Edellyttää NVDA 2025.2:ta tai uudempaa.

## Versio 25.07

* Lisäosan koodin vakautta parannettu Pyrightin (Pythonin staattinen tyypintarkistustyökalu) avulla.

## Versio 25.06

* Paranneltu yhteystilan ilmoitusta langattomiin verkkoihin yhdistettäessä. (@danstiv).

## Versio 25.02

* Palautettu rajoitettu tuki Windows 8.1:lle.
* Paranneltu käytetyn ja kokonaismuistimäärän ilmoituksen tarkkuutta (@danstiv).
* NVDA ei näytä enää lakkaavan vastaamasta hetkellisesti suoritettaessa muistin käyttöön liittyvää komentoa (NVDA+Vaihto+2/5) ensimmäistä kertaa NVDA:n käynnistämisen jälkeen.
* Windows Insider -esiversioita ei enää ilmoiteta "Windows Insider" -versioiksi.

## Versio 24.08

* Edellyttää NVDA 2024.2:ta tai uudempaa. Tämä mahdollistaa psutil-riippuvuuden poistamisen lisäosasta, koska se sisältyy NVDA:han.
* Päivitetty psutil-riippuvuus NVDA 2024.2:n mukana tulevaan versioon (6.0.0).
* Ruff korvaa Flake8:n koodin tarkistustyökaluna.

## Versio 24.05

* Edellyttää NVDA 2024.1:tä tai uudempaa.
* NVDA tunnistaa langattomat verkot, joissa käytetään WPA3-autentikointimenetelmiä, kuten tasavertaista samanaikaista todennusta (SAE).

## Versio 24.04

* Päivitetty psutil-riippuvuus versioksi 5.9.8.
* Lisätty tuki pyydettäessä-puhetilalle, jotta resurssitiedot voidaan puhuttaa sitä käytettäessä.

## Versio 23.11

* Päivitetty psutil-riippuvuus alaspäin versioksi 5.9.4 muistinkäytön puhumisessa ilmenneiden ongelmien vuoksi.

## Versio 23.10

* Päivitetty psutil-riippuvuus versioksi 5.9.5.

## Versio 23.09

* NVDA ei enää kirjoita lokiin käynnistyksen virheilmoituksia Windows Server -järjestelmissä, kun langaton verkkosovitin ei ole käytettävissä.

## Versio 23.06

* Korjattu tilanne, jossa Resurssienvalvonta ei toimi oikein langattoman verkkosovittimen puuttumisen vuoksi.

## Versio 23.05.1

WlanReporter-lisäosa sisältyy nyt Resurssienvalvontaan.

* Aiempi langattomien yhteyksien etsintätapa on korvattu Windowsin rajapinnalla, jota käytetään wlanReporter-lisäosassa: https://github.com/kvark128/WlanReporter/.
  * NVDA kertoo nyt SSID-nimen ja signaalin voimakkuuden jälkeen myös verkon suojauksen tyypin.
  * NVDA ilmoittaa nyt langattoman verkon yhteyden muodostamisesta ja katkaisusta.
  * NVDA ilmoittaa nyt, kun langattomat yhteydet otetaan käyttöön tai poistetaan käytöstä.

## Versio 23.05

* Lisätty mahdollisuus yhdistetyn langattoman verkon tilan tunnistamiseen ja näyttämiseen.
  * Ilmoittaa yhdistetyn langattoman verkon SSID-nimen.
  * Ilmoittaa langattoman verkon signaalin voimakkuuden.
  * Ilmoittaa "SSID:tä ei löydy", jos langatonta verkkoa ei löydy.

## Versio 23.02

* Edellyttää NVDA 2022.4:ää tai uudempaa.
* Edellyttää Windows 10 21H2:ta (marraskuun 2021 päivitys/koontiversio 19044) tai uudempaa.

## Versio 23.01

* Edellyttää NVDA 2022.3:a tai uudempaa.
* Edellyttää Windows 10:tä tai uudempaa, koska Microsoft ei enää tue Windows 7:ää, 8:aa tai 8.1:tä tammikuusta 2023 alkaen.
* Päivitetty psutil-riippuvuus versioksi 5.9.4.
* Suorittimen arkkitehtuuri (x86/AMD64/ARM64) ilmoitetaan osana Windowsin versiotietoja.
* NVDA ei enää ilmoita suoritinytimen kuormitusta yhden ytimen järjestelmissä, koska keskimääräinen suorittimen kuormitus on sama kuin ytimen kuormitus.

## Versio 22.03

Tämä on viimeinen Windows 7 Service Pack 1:tä, 8:aa ja 8.1:tä tukeva vakaa versio.

* Edellyttää NVDA 2021.3:a tai uudempaa.
* Käyttäjälle näytetään varoitus, kun lisäosaa yritetään asentaa Windows 7:ään, 8:aan tai 8.1:een.
* Päivitetty psutil-riippuvuus versioksi 5.9.0.

## Versio 22.01

* Edellyttää NVDA 2021.2:ta tai uudempaa.

## Versio 21.10

* Edellyttää NVDA 2021.1:tä tai uudempaa tähän lisäosaan vaikuttavien NVDA-muutosten vuoksi.

## Versio 21.08

* Windowsin vähimmäisversiovaatimus on nyt sidottu NVDA-versioihin.
* Windowsin koontiversiot 20348 ja 22000 tunnistetaan Windows Server 2022:ksi ja Windows 11:ksi.
* Windows-versiota, kuten "Windows 10", ei käytetä Insider-esiversioissa. Sen sijaan NVDA ilmoittaa "Windows Insider".
* Suorittimen arkkitehtuuri (x64 tai ARM64) ilmoitetaan osana Windowsin versiotietoja 64-bittisissä järjestelmissä.

## Versio 21.04

* Edellyttää NVDA 2020.4:ää tai uudempaa.
* Päivitetty psutil-riippuvuus versioksi 5.8.0.
* NVDA ilmoittaa kopioitavan resurssiyhteenvedon, kun lisäosan komentoja painetaan kahdesti resurssitietojen kopioimiseksi leikepöydälle.

## Versio 21.01

* Päivitetty psutil-riippuvuus versioksi 5.7.3.
* Windowsin versioilmoitusta lyhennetty.
* Windows 8.1:ssä koontiversio.tarkenne ilmoitetaan osana Windowsin versiota samalla tavalla kuin Windows 10:ssä.

## Versio 20.09

* Järjestelmän käynnissäoloaika ilmoitetaan nyt päivinä, tunteina, minuutteina ja sekunteina.
* Windows Server Insider-esikoontiversio 20201 tai sitä uudempi tunnistetaan oikein Server Insider -koontiversioksi.

## Versio 20.07

* Windows 10:n versio 20H2 tunnistetaan oikein Windowsin versiotietoja haettaessa (NVDA+Vaihto+6).
* Yksinkertaistettu Windows 10:n versioilmoitusta painettaessa NVDA+Vaihto+6, esim. Windows 10verVVKK:n:n asemesta Windows 10 VVKK.

## Versio 20.06

* Ratkaistu useita koodaustyylin ongelmia sekä mahdollisia virheitä Flake8:n kanssa.

## Versio 20.04

* Päivitetty psutil-riippuvuus versioksi 5.7.0.

## Versio 20.01

* Edellyttää NVDA 2019.3:a tai uudempaa laajamittaisen Python 3:n käytön takia.

## Versio 19.11

* Insider-esiversioiden tunnistusta paranneltu erityisesti Windows 10 20H1:ssä ja uudemmissa.

## Versio 19.07

* Päivitetty psutil-riippuvuus versioksi 5.6.3.
* Sisäisiä muutoksia akun tilan ilmoittavaan komentoon.

## Versio 18.12

* Sisäisiä muutoksia tulevien NVDA-versioiden tukemiseksi.

## Versio 18.10

* Koodista on tehty yhteensopivampaa Python 3:n kanssa.
* Päivitetty psutil-riippuvuus versioksi 5.4.7.
* NVDA ei enää ilmoita virheistä haettaessa tietoa levyn kapasiteetista ja muistin käytöstä , mikäli käytetään  tietokonetta tai palvelua, jossa RAM-muistin määrä tai levyn koko ylittää yhden petatavun.
* Muistin ja levyn käytön arvot näytetään enintään kahdella desimaalilla (esim. 4.00 Gt aiemman 4.0 Gt sijaan).
* Windows Insider -esiversioiden tunnistusta paranneltu.

## Versio 18.04

Versio 18.04.x on viimeinen, joka tukee 7 SP1:tä vanhempia Windows-versioita.

* Viimeinen Windows Server 2003:a, Vistaa ja Server 2008:aa tukeva versio.
* Parempi Windows 10 -versioiden tunnistaminen sekä julkisten ja Insider-esiversioiden erottaminen toisistaan.

## Versio 17.12

* Lisätty tuki 64-bittisille ARM-suorittimille Windows 10:ssä.

## Versio 17.09

Tärkeää: 17.09.x on viimeinen Windows XP:tä tukeva versio.

* Viimeinen Windows XP:ssä toimiva versio.
* Windows 10:n koontiversio 16278 ja uudemmat tunnistetaan versioksi 1709. Tästä lisäosasta julkaistaan pieni päivitys, kun version 1709 vakaa koontiversio on julkistettu.

## Versio 17.07.1

* Palautettu Windows XP:n tuki (ollut rikki versiosta 17.02 lähtien).

## Versio 17.05

* Järjestelmän käynnissäoloajan ilmoittaminen (edellisestä käynnistyksestä kulunut aika; NVDA+Shift+7).

## Versio 17.02

* Päivitetty psutil-riippuvuus versioksi 5.0.1.
* NVDA ei näytä enää virheilmoitusta levynkäyttötietoja tarkistettaessa järjestelmissä, joissa siirrettävää massamuistia ei tunnistettu oikein (esim. kun muistikorttia ei ole asetettu kortinlukijaan).

## Versio 16.08

Lisäosan versionumerot ovat Versiosta 16.08 alkaen muotoa vuosi.kuukausi.tarkenne.

* Windows 10:n eri versiot tunnistetaan nyt oikein (kuten 1607 koontiversiossa 14393).
* Windows 10:n koontiversiot tunnistetaan oikein kumulatiivisten päivitysten asentamisen jälkeen (kuten 14393.51).
* Insider-esiversiot tunnistetaan oikein.

## Muutokset versiossa 4.5

* Lisäosan koodivarasto on muuttanut GitHubiin (löytyy osoitteesta https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 tunnistetaan oikein.

## Muutokset versiossa 4.0

* Päivitetty psutil-riippuvuus versioksi 2.2.1.
* Suorituskyky parantunut huomattavasti suorittimen kuormituksen tietoja haettaessa.
* Lisätty tuki Windows 10:n tunnistamiselle.
* Windows 10:n versiota ilmoitettaessa kerrotaan myös koontiversio.
* Ohje on käytettävissä Lisäosien hallinnassa.

## Muutokset versiossa 3.1

* Resurssienvalvonta tukee virallisesti Windows 8.1:tä.
* Käännöksiä päivitetty.

## Muutokset versiossa 3.0

* Päivitetty psutil-riippuvuus versioksi 1.2.1.
* Suorittimen arkkitehtuurin sekä Windowsin ja Service Packin version ilmoittaminen (NVDA+Shift+6).
* Mahdollisuus vaihtaa lisäosan pikanäppäimiä (NVDA:n 2013.3-versiossa tai uudemmassa).
* Mahdollisuus kopioida yksittäisen resurssin tiedot leikepöydälle painamalla komentoja kahdesti.

## Muutokset versiossa 2.4

* Uusia kieliä: kiina (yksinkertaistettu), ukraina
* Käännöksiä päivitetty.

## Muutokset versiossa 2.3

* Lisätty bulgariankielinen käännös.

## Muutokset versiossa 2.2

* Lisätty seuraavat käännökset: arabia, aragonia, brasilianportugali, espanja, galego, hollanti, italia, japani, korea, kroatia, nepali, puola, ranska, saksa, slovakki, slovenia, suomi, tamili, turkki, unkari ja venäjä.

## Muutokset versiossa 2.1

* Päivitetty psutil-riippuvuus versioksi 0.6.1.
* Korjattu pitkä viive asemien tietoja haettaessa.
* Koodia siivottu.

## Muutokset versiossa 2.0

* Lisätty käännösten tuki ja käännöskommentteja.

## Muutokset versiossa 1.0

* Ensimmäinen versio

[1]: http://addons.nvda-project.org/files/get.php?file=resourceMonitor
