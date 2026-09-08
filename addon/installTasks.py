# resourceMonitor/installTasks.py
# Copyright 2026 Joseph Lee, released under GPL.

# Registers add-on config spec/settings blueprint.

import config
confspecRegistrationAvailable = hasattr(config, "configSections")

def onInstall() -> None:
	# Register this add-on's settings with NVDA's configuration system.
	# If running NVDA 2026.3, register the confspec here, otherwise do it from the main global plugin module.
	if not confspecRegistrationAvailable:
		return
	confspec = {
		"gpuTempUnit": "string(default=celsius)",
	}
	config.configSections.registerSection("resourceMonitor", confspec, isBaseOnly=True)
