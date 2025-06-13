import sys
import argparse
from core.interface import list_interfaces
from core.changer import change_mac
from utils.validator import is_valid_mac, generate_random_mac

# Store original MACs for restore option
original_macs = {}

def list_all_interfaces():
    print("\nAvailable Network Interfaces:")
    for iface, mac in list_interfaces():
        print(f"  {iface} -> {mac}")

def change_to_custom(interface, new_mac):
    if not is_valid_mac(new_mac):
        print("[-] Invalid MAC address format.")
        return
    original_macs[interface] = dict(list_interfaces()).get(interface)
    change_mac(interface, new_mac)

def change_to_random(interface):
    new_mac = generate_random_mac()
    original_macs[interface] = dict(list_interfaces()).get(interface)
    print(f"[+] Generated random MAC: {new_mac}")
    change_mac(interface, new_mac)

def restore_mac(interface):
    if interface not in original_macs:
        print("[-] Original MAC not saved. Run random/custom change first.")
        return
    original = original_macs[interface]
    print(f"[~] Restoring original MAC: {original}")
    change_mac(interface, original)

def main():
    parser = argparse.ArgumentParser(description="Advanced MAC Address Changer CLI")
    parser.add_argument("-l", "--list", action="store_true", help="List all network interfaces")
    parser.add_argument("-i", "--interface", type=str, help="Interface to target (e.g., eth0)")
    parser.add_argument("-m", "--mac", type=str, help="Set a custom MAC address")
    parser.add_argument("-r", "--random", action="store_true", help="Generate and assign random MAC")
    parser.add_argument("--restore", action="store_true", help="Restore original MAC address")

    args = parser.parse_args()

    if args.list:
        list_all_interfaces()
    elif args.interface:
        if args.mac:
            change_to_custom(args.interface, args.mac)
        elif args.random:
            change_to_random(args.interface)
        elif args.restore:
            restore_mac(args.interface)
        else:
            print("[-] No action provided. Use --mac or --random or --restore.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
