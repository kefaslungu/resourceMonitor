# resource Monitor #

* Автори: Alex Hall, Joseph Lee, beqa gozalishvili та інші учасники
  спільноти NVDA
* Stable version: [version 2.4][1]
* Development version: [version 3.0-dev][2]

Цей плагін надає інформацію про завантаженість процесора, використання
пам'яті, дисків і статус батареї.

# Гарячі клавіші #

* NVDA+Shift+E Надає інформацію про використання оперативної пам'яті,
  середню завантаженість процесора та батарею, якщо така є,
* NVDA+Shift+1 Надає інформацію про середню завантаженість процесора і про
  завантаженість кожного ядра,
* NVDA+Shift+2/5 Надає інформацію про зайнятий та повний об'єм як фізичної,
  так і віртуальної пам'яті,
* NVDA+Shift+3 надає інформацію про зайнятий та повний об'єм статичних та
  переносних дисків, підключених до комп'ютера,
* NVDA+Shift+4 Повідомляє про відсоток батареї, статус заряджання, час, що
  залишився (якщо батарея не заряджається) і попередження про низький та
  критично низький заряд батареї.
* NVDA+Shift+6 Presents currently installed Windows version, CPU bit (32 or
  64-bit) and service pack if any (version 3.0-dev).

## Usage notes ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper Threading where number of CPU's
  is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## Changes for 3.0-dev ##

* Updated psutil dependency to 1.2.1.
* Added a command (NVDA+Shift+6) to report the version of Windows you are
  using, CPU bit and service packs if any.
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## Зміни у версії 2.4 ##

* Нові мови: китайська (традиційне письмо) та українська.
* Оновлено переклади.

## Зміни у версії 2.3 ##

* Додано болгарську мову інтерфейсу.

## Зміни у версії 2.2 ##

* Додано aragonese, Galatian, арабську, іспанську, італійську, корейську,
  непальську, нідерландську, німецьку, польську, португальську (Бразилія),
  російську, словацьку, словенську, тамільську, турецьку, угорську, фінську,
  французьку, хорватську та японську мови.

## Зміни у версії 2.1 ##

* Оновлено psutil dependency до versії 0.6.1.
* Виправлено велику затримку при отриманні інформації про диски.
* %s-es замінено на {нормальніЗмінні}.
* Трохи почищено код.

## Зміни у версії 2.0 ##

* Додано підтримку перекладів і коментарів до них.

## Зміни у версії 1.0 ##

* Перший реліз

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
