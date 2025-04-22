from scapy.all import *

ip_layer = IP(dst="247ctf.com")
icmp_layer = ICMP()
packet = ip_layer / icmp_layer
r = send(packet)

# print(packet.show())
# wireshark(packet)

# ans, uans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.0.0/24"), timeout=3, verbose=False)
# for i in ans:
#     print(i)
#     print(i[1].psrc)


SYN = 0x02
RST = 0x04
ACK = 0x10

# for port in [22,80,139,443,445,8080]:
#     tcp_connect = sr1(IP(dst="247ctf.com")/TCP(sport=RandShort(), dport=port, flags="S"), timeout=1, verbose=False)
#     if tcp_connect and tcp_connect.haslayer(TCP):
#         response_flags = tcp_connect.getlayer(TCP).flags
#         if response_flags == (SYN + ACK):
#             snd_rst = send(IP(dst="247ctf.com")/TCP(sport=RandShort(), dport=port, flags="AR"), verbose=False)
#             print(f"{port} is open!")
#         elif response_flags == (RST + ACK):
#             print(f"{port} is closed!")
#     else:
#         print(f"{port} is closed!")

from scapy.layers.http import HTTPRequest

def process(packet):
    if packet.haslayer(HTTPRequest):
        print(packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode())

# sniff(filter="port 80", prn=process, store=False)

