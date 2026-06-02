# Resurssienvalvonta

* Tekijät: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst sekä muut NVDA-yhteisön jäsenet

Tämä lisäosa antaa tietoja suorittimen kuormituksesta sekä muistin ja muiden resurssien käytöstä.

## Pikanäppäimet

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
