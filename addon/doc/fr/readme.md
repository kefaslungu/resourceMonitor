# Resource Monitor #

* Auteurs : Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst et d'autres contributeurs de NVDA

Cette extension fournit des informations sur la charge du processeur,
l'utilisation de la mémoire et d'autres informations sur l'utilisation des
ressources.

# Raccourcis

Toutes les commandes prennent en charge le mode parole à la demande.

* NVDA+Maj+E: Annonce le pourcentage de mémoire utilisée, la charge moyenne
  du processeur et des informations sur la batterie si disponibles.
* NVDA+Maj+1: Annonce la charge moyenne du processeur et, pour les
  processeurs  multi cœur la charge de chaque cœur.
* NVDA+Maj+2/5: Annonce les quantités d'espace mémoire physique et virtuelle
  utilisées et totales.
* NVDA+Maj+3: Annonce les quantités d'espace utilisé et total des disques
  fixes et amovibles.
* NVDA+Maj+4: Annonce le pourcentage de charge de la batterie, l'état de
  charge si elle est en charge, le temps restant (sauf si en charge), et une
  alerte si le niveau de la batterie est faible ou critique.
* NVDA+Maj+6: Annonce l'architecture du processeur et les numéros de version
  de Windows et du service pack.
* NVDA+Maj+7: Annonce le temps de fonctionnement du système depuis sa mise
  en route.
* NVDA+Maj+8: Annonce des informations sur la connexion sans fil, le nom et
  la force SSID, ou pas de SSID s'il n'y en a pas disponible.

Vous pouvez modifier ces touches de raccourci dans le dialogue Gestes de
commandes.

## Remarques sur l'utilisation

Cette extension ne remplace pas le gestionnaire de tâches et les autres
programmes d'information système pour Windows. Aussi, notez ce qui suit :

* Les informations sur les ressources ne peuvent pas être copiées dans le
  presse-papiers si vous exécutez l'extension dans des écrans sécurisés.
* L'utilisation du processeur est donnée pour les processeurs logiques, non
  pour les cœurs physiques. Cela est perceptible pour les processeurs qui
  utilise la technologie Hyper Threading où le nombre de CPU est deux fois
  le nombre de cœurs du processeur. Sur certains ordinateurs plus récents,
  tous les cœurs du CPU ne seront pas activés par l'Hyper Threading.
* Si l'activité du disque est lourde, comme la copie de fichiers volumineux,
  il peut y avoir des retards lors de l'obtention d'informations sur
  l'utilisation du disque.
* Lors de l'annonce des informations d'architecture du processeur, "x86" et
  "AMD64" se réfèrent aux processeurs Intel et AMD 32 bits et 64 bits (x64),
  respectivement.
* Cette extension requiert Windows 10 22H2 (2022 Update/build 19045) ou
  au-delà.
* L'installation de l'extension sur Windows 10/11 LTSC n'est pas prise en
  charge.

## Version 25.07

* Rendu le code de l'extension plus robuste avec l'aide de Pyright (un
  vérificateur de type statique Python).

## Version 25.06

* Amélioration de l'annonce de l'état de la connexion lors de la connexion
  aux réseaux sans fil (@danstiv).

## Version 25.02

* Restauré prise en charge limitée pour Windows 8.1.
* Amélioration de la précision de l'annonce d'informations de mémoire
  utilisée et totale (@danstiv).
* NVDA ne semblera plus geler brièvement lors de l'exécution de la commande
  d'utilisation de la mémoire (NVDA+Maj+2/5) la première fois après le
  démarrage de NVDA.
* Les versions Windows Insider Preview ne sont plus signalées comme "Windows
  Insider".

## Version 24.08

* NVDA 2024.2 ou version ultérieure est requis. Cela permet de supprimer la
  dépendance psutil de l'extension car NVDA l'inclut.
* Mise à jour de la dépendance psutil  vers la version incluse avec NVDA
  2024.2 (6.0.0).
* Ruff remplace Flake8 comme code linter.

## Version 24.05

* NVDA 2024.1 ou version ultérieure est requis.
* NVDA reconnaîtra les réseaux sans fil avec des méthodes d'authentification
  WPA3 telles que l'authentification simultanée d'égaux (SAE).

## Version 24.04

* Mise à jour de la dépendance psutil vers la version 5.9.8.
* Ajout de la prise en charge du mode parole à la demande afin que les
  informations sur les ressources puissent être annoncées dans ce mode.

## Version 23.11

* Dépendance psutil rétrogradée à 5.9.4 en raison de problèmes avec les
  annonces d'utilisation de la mémoire.

## Version 23.10

* Mise à jour de la dépendance psutil vers la version 5.9.5.

## Version 23.09

