import scapy.all as scapy
import arpspoof_enhanced


def packet_sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_ip = (packet[scapy.ARP].psrc)

            real_mac = arpspoof_enhanced.mac(real_ip)
            receiving_mac = packet[scapy.ARP].hwsrc

            if real_mac != receiving_mac:
                print("Your ARP is being Spoofed")
        except IndexError:
            pass
    print(packet.show())

packet_sniff("eth1")
