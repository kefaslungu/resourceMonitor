# Monitor resursa

* Autori: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst i drugi NVDA saradnici

Ovaj dodatak pruža informacije o opterećenju procesora, iskorišćenoj memoriji i druge informacije o korišćenju resursa.

## Prečice

All commands support speech on demand mode.

* NVDA+Šift+E: Prikazuje iskorišćeni RAM, prosečno opterećenje procesora i informacije o bateriji ako su dostupne.
* NVDA+Šift+1: Prikazuje prosečno opterećenje procesora i ako su prisutni procesori sa više jezgara opterećenost svakog jezgra.
* NVDA+Šift+2/5: Prikazuje iskorišćeni i ukupan prostor za fizički i virtuelni RAM.
* NVDA+Šift+3: prikazuje iskorišćeni i ukupan prostor statičkih diskova i diskova koji se mogu ukloniti.
* NVDA+Šift+4: prikazuje procenat baterije, status punjenja, preostalo vreme (ako se baterija ne puni) i upozorenje ako je baterija slaba ili kritična.
* NVDA+Šift+6: prikazuje arhitekturu procesora, Windows verziju i brojeve servisnog paketa.
* NVDA+Šift+7: prikazuje vreme rada sistema.
* NVDA+Šift+8: prikazuje informacije o bežičnoj mreži, ssid ime i jačinu, ili bez ssid-a ako nema povezane mreže.

Možete promeniti ove prečice iz dijaloga ulaznih komandi.

## Napomene o korišćenju

Ovaj dodatak ne menja upravljača zadacima i druge programe za informacije o sistemu za Windows. Takođe imajte sledeće na umu:

* Informacije o resursima se ne mogu kopirati u privremenu memoriju ako pokrećete dodatak na bezbednim ekranima.
* Iskorišćenost procesora se pruža za logičke procesore, ne fizička jezgra. Ovo se može uočiti na procesorima koji koriste Hyper-Threading na kojima je broj procesora dva puta veći u odnosu na broj jezgara procesora. Na nekim novijim računarima, neće sva jezgra procesora imati hyper-threading omogućen.
* Ako je u toku zahtevna aktivnost na disku kao što je kopiranje velikih datoteka, može doći do kašnjenja prilikom preuzimanja informacija o iskorišćenosti diskova.
* Kada se izgovaraju informacije o arhitekturi procesora, "x86" i "AMD64" se odnose na 32-bitne i 64-bitne (x64) Intel i AMD procesore.
* This add-on requires Windows 10 22H2 (2022 Update/build 19045) or later.
* Installing the add-on on Windows 10/11 LTSC is not supported.
