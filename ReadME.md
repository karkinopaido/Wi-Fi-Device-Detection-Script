# Wi-Fi Device Detection Script

This Python script detects devices connected to a Wi-Fi network and provides information about their distance from the router. It utilizes the `pywifi` library to scan for Wi-Fi networks, retrieve the signal strength (RSSI), and calculate the approximate distance based on a signal propagation model.

## Features

- Connect to a specified Wi-Fi network using SSID and password.
- Scan for available Wi-Fi networks and detect devices connected to a specific network.
- Calculate the approximate distance of detected devices from the router using the received signal strength (RSSI).
- Differentiate between Wi-Fi devices and devices connected via Ethernet.
- Display the device information, including the MAC address, connection type, and distance from the router.

## Prerequisites

- Python 3.x
- `pywifi` library: Install using `pip install pywifi`.
- `tkinter` library: Included with Python by default.
- `netifaces` library: Install using `pip install netifaces`.

## Usage

1. Set the SSID (Wi-Fi network name) and password of your home network in the script.
2. Run the script using Python: `python wifi_device_detection.py`.
3. Click the "Detect Devices" button to initiate the detection process.
4. The script will scan for Wi-Fi networks and display the devices connected to the specified network along with their distance from the router.

Please ensure that you have the necessary permissions and meet any legal or ethical obligations before using this script to detect devices on a network. This script should be used responsibly and in compliance with applicable laws and regulations regarding network security and privacy.

## Limitations

- The distance calculation is based on a path loss model and provides an estimate rather than an exact measurement.
- The accuracy of distance calculations can be affected by factors such as obstacles, signal interference, and environmental conditions.
- The script assumes that it is running on the same network and has permission to access the connected devices' information.

## License

This script is provided under the [MIT License](LICENSE).
