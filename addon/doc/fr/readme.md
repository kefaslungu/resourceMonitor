# Resource Monitor

* Auteurs : Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst et d'autres contributeurs de NVDA

Cette extension fournit des informations sur la charge du processeur, l'utilisation de la mémoire et d'autres informations sur l'utilisation des ressources.

## Raccourcis

Toutes les commandes prennent en charge le mode parole à la demande.

* NVDA+Maj+E: Annonce le pourcentage de mémoire utilisée, la charge moyenne du processeur et des informations sur la batterie si disponibles.
* NVDA+Maj+1: Annonce la charge moyenne du processeur et, pour les processeurs  multi cœur la charge de chaque cœur.
* NVDA+Maj+2/5: Annonce les quantités d'espace mémoire physique et virtuelle utilisées et totales.
* NVDA+Maj+3: Annonce les quantités d'espace utilisé et total des disques fixes et amovibles.
* NVDA+Maj+4: Annonce des informations sur la connexion sans fil, le nom et la force SSID, ou pas de SSID s'il n'y en a pas disponible.
* NVDA+Maj+6: Annonce l'architecture du processeur et les numéros de version de Windows et du service pack.
* NVDA+Maj+7: Annonce le temps de fonctionnement du système depuis sa mise en route.
* Unassigned: presents information about the graphics processing unit (GPU; unavailable in secure mode).
* Unassigned: presents graphics processing unit (GPU memory usage information; unavailable in secure mode).

Vous pouvez modifier ces touches de raccourci dans le dialogue Gestes de commandes.

## Remarques sur l'utilisation

Cette extension ne remplace pas le gestionnaire de tâches et les autres programmes d'information système pour Windows. Aussi, notez ce qui suit :

* Apart from overall resource usage command (NVDA+Shift+E), pressing other commands twice will copy resource usage information to the clipboard.
* Les informations sur les ressources ne peuvent pas être copiées dans le presse-papiers si vous exécutez l'extension dans des écrans sécurisés.
* L'utilisation du processeur est donnée pour les processeurs logiques, non pour les cœurs physiques. Cela est perceptible pour les processeurs qui utilise la technologie Hyper Threading où le nombre de CPU est deux fois le nombre de cœurs du processeur. Sur certains ordinateurs plus récents, tous les cœurs du CPU ne seront pas activés par l'Hyper Threading.
* Si l'activité du disque est lourde, comme la copie de fichiers volumineux, il peut y avoir des retards lors de l'obtention d'informations sur l'utilisation du disque.
* GPU information is given for Nvidia GPU's.
* Lors de l'annonce des informations d'architecture du processeur, "x86" et "AMD64" se réfèrent aux processeurs Intel et AMD 32 bits et 64 bits (x64), respectivement.
* L'installation de l'extension sur Windows 10/11 LTSC n'est pas prise en charge.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
