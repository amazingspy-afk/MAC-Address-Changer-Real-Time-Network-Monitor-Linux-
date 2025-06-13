import re
import random


def is_valid_mac(mac):
    """
    Checks if the provided MAC address is valid.
    Valid format: XX:XX:XX:XX:XX:XX where X is a hex digit.
    """
    mac_regex = r'^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$'
    return re.match(mac_regex, mac) is not None

# Test the function
if __name__ == "__main__":
    test_macs = [
        "00:11:22:33:44:55",  # valid
        "AA:BB:CC:DD:EE:FF",  # valid
        "00-11-22-33-44-55",  # invalid
        "0011.2233.4455",     # invalid
        "G1:23:45:67:89:AB"   # invalid (G is not hex)
    ]

    for mac in test_macs:
        result = "Valid" if is_valid_mac(mac) else "Invalid"
        print(f"{mac}: {result}")


def generate_random_mac():
    """
    Generates a random, locally administered MAC address.
    Format: 02:xx:xx:xx:xx:xx
    """
    mac = [0x02,
           random.randint(0x00, 0x7F),
           random.randint(0x00, 0xFF),
           random.randint(0x00, 0xFF),
           random.randint(0x00, 0xFF),
           random.randint(0x00, 0xFF)]
    return ':'.join(f'{octet:02x}' for octet in mac)

