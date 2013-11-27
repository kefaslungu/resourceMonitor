# resource Monitor #

* Auteurs : Alex Hall, Joseph Lee, beqa gozalishvili et d'autres
  contributeurs de NVDA
* Version stable : [version 2.4][1]
* Version de développement : [version 3.0-dev][2]

Ce module complémentaire donne la charge moyenne du CPU, l'utilisation de la
mémoire, et l'état d'utilisation des disques et de la batterie.

# Raccourcis #

* NVDA+Maj+E Présente la quantité de mémoire utilisée, la charge moyenne du
  processeur, et les informations sur la batterie si disponibles.
* NVDA+Maj+1 Présente la charge moyenne du processeur et la charge de chaque
  coeur.
* NVDA+Maj+2/5 Présente les quentités de mémoire physique et virtuelle
  totales et utilisées.
* NVDA+Maj+3 Présente l'espace total et utilisé des disques de cet
  ordinateur.
* NVDA+Maj+4 Présente le pourcentage de chargement de la batterie, si elle
  est en charge, le temps restant (sauf si en charge), et une alerte si le
  niveau de la batterie est faible ou critique.
* NVDA+Shift+6 Presents currently installed Windows version, CPU bit (32 or
  64-bit) and service pack if any (version 3.0-dev).

## Remarques sur l'utilisation ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper Threading where number of CPU's
  is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## Changements pour la version 3.0-dev ##

* Updated psutil dependency to 1.2.1.
* Added a command (NVDA+Shift+6) to report the version of Windows you are
  using, CPU bit and service packs if any.
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## Changements pour la version 2.4 ##

* Nouvelles langues: Chinois (simplifié), Ukrainien.
* Mise à jour des traductions.

## Changements pour la version 2.3 ##

* Ajout de la traduction en bulgare.

## Changements pour la version 2.2 ##

* Ajout des traductions suivantes : Aragonais, Croate, Néherlandais,
  Finnois, Français, Galicien, Allemand, Hongrois, Italien, Koréen,
  Népalais, Portuguais (Brésile), Russe, Slovak, Slovénien, Espagnol, Tamoul
  et Turque.

## Changements pour la version 2.1 ##

* Mise à jour de la dépendance psutil  vers la version 0.6.1.
* Correction du long délai lors de l'optention des informations des disques
* Les %s ont été remplacés par des noms plus claires.
* Nettoyage du code.

## Changements pour la version 2.0 ##

* Ajout du support des traductions et des commentaires pour les traducteurs.

## Changements pour la version 1.0 ##

* Première version.

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
