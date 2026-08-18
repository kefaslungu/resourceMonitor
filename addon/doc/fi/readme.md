# Resurssienvalvonta

* Tekijät: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst sekä muut NVDA-yhteisön jäsenet

Tämä lisäosa antaa tietoja suorittimen kuormituksesta sekä muistin ja muiden resurssien käytöstä.

## Pikanäppäimet

Kaikki komennot tukevat pyydettäessä-puhetilaa.

* NVDA+Vaihto+E: Ilmoittaa käytetyn RAM-muistin määrän, suorittimen keskimääräisen kuormituksen sekä akun tiedot, mikäli sellainen on käytettävissä.
* NVDA+Vaihto+1: Ilmoittaa suorittimen keskimääräisen kuormituksen ja lisäksi ytimien kuormituksen, mikäli kyseessä on moniydinsuoritin.
* NVDA+Vaihto+2/5: Ilmoittaa sekä fyysisen että näennäisen RAM-muistin käytetyn ja kokonaismäärän.
* NVDA+Vaihto+3: Ilmoittaa kiintolevyjen ja siirrettävien asemien käytetyn ja kokonaistilan.
* NVDA+Vaihto+4: Ilmoittaa langattoman verkon tiedot, kuten SSID-nimen ja signaalin voimakkuuden tai "SSID:tä ei löydy", jos verkkoa ei ole käytettävissä.
* NVDA+Vaihto+6: Ilmoittaa suorittimen arkkitehtuurin sekä Windowsin ja Service Packin version.
* NVDA+Vaihto+7: Ilmoittaa järjestelmän käynnissäoloajan.
* Unassigned: presents information about the graphics processing unit (GPU; unavailable in secure mode).
* Unassigned: presents graphics processing unit (GPU memory usage information; unavailable in secure mode).

Voit muuttaa näitä pikanäppäimiä Näppäinkomennot-valintaikkunasta.

## Huomautuksia käytöstä

Tämä lisäosa ei korvaa Windowsin tehtävienhallintaa tai muita järjestelmätietoja näyttäviä ohjelmia. Ota lisäksi huomioon seuraavat seikat:

* Apart from overall resource usage command (NVDA+Shift+E), pressing other commands twice will copy resource usage information to the clipboard.
* Resurssitietoja ei voi kopioida leikepöydälle, jos lisäosaa käytetään suojatuissa ruuduissa.
* Suorittimen käyttö ilmoitetaan loogisille suorittimille, ei fyysisille ytimille. Tällä on merkitystä Hyper Threading -teknologiaa käyttävissä suorittimissa, joissa suorittimien määrä on kaksi kertaa ydinten määrä. Joissakin uudemmissa tietokoneissa Hyper Threading ei ole käytössä kaikilla suoritinytimillä.
* Levynkäyttötietoja haettaessa saattaa olla viivettä, mikäli levytoimintaa, kuten suurten tiedostojen kopiointia, on runsaasti.
* GPU information is given for Nvidia GPU's.
* Suorittimen arkkitehtuuritietoja ilmoitettaessa "x86" ja "AMD64" viittaavat 32- ja 64-bittisiin (x64) Intel- ja AMD-suorittimiin.
* Tämän lisäosan asentamista ei tueta Windows 10:n/11:n LTSC-versioissa.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
