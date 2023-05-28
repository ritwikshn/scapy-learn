#!/usr/bin/python3
from scapy.all import IP, TCP, Ether, raw

#a standalone TCP protocol packet
tcp = TCP()
print("standalone TCP packet - ")
print(repr(TCP(raw(tcp))))
print()

#a standalone IP protocol packet
ip = IP()
print("standalone IP packet - ")
print(repr(IP(raw(ip))))
print()

#a standalone Ether packet
ether = Ether()
print("standalone Ethernet packet - ")
print(repr(Ether(raw(ether))))
print()

#stacked packet
#notice the change in properties (like checksum, protocol) from the
#corresponding values in standalone packets
stacked = ether / ip / tcp
print("stacked packet - ")
print(repr(Ether(raw(stacked))))
