# Resource Monitor #

* Auteurs : Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst et d'autres contributeurs de NVDA
* Télécharger [version stable][1]
* NVDA compatibility: 2020.4 to 2021.1

Cette extension fournit des informations sur la charge du processeur,
l'utilisation de la mémoire et d'autres informations sur l'utilisation des
ressources.

# Raccourcis

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
* NVDA+Maj+6: Annonce l'architecture du processeur 32/64-bit et les numéros
  de version de Windows et du service pack.
* NVDA+Maj+7: Annonce le temps de fonctionnement du système depuis sa mise
  en route.

Si vous avez NVDA 2013.3 ou version ultérieure installé, vous pouvez
modifier ces touches de raccourci dans le dialogue Gestes de commandes.

## Remarques sur l'utilisation

Cette extension ne remplace pas le gestionnaire de tâches et les autres
programmes d'information système pour Windows. Aussi, notez ce qui suit :

* L'utilisation du processeur est donnée pour les processeurs logiques, non
  pour les cœurs physiques. Cela est perceptible pour les processeurs qui
  utilise la technologie Hyper Threading où le nombre de CPU est deux fois
  le nombre de cœurs du processeur.
* Si l'activité du disque est lourde, comme la copie de fichiers volumineux,
  il peut y avoir des retards lors de l'obtention d'informations sur
  l'utilisation du disque.
* Cette extension requiert Windows 7 Service Pack 1 ou au-delà.

## Version 21.04

* Nécessite NVDA 2020.4 ou au-delà.
* Mise à jour de la dépendance psutil vers la version 5.8.0.
* Lorsqu'on appuie deux fois sur une commande de l'extension pour copier les
  informations sur les ressources dans le presse-papiers, NVDA annoncera le
  résumé des ressources copié

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
* Correction du long délai lors de l'obtention des informations des disques
* Nettoyage du code.

## Changements pour la version 2.0

* Ajout du support des traductions et des commentaires pour les traducteurs.

## Changements pour la version 1.0

* Première version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
