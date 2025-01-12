from . import psutil


def get_physical_memory():
	memory = psutil.virtual_memory()
	return memory.used, memory.total


def get_virtual_memory():
	memory = psutil._psutil_windows.virtual_mem()
	return memory[2]-memory[3], memory[2]
