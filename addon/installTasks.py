# resourceMonitor/installTasks.py
# Copyright 2026 Joseph Lee, released under GPL.

# Registers add-on config spec/settings blueprint.

import config
import gui

def onInstall() -> None:
	# Register this add-on's settings with NVDA's configuration system.
	# The global plugin main module version serves as a fallback in case custom sections data is gone.
	confspec = {
		"layerEntryONFirstPress": "bool(default=true)",
		"gpuTempUnit": "string(default=celsius)",
		"memorySizeUnit": "string(default=alternative)",
		"wifiStatusNotification": "option('off', 'message', 'sound', 'both', default='both')",
	}
	config.configSections.registerSection("resourceMonitor", confspec, isBaseOnly=True)
	# Temporary: display NVDA+Shift+number row command deprecation notice (replaced by the layer commands set).
	gui.MessageDialog.alert(
		_( # Translators: dialog text informing users about deprecation of NVDA+Shift+number row commands.
			"""The NVDA+Shift+number row commands used to obtain individual resource information such as NVDA+Shift+1 for CPU load are deprecated.\n
Please use Resource Monitor layer commands (NVDA+Shift+E followed by a shortcut key) to obtain resource information as follows:\n
Overall resource usage: Space, CPU load: C, disk usage: D, GPU overview: G, GPU memory: Shift+G,\n
memory usage: M, OS (Windows) version and architecture: O, system uptime: U, wi-fi status: W.\n
After obtaining resource usage via the layer commands, press Escape to exit the layer.\n
Note: you can assign keyboard shortcuts for individual Resource Monitor layer commands from input gestures dialog."""
		),
		# Translators: dialog title for NVDA+Shift+number row commands deprecation/warning notice.
		_("Resource Monitor commands warning"),
	)
