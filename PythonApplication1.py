import pywifi
from pywifi import const
import math
import tkinter as tk

# Set the SSID (Wi-Fi network name) and password of your home network
home_network_ssid = "alepoumhnklepseis"
home_network_password = "SegmentationFault69"

# Constants for signal propagation model
reference_distance = 1.0  # Reference distance in meters
reference_rssi = -50  # RSSI value at the reference distance
path_loss_exponent = 2.0  # Path loss exponent for signal attenuation

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()  # Create a PyWiFi object
    iface = wifi.interfaces()[0]  # Get the first available Wi-Fi interface

    iface.disconnect()  # Disconnect from any currently connected network

    profile = pywifi.Profile()  # Create a profile object
    profile.ssid = ssid  # Set the SSID
    profile.auth = const.AUTH_ALG_OPEN  # Set the authentication algorithm
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # Set the key management type for WPA2-PSK
    profile.cipher = const.CIPHER_TYPE_CCMP  # Set the cipher type
    profile.key = password  # Set the password

    iface.remove_all_network_profiles()  # Remove all existing network profiles
    temp_profile = iface.add_network_profile(profile)  # Add the new network profile

    iface.connect(temp_profile)  # Connect to the network

    # Wait for the connection to be established
    while iface.status() != const.IFACE_CONNECTED:
        pass

    print("Connected to the Wi-Fi network.")

def calculate_distance(rssi):
    # Calculate the distance using the logarithmic path loss model
    distance = 10 ** ((reference_rssi - rssi) / (10 * path_loss_exponent))
    return distance

def detect_people():
    wifi = pywifi.PyWiFi()  # Create a PyWiFi object
    iface = wifi.interfaces()[0]  # Get the first available Wi-Fi interface

    iface.scan()  # Scan for available networks
    scan_result = iface.scan_results()

    devices_count = 0

    for result in scan_result:
        if result.ssid == home_network_ssid:
            mac_address = result.bssid
            rssi = result.signal
            distance = calculate_distance(rssi)
            devices_count += 1
            print(f"Wi-Fi device {devices_count} with MAC address {mac_address} detected at a distance of {distance:.2f} meters from the router.")

    if devices_count == 0:
        print("No Wi-Fi devices detected on the network.")

def on_button_click():
    # Call the detect_people function when the button is clicked
    detect_people()

# Create the GUI window
window = tk.Tk()

# Create a button widget
button = tk.Button(
    window,
    text="Detect Devices",
    command=on_button_click,
    bg="#4287f5",  # Background color of the button
    fg="white",  # Text color of the button
    relief="raised",  # Border style of the button
    font=("Arial", 14),  # Font style and size of the button text
    padx=10,  # Padding in the X direction
    pady=5,  # Padding in the Y direction
)
button.pack()

# Start the GUI event loop
window.mainloop()
