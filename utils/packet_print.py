from scapy.all import *


def print_packet(packet, verbose = False):
    if verbose:
        protocol = packet.__class__
        print(repr(protocol(raw(packet))))
    else:
        print(repr(packet))

