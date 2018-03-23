# Resource Monitor #

* Auteurs : Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala et
  d'autres contributeurs de NVDA
* Télécharger [version stable][1]

Ce module complémentaire fournit des informations sur la charge du CPU,
l'utilisation de la mémoire et d'autres informations sur l'utilisation des
ressources.

# Raccourcis #

* NVDA+Maj+E Présente l'espace de mémoire utilisée, la charge moyenne du
  processeur, et les informations sur la batterie si disponibles.
* NVDA+Maj+1 Présente la charge moyenne du processeur si le CPU multi coeur
  est présent à la charge de chaque coeur.
* NVDA+Maj+2/5 Présente les quentités d'espace mémoire physique et virtuelle
  totales et utilisées.
* NVDA+Maj+3 Présente les quentités d'espace total et utilisé des disques
  statiques et amovibles.
* NVDA+Maj+4 Présente le pourcentage de chargement de la batterie, l'état de
  charge si elle est en charge, le temps restant (sauf si en charge), et une
  alerte si le niveau de la batterie est faible ou critique.
* NVDA+Maj+6 Présente l'architecture CPU 32/64-bit et   les numéros de
  version de Windows et le service pack.
* NVDA+Maj+7 présente le temps de bon fonctionnement du système.

Si vous avez NVDA 2013.3 ou version ultérieure installé, vous pouvez
modifier ces touches de raccourci.

## Remarques sur l'utilisation ##

Ce module complementaire ne remplace pas le gestionnaire de tâches et les
autres programmes d'information système pour Windows. Aussi, notez ce qui
suit :

* L'utilisation du CPU est donnée pour les processeurs logiques, coeurs non
  physiques. Cela est perceptible pour les processeurs qui utilise la
  technologie Hyper Threading où le nombre de CPU est deux fois le nombre de
  coeurs du processeur.
* Si l'activité du disque est lourde, comme la copie de fichiers volumineux,
  il peut y avoir des retards lors de l'obtention d'informations sur
  l'utilisation du disque.
* Support for Windows XP from this add-on ended on December 31,
  2017. Support for Windows Server 2003, Vista and Server 2008 will end on
  June 30, 2018.

## Version 18.04

Version 18.04.x is the last release to support Windows releases earlier than
7 SP1.

* Last release to support Windows Server 2003, Vista and Server 2008.
* Better detection of Windows 10 releases and distinguishing between public
  and Insider Preview builds.

## Version 17.12

* Ajout du support pour les processeurs ARM 64 bits sur Windows 10.

## Version 17.09

Important : la version 17.09.x est la dernière version compatible avec
Windows XP.

* Dernière version à exécuter sur Windows XP.
* Windows 10 build 16278 et versions ultérieures est reconnu comme Version
  1709. Une révision mineure pour ce module complémentaire sera publié une
  fois que la version stable de la build 1709 sera publiée.

## Version 17.07.1

* Réintroduire le support pour Windows XP (cassé depuis la version 17.02).

## Version 17.05

* Annonce le temps de bon fonctionnement du système (temps passé depuis le
  dernier démarrage, NVDA+Maj+7).

## Version 17.02

* Mise à jour de la dépendance psutil vers la version 5.0.1.
* Lors de la vérification de l'utilisation du disque, NVDA ne présentera
  plus de boîte de dialogue d'erreur sur certains systèmes où un support
  amovible n'est pas correctement reconnu (par exemple lorsqu'une carte
  n'est pas insérée dans un lecteur de carte).)

## Version 16.08

À partir de la version 16.08, les publications pour le module complémentaire
sera affiché comme year.month.revision.

* Diverses révisions de Windows 10 sont maintenant correctement reconnues
  (tels que la 1607 pour la build 14393).
* Windows 10 build revisions (après l'installation des mises à jour
  cumulatives) sont correctement reconnues (tels que la 14393.51).
* Si en utilisant la build Insider Preview, ceci est sûr qui va être
  reconnu.

## Changements pour la version 4.5 ##

* Le référentiel du module complémentaire a été déplacé à GitHub (peut être
  trouvé à https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 est correctement reconnu.

## Changements pour la version 4.0 ##

* Mise à jour de la dépendance psutil  vers la version 2.2.1.
* Nettement améliorée les performances lors de l'obtention d'informations
  sur la charge du CPU.
* Ajout du support pour la reconnaissance de Windows 10.
* Dans Windows 10, le numéro de build de Windows est également annoncé.
* Vous pouvez utiliser le Gestionnaire de modules complémentaires pour
  accéder à l'aide du module complémentaire.

## Changements pour la version 3.1 ##

* Resource Monitor officiellement prend en charge Windows 8.1.
* Mise à jour des traductions.

## Changements pour la version 3.0 ##

* Mise à jour de la dépendance psutil  vers la version 1.2.1.
* Présente l'actuelle  version de Windows, l'architecture du CPU et le
  service pack le cas échéant (NVDA+Maj+6).
* Possibilité de modifier les touches de raccourci pour le module
  complémentaire (NVDA 2013.3 ou version ultérieure).
* Possibilité de copier les informations de la ressource individuelle dans
  le presse-papiers en appuyant sur commandes ressource deux fois.

## Changements pour la version 2.4 ##

* Nouvelles langues: Chinois (simplifié), Ukrainien.
* Mise à jour des traductions.

## Changements pour la version 2.3 ##

* Ajout de la traduction en bulgare.

## Changements pour la version 2.2 ##

* Ajout des traductions suivantes : Arabe, Aragonais, Croate, Néherlandais,
  Finnois, Français, Galicien, Allemand, Hongrois, Italien, Japonais,
  Koréen, Népalais, Portuguais (Brésile), Russe, Slovak, Slovénien,
  Espagnol, Tamoul et Turque.

## Changements pour la version 2.1 ##

* Mise à jour de la dépendance psutil  vers la version 0.6.1.
* Correction du long délai lors de l'optention des informations des disques
* Nettoyage du code.

## Changements pour la version 2.0 ##

* Ajout du support des traductions et des commentaires pour les traducteurs.

## Changements pour la version 1.0 ##

* Première version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