* NVDA ne journalisera plus les messages d'erreur de démarrage sur les
  systèmes Windows Server lorsque les modules de capacité sans fil ne sont
  pas disponibles.

## Version 23.06

* La situation où resourceMonitor ne fonctionne pas correctement en raison
  de l'indisponibilité des adaptateurs sans fil a été corrigé.

## Version 23.05.1

wlanReporter NVDA-addon fait maintenant partie de resourceMonitor !

* L'ancienne façon de vérifier les connexions sans fil a été remplacée par
  l'API Windows de wlanReporter: https://github.com/kvark128/WlanReporter/ .

	* Après avoir annoncé le nom et la force SSID, NVDA vous dira également le
	  type de sécurité de votre réseau.
	* NVDA vous alertera désormais lorsque vous vous connectez et vous
	  déconnectez d'un réseau sans fil.
	* NVDA vous alertera désormais lorsque les connexions sans fil sont
	  activées ou désactivées.

## Version 23.05

* ajout de la possibilité de détecter et de présenter l'état du réseau sans
  fil connecté.

	* Annonce le nom du SSID sans fil connecté.
	* Annonce la force du SSID
	* Annoncez SSID non trouvé si aucun n'est détecté.

## Version 23.02

* NVDA 2022.4 ou version ultérieure est requis.
* Windows 10 21H2 (November 2021 Update/build 19044) ou au-delà est requis.

## Version 23.01

* NVDA 2022.3 ou version ultérieure est requis.
* Windows 10 ou ultérieure est requis car Windows 7, 8 et 8.1 ne sont plus
  pris en charge par Microsoft en janvier 2023.
* Mise à jour de la dépendance psutil vers la version 5.9.4.
* NVDA annoncera l'architecture du processeur actuel (x86 / AMD64 / ARM64)
  avec les informations de version de Windows.
* Sur les systèmes d'un seul cœur, NVDA n'annoncera plus la charge du cœur
  du processeur car la charge moyenne du processeur est la même que la
  charge du cœur.

## Version 22.03

La version 22.03 est la dernière version stable à prendre en charge Windows
7 Service Pack 1, 8 et 8.1.

* NVDA 2021.3 ou version ultérieure est requis.
* Un message d'avertissement s'affichera si vous installez l'extension sur
  Windows 7, 8 et 8.1.
* Mise à jour de la dépendance psutil vers la version 5.9.0.

## Version 22.01

* NVDA 2021.2 ou version ultérieure est requis.

## Version 21.10

* NVDA 2021.1 ou ultérieur est requis en raison de modifications apportées à
  NVDA qui affectent cette extension.

## Version 21.08

* L'exigence de version minimale de Windows est désormais liée aux versions
  de NVDA.
* Les builds Windows 20348 et 22000 sont respectivement reconnues comme
  Windows Server 2022 et Windows 11.
* Sur les builds Insider Preview, les versions de Windows telles que
  "Windows 10" ne seront pas utilisées. Au lieu de cela, NvDA annoncera
  "Windows Insider".
* Sur les systèmes 64 bits, l'architecture du processeur (x64 ou ARM64) sera
  annoncée avec les informations de version de Windows.

## Version 21.04

* NVDA 2020.4 ou version ultérieure est requis.
* Mise à jour de la dépendance psutil vers la version 5.8.0.
* Lorsqu'on appuie deux fois sur une commande de l'extension pour copier les
  informations sur les ressources dans le presse-papiers, NVDA annoncera le
  résumé des ressources copiés.

## Version 21.01

* Mise à jour de la dépendance psutil vers la version 5.7.3.
* Message de version Windows raccourci.
* Sous Windows 8.1, build.revision sera annoncé dans le message de version
  de Windows, de manière similaire à Windows 10.

## Version 20.09

* Le temps de fonctionnement du système est maintenant indiqué en jours,
  heures, minutes, secondes.
* Windows Server Insider Preview build 20201 ou au-delà est correctement
  reconnu comme une build Server Insider.

## Version 20.07

* Windows 10 Version 20H2 est correctement reconnue quand on obtient les
  informations de version de Windows (NVDA+maj+6).
* Simplification du message de version de Windows 10 ex: Windows 10 AAMM au
  lieu de Windows 10verAAMM lors de l'appui sur NVDA+Shift+6.

## Version 20.06

* Résolution de beaucoup de problèmes de style de code et de bogues
  potentiels avec Flake8.

## Version 20.04

* Mise à jour de la dépendance psutil vers la version 5.7.0.

## Version 20.01

* NVDA 2019.3 ou au-delà est requis en raison d'une utilisation importante
  de Python 3.

## Version 19.11

* Amélioration de la détection des builds de Windows Insider Preview, en
  particulier pour20h1 et au-delà.

## Version 19.07

