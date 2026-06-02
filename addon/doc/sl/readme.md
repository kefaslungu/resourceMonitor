# Nadzornik porabe

* Avtorji: Alex Hall, Joseph Lee, beqa gozalishvili in drugi NVDA sodelujoči

This plugin gives information about CPU load, memory usage, battery and disk usage status.

## Bližnjice

* NVDA+Shift+E Presents used ram, average processor load, and battery info if available,
* NVDA+Shift+1 Presents the average processor load and the load of each core,
* NVDA+Shift+2/5 Presents the used and total space for both physical and virtual ram,
* NVDA+Shift+3 Presents the used and total space of the static and removable drives on this computer,
* NVDA+Shift+4 Presents battery percentage, charging status, remaining time (if not charging), and a warning if the battery is low or critical,
* NVDA+Shift+6 Presents currently installed Windows version, CPU bit (32 or 64-bit) and service pack if any (version 3.0-dev).

## Opombe k uporabi

This add-on does not replace task manager and other system information programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper Threading where number of CPU's is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.
