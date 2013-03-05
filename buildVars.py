# Build customizations
# Change this file instead of sconstruct, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
# add-on Name
	"addon-name" : "resourceMonitor",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on information.
	"addon-summary" : _("A handy resource monitor to report CPU load, memory usage, battery and disk usage status."),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon-description" : _("Allows you to monitor system information easily."),
	# version
	"addon-version" : "2.2-dev",
	# Author(s)
	"addon-author" : "Alex Hall <mehgcap@gmail.com>, Joseph Lee <joseph.lee22590@gmail.com>, beqa gozalishvili <beqaprogger@gmail.com> and other NVDA contributors",
	# URL for the add-on documentation support
	"addon-url" : "http://addons.nvda-project.org/"
}

import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "resourceMonitor", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
