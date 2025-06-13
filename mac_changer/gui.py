import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from core.interface import list_interfaces
from core.changer import change_mac
from utils.validator import is_valid_mac, generate_random_mac

# Keep a dictionary to store original MACs
original_macs = {}

class MACChangerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MAC Address Changer")

        # Interface Dropdown
        tk.Label(root, text="Select Interface:").pack()
        self.interfaces = dict(list_interfaces())
        self.iface_var = tk.StringVar()
        self.iface_dropdown = ttk.Combobox(root, textvariable=self.iface_var)
        self.iface_dropdown['values'] = list(self.interfaces.keys())
        self.iface_dropdown.pack()

        # Display current MAC
        self.current_mac_label = tk.Label(root, text="Current MAC: -")
        self.current_mac_label.pack()

        # Entry for custom MAC
        tk.Label(root, text="Enter Custom MAC:").pack()
        self.custom_mac_entry = tk.Entry(root)
        self.custom_mac_entry.pack()

        # Buttons
        tk.Button(root, text="Apply Custom MAC", command=self.apply_custom_mac).pack(pady=5)
        tk.Button(root, text="Generate Random MAC", command=self.apply_random_mac).pack(pady=5)
        tk.Button(root, text="Restore Original MAC", command=self.restore_mac).pack(pady=5)

        # Bind interface change to update MAC label
        self.iface_dropdown.bind("<<ComboboxSelected>>", self.update_mac_display)

    def update_mac_display(self, event=None):
        iface = self.iface_var.get()
        current_mac = self.interfaces.get(iface, "N/A")
        self.current_mac_label.config(text=f"Current MAC: {current_mac}")

    def apply_custom_mac(self):
        iface = self.iface_var.get()
        new_mac = self.custom_mac_entry.get().strip()

        if not is_valid_mac(new_mac):
            messagebox.showerror("Invalid", "MAC address format is invalid.")
            return

        original_macs[iface] = self.interfaces.get(iface)
        change_mac(iface, new_mac)
        messagebox.showinfo("Success", f"MAC changed to {new_mac}")
        self.refresh_interfaces()

    def apply_random_mac(self):
        iface = self.iface_var.get()
        rand_mac = generate_random_mac()

        original_macs[iface] = self.interfaces.get(iface)
        change_mac(iface, rand_mac)
        messagebox.showinfo("Random MAC", f"MAC changed to {rand_mac}")
        self.refresh_interfaces()

    def restore_mac(self):
        iface = self.iface_var.get()
        original = original_macs.get(iface)

        if not original:
            messagebox.showerror("Not Available", "Original MAC not saved.")
            return

        change_mac(iface, original)
        messagebox.showinfo("Restored", f"MAC restored to {original}")
        self.refresh_interfaces()

    def refresh_interfaces(self):
        self.interfaces = dict(list_interfaces())
        self.update_mac_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = MACChangerGUI(root)
    root.mainloop()
