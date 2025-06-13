import subprocess
import sys
sys.path.append("..")  # So we can import from utils
from utils.validator import is_valid_mac


import subprocess

def change_mac(interface, new_mac):
    try:
        subprocess.check_call(['pkexec', 'ip', 'link', 'set', interface, 'down'])
        subprocess.check_call(['pkexec', 'ip', 'link', 'set', interface, 'address', new_mac])
        subprocess.check_call(['pkexec', 'ip', 'link', 'set', interface, 'up'])
        print(f"[+] Changed MAC of {interface} to {new_mac}")
    except subprocess.CalledProcessError:
        print("[-] Failed to change MAC address. Ensure you have correct permissions.")


# Test code
from utils.validator import is_valid_mac, generate_random_mac

if __name__ == "__main__":
    iface = input("Enter the interface (e.g., eth0, wlan0): ")
    mode = input("Type 'r' for random MAC or 'c' for custom: ").strip().lower()

    if mode == 'r':
        mac = generate_random_mac()
        print(f"[+] Generated Random MAC: {mac}")
    else:
        mac = input("Enter custom MAC address (e.g., 00:11:22:33:44:55): ")
        if not is_valid_mac(mac):
            print("[-] Invalid MAC address format. Exiting.")
            exit()

    change_mac(iface, mac)


