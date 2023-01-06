# resourceMonitor/installTasks.py
# Copyright 2017-2023 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
addonHandler.initTranslation()


def onInstall():
	import gui
	import wx
	import winVersion
	import globalVars
	# Do not present dialogs if minimal mode is set.
	currentWinVer = winVersion.getWinVer()
	# Resource Monitor requires Windows 10 21H2 or later.
	# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
	# Unsupported systems include Windows versions earlier than 10 and unsupported feature updates.
	unsupportedWindowsReleaseTitle = _("Unsupported Windows release")
	minimumWinVer = winVersion.WIN10_21H2
	if currentWinVer < minimumWinVer:
		if not globalVars.appArgs.minimal:
			gui.messageBox(
				_(
					# Translators: Dialog text shown when trying to install the add-on on
					# releases earlier than minimum supported release.
					"You are using {releaseName} ({build}), a Windows release not supported by this add-on.\n"
					"This add-on requires {supportedReleaseName} ({supportedBuild}) or later."
				).format(
					releaseName=currentWinVer.releaseName,
					build=currentWinVer.build,
					supportedReleaseName=minimumWinVer.releaseName,
					supportedBuild=minimumWinVer.build
				), unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR
			)
		raise RuntimeError("Attempting to install Resource Monitor add-on on Windows releases earlier than 10")
