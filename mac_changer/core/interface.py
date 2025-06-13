import netifaces

def list_interfaces():
    """
    Returns a list of active physical network interfaces,
    excluding loopback and virtual ones.
    """
    interfaces = netifaces.interfaces()
    valid_interfaces = []

    for iface in interfaces:
        # Skip loopback and docker interfaces
        if iface.startswith('lo') or iface.startswith('docker'):
            continue
        # Check if interface has a MAC address
        try:
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_LINK in addrs:
                mac_info = addrs[netifaces.AF_LINK][0]
                mac = mac_info.get('addr', None)
                if mac:
                    valid_interfaces.append((iface, mac))
        except ValueError:
            continue

    return valid_interfaces

# Test code
if __name__ == "__main__":
    interfaces = list_interfaces()
    print("Available network interfaces:")
    for iface, mac in interfaces:
        print(f"{iface} -> MAC: {mac}")