* Mise à jour de la dépendance psutil vers la version 5.6.3.
* Changements internes dans la commande d'annonce de l'état de la batterie.

## Version 18.12

* Changements internes pour supporter de futures versions de NVDA.

## Version 18.10

* Le code a été rendu plus compatible avec Python 3.
* Mise à jour de la dépendance psutil vers la version 5.4.7.
* Lors de l’obtention de la capacité des disques et de l’utilisation de la
  mémoire, NVDA ne donne plus d'erreur si vous utilisez un ordinateur ou un
  service contenant plus d’un pétaoctet de RAM ou d'espace disque.
* Les valeurs pour l’utilisation de la mémoire et le disque sont montrées
  avec deux décimales (par exemple 4.00 Go au lieu de 4.0 Go).
* Amélioration de la détection des builds de Windows Insider Preview.

## Version 18.04

La version 18.04.x est la dernière version à prendre en charge les versions
de Windows antérieures à 7 SP1.

* La dernière version à prendre en charge Windows Server 2003, Vista et
  Server 2008.
* Meilleure détection des versions de Windows 10 et distinction entre les
  versions publiques et les versions d'Insider Preview.

## Version 17.12

* Ajout du support pour les processeurs ARM 64 bits sur Windows 10.

## Version 17.09

Important : la version 17.09.x est la dernière version compatible avec
Windows XP.

* Dernière version à fonctionner sous Windows XP.
* Windows 10 build 16278 et versions ultérieures est reconnu comme Version
  1709. Une révision mineure pour cette extension sera publié une fois que
  la version stable de la build 1709 sera publiée.

## Version 17.07.1

* Réintroduit le support de Windows XP (cassé depuis la version 17.02).

## Version 17.05

* Annonce du temps de bon fonctionnement du système (temps passé depuis le
  dernier démarrage, NVDA+Maj+7).

## Version 17.02

* Mise à jour de la dépendance psutil vers la version 5.0.1.
* Lors de la vérification de l'utilisation du disque, NVDA ne présentera
  plus de dialogue d'erreur sur certains systèmes où un support amovible
  n'est pas correctement reconnu (par exemple lorsqu'une carte n'est pas
  insérée dans un lecteur de carte).)

## Version 16.08

À partir de la version 16.08, les versions pour cette extension seront de la
forme année.mois.révision.

* Diverses révisions de Windows 10 sont maintenant correctement reconnues
  (tels que la 1607 pour la build 14393).
* Les révisions de build de Windows 10 (après l'installation des mises à
  jour cumulatives) sont correctement reconnues (tels que la 14393.51).
* Si vous utilisez une build Insider Preview, celle-ci sera reconnue.

## Changements pour la version 4.5

* Le référentiel de l'extension a été déplacé vers GitHub (peut être trouvé
  sur https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 est correctement reconnu.

## Changements pour la version 4.0

* Mise à jour de la dépendance psutil  vers la version 2.2.1.
* Nette amélioration des performances lors de l'obtention d'informations sur
  la charge du processeur.
* Ajout du support pour la reconnaissance de Windows 10.
* Dans Windows 10, le numéro de build de Windows est également annoncé.
* Vous pouvez utiliser le Gestionnaire d'extensions pour accéder à l'aide de
  l'extension.

## Changements pour la version 3.1

* Resource Monitor prend officiellement en charge Windows 8.1.
* Mise à jour des traductions.

## Changements pour la version 3.0

* Mise à jour de la dépendance psutil  vers la version 1.2.1.
* Annonce la version en cours de Windows, l'architecture du processeur et le
  service pack le cas échéant (NVDA+Maj+6).
* Possibilité de modifier les touches de raccourci de l'extension (NVDA
  2013.3 ou version ultérieure).
* Possibilité de copier les informations de la ressource individuelle dans
  le presse-papiers en appuyant deux fois sur commandes ressource.

## Changements pour la version 2.4

* Nouvelles langues: Chinois (simplifié), Ukrainien.
* Mise à jour des traductions.

## Changements pour la version 2.3

* Ajout de la traduction en bulgare.

## Changements pour la version 2.2

* Ajout des traductions suivantes : Arabe, Aragonais, Néerlandais, Finnois,
  Français, Galicien, Allemand, Croate, Hongrois, Italien, Japonais, Coréen,
  Népalais, Portugais (Brésilien), Russe, Slovaque, Slovène, Espagnol,
  Tamoul et Turque.

## Changements pour la version 2.1

* Mise à jour de la dépendance psutil  vers la version 0.6.1.
* Correction du long délai lors de l'obtention des informations des disques.
* Nettoyage du code.

## Changements pour la version 2.0

* ajout d'un support de traduction et de commentaires de traduction.

## Changements pour la version 1.0

* Première version

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
