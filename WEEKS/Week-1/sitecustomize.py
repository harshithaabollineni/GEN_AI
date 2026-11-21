import platform
import subprocess

_original_mac_ver = platform.mac_ver

def fixed_mac_ver():
    version, version_info, machine = _original_mac_ver()

    if not version:
        version = subprocess.check_output(
            ["/usr/bin/sw_vers", "-productVersion"],
            text=True
        ).strip()

        machine = platform.machine()

    return version, version_info, machine

platform.mac_ver = fixed_mac_ver
