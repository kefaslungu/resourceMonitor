# resourceMonitor/installTasks.py
# Copyright 2017-2023 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
addonHandler.initTranslation()


def onInstall():
	import winVersion
	import gui
	import wx
	if winVersion.getWinVer() < winVersion.WIN10:
		gui.messageBox(
			_(
				# Translators: Dialog text shown when trying to install the add-on on an older version of Windows.
				"You are using an older version of Windows. This add-on requires Windows 10 or later."
			),
			# Translators: title of the dialog shown when trying to install the add-on on an old version of Windows.
			_("Old Windows version"), wx.OK | wx.ICON_WARNING
		)
		raise RuntimeError("Attempting to install Resource Monitor add-on on Windows releases earlier than 10")
