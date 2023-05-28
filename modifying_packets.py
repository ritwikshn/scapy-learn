#!/usr/bin/python3
from scapy.all import IP, raw
from utils.packet_print import print_packet


packet = IP(ttl = 10)

#notice how source address in auto chosen as loopback
print("packet object - ")
print_packet(packet, verbose = True)

#modify packet properties
packet.dst = "192.168.29.1"


print("Modified the destination address to 192.168.29.1")

#notice the source address now is chosen as IPv4 adress of the host from LAN
print("packet object - ")
print_packet(packet, verbose = True)