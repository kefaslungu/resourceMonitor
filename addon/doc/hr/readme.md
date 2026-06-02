# Prati stanje resursa (Resource Monitor)

* Autori: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst i drugi NVDA doprinositelji

Ovaj dodatak daje informacije o opterećenosti procesora, korištenju memorije i druge informacije o korištenju resursa.

## Prečaci

All commands support speech on demand mode.

* NVDA+šift+E: Prikazuje korištenje ram memorije, prosječno opterećenje procesora i informacije o stanju baterije, ako su dostupne.
* NVDA+šift+1: Prikazuje prosječnu opterećenost procesora i ako postoje višejezgreni procesori, prikazuje opterećenje svake jezgre.
* NVDA+šift+2/5: Prikazuje korišteni i ukupni kapacitet fizičke I virtualne ram memorije.
* NVDA+šift+3: Prikazuje korišteni i ukupni prostor na statičnim i prenosivim diskovima.
* NVDA+šift+4: Prikazuje postotak baterije, stanje punjenja, preostalo vrijeme (ako se ne puni), te upozorenje, ako je baterija slaba ili skoro prazna.
* NVDA+šift+6: Prikazuje arhitekturu procesora, Windows verziju i broj service paketa.
* NVDA+šift+7: Prikazuje vrijeme neprekidnog rada sustava.
* NVDA+šift+8: prikazuje informacije o bežičnoj vezi, ime i snagu ssid-a ili ne prikazuje ssid ako nije dostupan.

Tipkovničke prečace je moguće mijenjati putem dijaloškog okvira za ulazne geste.

## Upute za primjenu

Ovaj dodatak ne zamijenjuje upravljača zadataka i druge programe za informacije o sustavu Windows. Važno je znati i sljedeće:

* Podaci o resursima ne mogu se kopirati u međuspremnik ako se dodatak pokreće na sigurnim ekranima.
* Informacije o korištenju procesora dane su za logičke procesore, ne za fizičke jezgre. To se može primijetiti kod procesora koji koriste Hyper-Threading gdje je broj procesora dvostruko veći od broja jezgri. Na nekim novijim računalima Hyper-Threading neće biti aktivirano za sve jezgre CPU-a.
* Ako je u tijeku velika aktivnost diska, kao što je kopiranje velikih datoteka, moguća su kašnjenja prilikom dobivanja informacija o korištenju diska.
* Kada se najavljuju informacije o arhitekturi procesora, „x86” i „AMD64” odnose se na 32-bitne i 64-bitne (x64) Intel odnosno AMD procesore.
* This add-on requires Windows 10 22H2 (2022 Update/build 19045) or later.
* Installing the add-on on Windows 10/11 LTSC is not supported.
