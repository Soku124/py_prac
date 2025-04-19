from scapy.all import *

ip_layer = IP(dst="247ctf.com")
icmp_layer = ICMP()
packet = ip_layer / icmp_layer
r = send(packet)

print(packet.show())