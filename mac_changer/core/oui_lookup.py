import os
import re

OUI_FILE = os.path.join(os.path.dirname(__file__), '../data/oui.txt')

def load_oui_map():
    """
    Parses the IEEE OUI text file and returns a dictionary
    mapping MAC prefixes (first 6 hex chars) to vendor names.
    """
    oui_map = {}
    pattern = re.compile(r"^(?P<mac>[0-9A-Fa-f]{6})\s+\(base 16\)\s+(?P<vendor>.+)$")

    with open(OUI_FILE, 'r') as f:
        for line in f:
            match = pattern.match(line.strip())
            if match:
                mac_prefix = ':'.join([match.group("mac")[i:i+2] for i in range(0, 6, 2)]).lower()
                oui_map[mac_prefix] = match.group("vendor")

    return oui_map

def get_vendor_by_mac(mac, oui_map):
    """
    Returns vendor name based on MAC prefix, or 'Unknown'.
    """
    mac_prefix = ':'.join(mac.lower().split(':')[0:3])
    return oui_map.get(mac_prefix, 'Unknown')

# Test
if __name__ == "__main__":
    oui_map = load_oui_map()
    print(get_vendor_by_mac("00:1A:2B:44:55:66", oui_map))  # Example output: Cisco
