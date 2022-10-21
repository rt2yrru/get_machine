import platform
import sys


_system,_machine,_platform,_uname,_version,_mac_version=(platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
platform.mac_ver(),)

print(_system)
print(_machine)
print(_platform)
print(_uname)
print(_version)
print(_mac_version)
