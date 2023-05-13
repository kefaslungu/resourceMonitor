from comtypes import GUID
from ctypes import *
from ctypes.wintypes import DWORD, PDWORD, HANDLE, BOOL

wlanapi = windll.wlanapi

WLAN_NOTIFICATION_SOURCE_ALL = 0x0000ffff
WLAN_NOTIFICATION_SOURCE_ACM = 0x00000008
wlan_notification_acm_connection_complete = 0x0000000a
wlan_notification_acm_disconnected = 0x00000015
wlan_notification_acm_interface_arrival = 0x0000000d
wlan_notification_acm_interface_removal = 0x0000000e

WLAN_AVAILABLE_NETWORK_CONNECTED = 1

# State of the interface
wlan_interface_state_connected = 1

# Return codes
ERROR_SUCCESS = 0

# Client versions
CLIENT_VERSION_WINDOWS_XP_SP3 = 1
CLIENT_VERSION_WINDOWS_VISTA_OR_LATER = 2

# Values of wireless LAN authentication algorithm
DOT11_AUTH_ALGO_80211_OPEN = 1
DOT11_AUTH_ALGO_80211_SHARED_KEY = 2
DOT11_AUTH_ALGO_WPA = 3
DOT11_AUTH_ALGO_WPA_PSK = 4
DOT11_AUTH_ALGO_WPA_NONE = 5
DOT11_AUTH_ALGO_RSNA = 6
DOT11_AUTH_ALGO_RSNA_PSK = 7
DOT11_AUTH_ALGO_IHV_START = 0x80000000
DOT11_AUTH_ALGO_IHV_END = 0xffffffff

class DOT11_SSID(Structure):
	_fields_ = [
		("SSIDLength", c_ulong),
		("SSID", c_char * 32),
	]

class WLAN_CONNECTION_NOTIFICATION_DATA(Structure):
	_fields_ = [
		("wlanConnectionMode", c_uint),
		("strProfileName", c_wchar * 256),
		("dot11Ssid", DOT11_SSID),
		("dot11BssType", c_uint),
		("bSecurityEnabled", BOOL),
		("wlanReasonCode", DWORD),
		("dwFlags", DWORD),
		("strProfileXml", c_wchar * 1),
	]

class WLAN_NOTIFICATION_DATA(Structure):
	_fields_ = [
		("NotificationSource", DWORD),
		("NotificationCode", DWORD),
		("InterfaceGuid", GUID),
		("dwDataSize", DWORD),
		("pData", c_void_p),
	]

class WLAN_AVAILABLE_NETWORK(Structure):
	_fields_ = [
		("ProfileName", c_wchar * 256),
		("dot11Ssid", DOT11_SSID),
		("dot11BssType", c_uint),
		("NumberOfBssids", c_ulong),
		("NetworkConnectable", BOOL),
		("wlanNotConnectableReason", DWORD),
		("NumberOfPhyTypes", c_ulong),
		("dot11PhyTypes", c_uint * 8),
		("MorePhyTypes", BOOL),
		("wlanSignalQuality", c_ulong),
		("SecurityEnabled", BOOL),
		("dot11DefaultAuthAlgorithm", c_uint),
		("dot11DefaultCipherAlgorithm", c_uint),
		("Flags", DWORD),
		("Reserved", DWORD),
	]

class WLAN_AVAILABLE_NETWORK_LIST(Structure):
	_fields_ = [
		("NumberOfItems", DWORD),
		("Index", DWORD),
		("Network", WLAN_AVAILABLE_NETWORK * 1),
	]

class WLAN_INTERFACE_INFO(Structure):
	_fields_ = [
		("InterfaceGuid", GUID),
		("strInterfaceDescription", c_wchar * 256),
		("isState", c_uint),
	]

class WLAN_INTERFACE_INFO_LIST(Structure):
	_fields_ = [
		("NumberOfItems", DWORD),
		("Index", DWORD),
		("InterfaceInfo", WLAN_INTERFACE_INFO * 1),
	]

