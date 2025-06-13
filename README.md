# MAC-Address-Changer-Real-Time-Network-Monitor-Linux-
A Python-based tool that enables users to spoof MAC addresses and monitor network interfaces in real-time. It features both a command-line interface and a Tkinter-based graphical interface, allowing secure MAC changes via pkexec without needing to run the GUI as root. The tool supports random and custom MAC address .
# 🔐 MAC Address Changer & Network Monitor (Linux)

A Python-based MAC address spoofing tool with a user-friendly Tkinter GUI and real-time network interface monitoring — designed for privacy, network testing, and education.

## ✨ Features

- Change MAC addresses for any interface
- Generate random or custom MAC addresses
- Restore original MAC
- Real-time interface monitor: IP, MAC, status, traffic
- CLI & GUI (sudo-free GUI via `pkexec`)

## 📸 GUI Preview



## 🛠️ Technologies Used

- Python 3, Tkinter, psutil, subprocess, pkexec
- Linux (Kali), iproute2
- Modular folder structure (core/, utils/)

## ⚙️ Setup Instructions

```bash
git clone https://github.com/amazingsppy-afk/mac-address-changer.git
cd mac-address-changer
pip install -r requirements.txt
python3 gui.py
