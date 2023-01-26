# ARP Spoofer

This script is used to perform network spoofing by issuing spoofed ARP requests. It allows you to target a device on the network and change its ARP cache, making it believe that your device has a different IP address.

## How to run

To run the ARP spoofer script, open a terminal and navigate to the directory where the script is located. Then, run the following command:

python arp_spoof.py <target_ip> <spoof_ip>

Replace `<target_ip>` with the IP address of the target device, and `<spoof_ip>` with the IP address that you want to use as the source in the spoofed ARP packets.

For example, if you want to target the device with IP address 192.168.1.5 and use the IP address 192.168.1.1 as the source in the spoofed ARP packets, you would run the following command:

`python arpspoof.py 192.168.1.5 192.168.1.1`


Please note that this script is for educational purposes only, and that using it for malicious purposes is illegal.

## Prerequisites

- Scapy library
- Administrative permission

To install the Scapy library, use the following command:

`pip install scapy`

Make sure to run your script with administrative permission.
