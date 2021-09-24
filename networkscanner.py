import scapy.all as scapy #scapy.all ko satta scapy to make it easy

"""def scan(ip):
    scapy.arping(ip) #arping scapy ko euta function"""
def Network(indx):
    import subprocess #cmd bata jasari run garna milcha
    import re
    indx = int(indx)
    cmd = subprocess.check_output(["ip", "route"])
    str_cmd = cmd.decode("UTF-8")
    list_otp = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?",str_cmd)  # Matching IP with CIDR using Regular Expression
    return (list_otp[indx])


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request #packet banako
    answered_list = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0] #srp allows to send packets with custom ether. Verbose mathi ko dekhaundaina.

    clients_list = []
    for element in answered_list:
        clients_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        clients_list.append(clients_dict)
        """print(element[1].psrc + "\t\t" + element[1].hwsrc)"""
    return(clients_list)



def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


if __name__ == '__main__':
    scan_result = scan(Network(1))
    print_result(scan_result)