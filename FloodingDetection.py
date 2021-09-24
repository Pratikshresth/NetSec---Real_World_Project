import sys

import six

import InterfaceIP
from time import sleep
from scapy.all import *
from termcolor import colored
from scapy.layers import l2, dhcp, inet
import datetime





count = 0
counta = 0
dict = {}

class StarveDetect:

    def Custom_Inspection(self,Packet):
        print("hello")
        global count, dict, counta
        arrivaltime = (str(datetime.datetime.now()).split(" ")[1])
        incomingpktsrc = Packet.src

        #Detecting Using DHCP Discovery Comparing The MAC Addresses and THe Arrival Time of Each Packet
        #if Discovery Message is detected
        if Packet[dhcp.DHCP].options[0][1] == 1:  # Discovery Message Type = 1, Offer  = 2
            count+=1
            for storedtime, storedmac in dict.items():
                if storedmac == incomingpktsrc and count > 5:  # If MAC Stored in DICT Matches The MAC of present Incoming Discovery Packet and Count Greated Than 5
                    result = self.AlertCheck(storedtime, arrivaltime, incomingpktsrc)
                    if result == 0:
                        sleep(10)
                        dict.clear()
                        break
            dict.clear()
            dict[arrivaltime] = incomingpktsrc
            # print(dict)


        #Detecting Using DHCP Offer, Sending the Offered IP an ARP request in the interval of 4seconds to ensure that the complete DHCP Process is Done
        elif Packet[dhcp.DHCP].options[0][1] == 2:
            Offered_IP = Packet[dhcp.BOOTP].yiaddr
            # print(Offered_IP)

            arppacket = (
                    l2.Ether(dst='ff:ff:ff:ff:ff:ff') /
                    l2.ARP(op=1, pdst="10.0.0.254")
            )
            reply = srp1(arppacket, iface="eth1", verbose=0, timeout=4)

            if reply == None:
                packet = (
                        l2.Ether(dst="0000:1111:2222:1111", type=0x0101) /
                        inet.IP(src="0.0.0.0", dst="255.255.255.255") /
                        Raw(load="Warning: Anamoly DHCP Detected")
                )
                six.print_(colored("\n!!! ALERT !!! Possible Flood Attack Detected", "red"))
                six.print_(colored("\nSending Alert to Server", "red"))
                sendp(packet, verbose=0)
                sys.exit()



    def AlertCheck(self, timestored, arrivaltime, incomingpktsrc):
        StoredHour = timestored.split(":")[0]
        StoredMin = timestored.split(":")[1]
        arrivalHour = arrivaltime.split(":")[0]
        arrivalMin = arrivaltime.split(":")[1]
        MinuteDiff = int(arrivalMin) - int(StoredMin)

        if (timestored == arrivaltime or StoredHour == arrivalHour and MinuteDiff in range(10)):  # Comparing Hours Minutes of Packets and Determining Interval between previous and present Packet
            six.print_(colored(f"\nAnamoly DHCP Discover Detected in the Interval of {MinuteDiff} Minutes", "red"))
            self.send_frame(timestored, arrivaltime, incomingpktsrc)
            return 0
        else:
            return 1




    def send_frame(self, timestored, arrivaltime, incomingpktsrc):
        packet = (
                l2.Ether(dst="0000:1111:2222:1111", type=0x0101) /
                inet.IP(src="0.0.0.0", dst="255.255.255.255") /
                Raw(load="Warning: Anamoly DHCP Deteced by " + incomingpktsrc + " at" + timestored + "and then again at " + arrivaltime)
        )


        six.print_(colored("\n!!! ALERT !!! Possible Flood Attack Detected","red"))
        six.print_(colored("\nSending Alert to Server", "red"))
        sendp(packet, verbose=0)


    def Main(self):
        # BANNER
        InterfaceIP.Banner("FLOOD   DETECT", "green")
        sniff(filter="udp and (port 67 or port 68)", prn=self.Custom_Inspection, store=0)


