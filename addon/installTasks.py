# resourceMonitor/installTasks.py
# Copyright 2026 Joseph Lee, released under GPL.

# Registers add-on config spec/settings blueprint.

import config

def onInstall() -> None:
	# Register this add-on's settings with NVDA's configuration system.
	# The global plugin main module version serves as a fallback in case custom sections data is gone.
	confspec = {
		"gpuTempUnit": "string(default=celsius)",
		"memorySizeUnit": "string(default=alternative)",
		"wifiStatusNotification": "option('off', 'message', 'sound', 'both', default='both')",
	}
	config.configSections.registerSection("resourceMonitor", confspec, isBaseOnly=True)
