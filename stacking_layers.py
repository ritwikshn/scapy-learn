#!/usr/bin/python3
from inspect import stack
from scapy.all import IP, TCP, Ether, raw
from utils.packet_print import print_packet

#a standalone TCP protocol packet
tcp = TCP()
print("standalone TCP packet - ")
print_packet(tcp, verbose = True)
print()

#a standalone IP protocol packet
ip = IP()
print("standalone IP packet - ")
print_packet(ip, verbose=True)
print()

#a standalone Ether packet
ether = Ether()
print("standalone Ethernet packet - ")
print_packet(ether, verbose=True)
print()

#stacked packet
#notice the change in properties (like checksum, protocol) from the
#corresponding values in standalone packets
stacked = ether / ip / tcp
print("stacked packet - ")
print_packet(stacked, verbose=True)