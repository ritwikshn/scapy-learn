#!/usr/bin/python3

# creating multiple IP packets; each destined to a different IP in a subnet

from scapy.all import IP
from utils.packet_print import print_packet

#the subnet ( in string )
target = "www.target.com/30"

#initialize
ip = IP(dst = target)

print("The IP object - ")
print_packet(ip, verbose = True)

print("The set of IPs in IP object - ")
print([p for p in ip])