WLAN_NOTIFICATION_CALLBACK = CFUNCTYPE(None, POINTER(WLAN_NOTIFICATION_DATA), POINTER(c_void_p))

def errcheck(result, func, args):
	if result != ERROR_SUCCESS:
		raise WinError(c_long(result).value)
	return result

def WlanOpenHandle(dwClientVersion, pReserved, pdwNegotiatedVersion, phClientHandle):
	""" The WlanOpenHandle function opens a connection to the server. """
	wlanapi.WlanOpenHandle.errcheck = errcheck
	wlanapi.WlanOpenHandle.argtypes = [DWORD, c_void_p, POINTER(DWORD), POINTER(HANDLE)]
	wlanapi.WlanOpenHandle.restype = DWORD
	return wlanapi.WlanOpenHandle(dwClientVersion, pReserved, pdwNegotiatedVersion, phClientHandle)

def WlanEnumInterfaces(hClientHandle, pReserved, ppInterfaceList):
	""" The WlanEnumInterfaces function enumerates all of the wireless LAN interfaces currently enabled on the local computer. """
	wlanapi.WlanEnumInterfaces.errcheck = errcheck
	wlanapi.WlanEnumInterfaces.argtypes = [HANDLE, c_void_p, POINTER(POINTER(WLAN_INTERFACE_INFO_LIST))]
	wlanapi.WlanEnumInterfaces.restype = DWORD
	return wlanapi.WlanEnumInterfaces(hClientHandle, pReserved, ppInterfaceList)

def WlanGetAvailableNetworkList(hClientHandle, pInterfaceGuid, dwFlags, pReserved, ppAvailableNetworkList):
	""" The WlanGetAvailableNetworkList function retrieves the list of available networks on a wireless LAN interface. """
	wlanapi.WlanGetAvailableNetworkList.errcheck = errcheck
	wlanapi.WlanGetAvailableNetworkList.argtypes = [HANDLE, POINTER(GUID), DWORD, c_void_p, POINTER(POINTER(WLAN_AVAILABLE_NETWORK_LIST))]
	wlanapi.WlanGetAvailableNetworkList.restype = DWORD
	return wlanapi.WlanGetAvailableNetworkList(hClientHandle, pInterfaceGuid, dwFlags, pReserved, ppAvailableNetworkList)

def WlanFreeMemory(pMemory):
	""" The WlanFreeMemory function frees memory. Any memory returned from Native Wifi functions must be freed. """
	wlanapi.WlanFreeMemory.argtypes = [c_void_p]
	wlanapi.WlanFreeMemory(pMemory)

def WlanCloseHandle(hClientHandle, pReserved):
	""" The WlanCloseHandle function closes a connection to the server. """
	wlanapi.WlanCloseHandle.errcheck = errcheck
	wlanapi.WlanCloseHandle.argtypes = [HANDLE, c_void_p]
	wlanapi.WlanCloseHandle.restype = DWORD
	return wlanapi.WlanCloseHandle(hClientHandle, pReserved)

def WlanRegisterNotification(hClientHandle, dwNotifSource, bIgnoreDuplicate, funcCallback, pCallbackContext, pReserved, pdwPrevNotifSource):
	""" The WlanRegisterNotification function is used to register and unregister notifications on all wireless interfaces. """
	wlanapi.WlanRegisterNotification.errcheck = errcheck
	wlanapi.WlanRegisterNotification.argtypes = [HANDLE, DWORD, BOOL, WLAN_NOTIFICATION_CALLBACK, c_void_p, c_void_p, PDWORD]
	wlanapi.WlanRegisterNotification.restype = DWORD
	return wlanapi.WlanRegisterNotification(hClientHandle, dwNotifSource, bIgnoreDuplicate, funcCallback, pCallbackContext, pReserved, pdwPrevNotifSource)
