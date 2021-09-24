import logging
from itertools import chain
import sys
import six
from termcolor import colored
import InterfaceIP
import MACCHANGER

# This will Supress all the messages that have lower level of seriousness than Error messages
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
try:
    from scapy.all import *
    from scapy.layers import l2, inet, dhcp, dns
    from scapy.layers.l2 import ARP
    from scapy import sendrecv
except ImportError:
    print("Scapy Package is not Installed in your System")
    sys.exit()



class DetectRD:

    # By default the value of conf.checkIPaddre is True
    conf.checkIPaddr = False

    # Getting HARDWARE ADDRESS
    def MAC_Address_Display(self,Interface):
        # Returns the Permanent MAC ADDRESS of the device
        # Original MAC Address
        Org_MAC_Bytes = subprocess.check_output(["ethtool", "-P", Interface])
        # Decoding the bytes to string format
        Org_MAC = Org_MAC_Bytes.decode("UTF-8")
        Hw_Addr = Org_MAC.split(' ')[2]
        return Hw_Addr


    def Separator(self,len, color):
        # This is a Custom Line Separator to split the results
        for i in range(len):
            six.print_(colored("-", color), end="")

    def DetectRD(self,i_face):
        # BANNER
        InterfaceIP.Banner('ROUGE   DHCP DETECTOR', "green")
        def unp_info(desiredinfo):
            # Grep Values From The Packets with Option 2
            all_reply = reply[1][dhcp.DHCP].options                                 # return the dhcp response list of tuples
            result = list(filter(lambda x: x.count(desiredinfo) > 0, all_reply))
            return (list(chain.from_iterable(result)))                              # in default return the value in list of tuple, this line will unpack the tuple and convert it to list


        # Crafting DHCP Discover Packet
        Generated_MAC = MACCHANGER.MAC_CH().Random_MAC_Generator()
        packet = (
                    l2.Ether(dst="ff:ff:ff:ff:ff:ff", src=Generated_MAC) /
                    inet.IP(src="0.0.0.0", dst="255.255.255.255") /
                    inet.UDP(sport=68, dport=67) /
                    dhcp.BOOTP(chaddr = Generated_MAC, xid=random.randint(1, 1000000000), flags=0xFFFFFF) /
                    dhcp.DHCP(options=[("message-type", "discover"), "end"])
        )


        #Sending packets and Receiving Multiple Offers

        ans, unans = srp(packet, multi = True, iface = i_face, timeout = 10, verbose = 0)  # Receives either the result or the unanswered

        # print(ans)
        # print(unans)
        #Storing MAC-IP Pairs in Dictionary

        mac_ip = {}


        for reply in ans:
            # Searching inside offer of DHCP by using Keywords

            serverid = unp_info("server_id")
            router = unp_info("router")
            nameserver = unp_info("name_server")
            subnet_mask = unp_info("subnet_mask")

            # Storing Values in Dictionary Format --> One key Multiple Values
            mac_ip[reply[1][l2.Ether].src] = [serverid[1], subnet_mask[1], nameserver[1], router[1]]


        #Results
        six.print_(colored("\n[!] Active DHCP Servers Currently In The LAN", "blue"))
        leng = len("[!] Active DHCP Servers Currently In The LAN [!]")


        # dict = {"c2:01:04:3c:00:00":['255.255.255.0', '10.0.0.254', '10.0.0.254', '10.0.0.254'], "52:54:00:12:35:02": ['255.255.255.0', '192.168.1.1', '10.0.0.1', '10.0.0.1']}

        count = 0
        for macip in mac_ip:
            count+=1

            #Checking Rouge and Real Server
            if macip == "c2:01:04:3a:00:00" and mac_ip[macip][0] == "10.0.0.254":
                six.print_(colored(f"\nDHCP SERVER {count}", "green"))
                lenn = len(f"DHCP SERVER {count}")
                self.Separator(lenn, "white")

                six.print_(colored(f"\n[-] SERVER MAC : {macip}\n[-] SERVER IP : {mac_ip[macip][0]}\n[-] SUBNET MASK : {mac_ip[macip][1]}\n[-] NAMESERVER : {mac_ip[macip][2]}\n[-] GATEWAY : {mac_ip[macip][3]}", "green"))
                six.print_(colored("\n[✓] Detected [✓] This is a Legitimate DHCP Server [✓]", "green"))
                # six.print_(colored(f"\n[-] SERVER MAC : {macip}\n[-] SERVER IP : {dict[macip]}", "green"))
                leng1 = len("[✓] Detected [✓] This is a Legitimate DHCP Server [✓]")
                self.Separator(leng1,"white")
                print("\n")

            else:
                #EMAIL GENERATOR TO ALERT ADMIN IF ROUGE SERVER IS DETECTED
                # InterfaceIP.Email_Generate()

                six.print_(colored(f"\nDHCP SERVER {count}", "red"))
                lenn = len(f"DHCP SERVER {count}")
                self.Separator(lenn, "white")

                six.print_(colored(f"\n[-] SERVER MAC : {macip}\n[-] SERVER IP : {mac_ip[macip][0]}\n[-] SUBNET MASK : {mac_ip[macip][1]}\n[-] NAMESERVER : {mac_ip[macip][2]}\n[-] GATEWAY : {mac_ip[macip][3]}", "red"))
                six.print_(colored("\n[✘] ALERT [✘] [✘] [✘] This is a Rouge DHCP Server [✘] [✘] [✘]", "red"))
                leng2 = len("[✘] ALERT [✘] [✘] [✘] This is a Rouge DHCP Server [✘] [✘] [✘]")
                self.Separator(leng2, "white")
                print("\n")



if __name__ == "__main__":
    import argparse


    parser = argparse.ArgumentParser(description='Rouge DHCP Detection')
    parser.add_argument('-i', '--iface', metavar="IFACE", default=conf.iface, type=str,
                        help='Interface you wish to use')

    args = parser.parse_args()
    DetectRD().DetectRD(i_face=args.iface)