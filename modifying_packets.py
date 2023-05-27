#!/usr/bin/python3
from scapy.all import IP

packet = IP(ttl = 10)

print("packet object - ")
print(packet)
print("source address is auto chosen as loopback - ")
print(packet.src)

#modify packet properties
packet.dst = "192.168.29.1"


print("Modified the destination address to 192.168.29.1")

print("packet object - ")
print(packet)
print("source address is auto chosen as IPv4 address from LAN - ")
print(packet.src)