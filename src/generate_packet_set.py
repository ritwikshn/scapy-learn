#!/usr/bin/python3
from scapy.all import IP, TCP, PacketList
from utils.packet_print import print_packet

#generate set of packets with destinations from a subnet
a = IP(dst = "www.target.com/30")
print([packet for packet in a])
print()

#generate set of packets with ttl from a given set
b = IP(ttl = [1, 2, (5, 9)])
print([packet for packet in b])
print()

#generate set of packets with destination port from a given set
c = TCP(dport = [80, 443])
print([packet for packet in c])
print()

#stacking set of packets will result in another set
#resulting set will have stacked packets from cartesian product
stacked = a/c
print([p for p in stacked])
print()

#make a PacketList out of the set of packet 
pl = PacketList(a)
print(pl)
print() 
pls = PacketList(a/c)
print(pls)
print() 