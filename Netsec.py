import argparse
import sys
from GUI import main

#Object of Graphical Int Class
parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest="MainTool", metavar="ALL AVAILABLE TOOLS")

#-------------------GRAPHICAL USER INTERFACE----------------------------
gui_parser = subparser.add_parser("GUI", help="Open Graphical User Interface")
gui_parser1 = subparser.add_parser("gui", help="Open Graphical User Interface")



# ----------------------------DHCP TOOL -------------------------------
dhcp_parser = subparser.add_parser("DHCP", help="DHCP TOOLS")
# dhcp_parser.add_argument("-S", action="store_true")

dhcp_subparsers = dhcp_parser.add_subparsers(dest="InsideTool")
dhcp_subparsers.metavar = 'DHCP Tool Options'

# -------Starvation-------------
dhcp_strv_parser = dhcp_subparsers.add_parser('strv', help="DHCP Starvation")
dhcp_strv_parser.add_argument("-p", "--pers", action="store_true", help="Persistant Mode")
dhcp_strv_parser.set_defaults()

# -------Rouge DHCP Creation-------------
dhcp_rouge_parser = dhcp_subparsers.add_parser('rdhcp', help="Create Rouge DHCP")
dhcp_rouge_parser.add_argument('-r', '--rougedhcp', metavar="ROUGESERVERIP", default="ip", type=str,
                               help='IP Address of Rouge Server')

dhcp_rouge_parser.add_argument('-i', '--iface', metavar="IFACE", default="ip", type=str,
                               help='Interface you wish to use')

dhcp_rouge_parser.add_argument('-rg', '--rougegateway', metavar="ROUGEGATEWAY", default="ip", type=str,
                               help='Gateway For Rouge IP Addresses')

dhcp_rouge_parser.add_argument('-rn', '--rougenetwork', metavar="ROUGENETWORK", default="192.168.1.0", type=str,
                               help='Network you wish to use in DHCP Pool')

dhcp_rouge_parser.add_argument('-s', '--subnet', metavar="SUBNET", default="255.255.255.0", type=str,
                               help='Subnet mask of the pool')

dhcp_rouge_parser.add_argument('-d', '--domain', metavar="DOMAINNAME", default="Officedomain", type=str,
                               help='Domain Name')

dhcp_rouge_parser.add_argument('-dn', '--dns', metavar="DNSSERVER", default="a", type=str,
                               help='Domain Name Server IP Address')
dhcp_rouge_parser.set_defaults()

# -------DHCP Starvation Detection-------------
dhcp_strvd_parser = dhcp_subparsers.add_parser('strvd', help="Detect DHCP Starvation Attack")
dhcp_strvd_parser.add_argument('-i', '--iface', metavar="IFACE", default="ip", type=str,
                               help='Interface you wish to use')
dhcp_strvd_parser.set_defaults()

# -------Rouge DHCP Server Detection-------------
dhcp_rdd_parser = dhcp_subparsers.add_parser('rd', help="Detect Rouge DHCP Servers in the Network")
dhcp_rdd_parser.add_argument('-i', '--iface', metavar="IFACE", default="ip", type=str,
                               help='Interface you wish to use')
dhcp_rdd_parser.set_defaults()



# ---------------------------- ARP Spoofer -------------------------------
arp_parser = subparser.add_parser("ARP", help="ARP Spoof (Man in the Middle)")
arp_parser.add_argument('-n', '--network', metavar="Network", default="10.0.0.0/24", type=str,
                               help='Network where you want to initiate ARP Spoof')
# arp_parser1= subparser.add_parser("arp", help="ARP Spoof (Man in the Middle)")



# ---------------------------- STP -------------------------------
stp_parser = subparser.add_parser("STP", help="Spanning Tree Protocol")
stp_subparsers = stp_parser.add_subparsers(dest="Insidestp")
stp_subparsers.metavar = 'STP Tool Options'

# -------BPDU Configuration-------------
stpbpdu_parser = stp_subparsers.add_parser('bpdu', help="BPDU Configuration Flood")
stpbpdu_parser.add_argument('-i', '--iface', metavar="Interafce", default="interface", type=str,
                               help='Interface to Launch Attack')
stpbpdu_parser.set_defaults()

# -------TCN FLOOD-------------
stptcn_parser = stp_subparsers.add_parser('tcn', help="Topology Change Notification Flood")
stptcn_parser.add_argument('-i', '--iface', metavar="Interafce", default="interface", type=str,
                               help='Interface to Launch Attack')
stptcn_parser.set_defaults()

# -------ROOT ROLE-------------
stproot_parser = stp_subparsers.add_parser('root', help="STP Root Role Attack")
stproot_parser.add_argument('-i', '--iface', metavar="Interafce", default="interface", type=str,
                               help='Interface to Launch Attack')
stproot_parser.set_defaults()



# ---------------------------- CDP -------------------------------
cdp_parser = subparser.add_parser("CDP", help="CDP Attack")
cdp_parser.add_argument('-i', '--iface', metavar="Interface", default="eth0", type=str,
                               help='Interface')



# ---------------------------- VTP -------------------------------
cdp_parser = subparser.add_parser("VTP", help="VTP Attack")
cdp_parser.add_argument('-i', '--iface', metavar="Interface", default="eth0", type=str,
                               help='Interface')


# ---------------------------- DNS -------------------------------
cdp_parser = subparser.add_parser("DNS", help="DNS Poisoining")
cdp_parser.add_argument('-dn', '--dns', metavar="DNS", default="142.250.67.238", type=str,
                               help='IP of Redirection')


# ---------------------------- Network Scanner -------------------------------
cdp_parser = subparser.add_parser("nets", help="Network Scanner")
cdp_parser.add_argument('-n', '--net', metavar="Network", default="10.0.0.0/24", type=str,
                               help='Network To Scan')


# ---------------------------- MAC Changer -------------------------------
mac_parser = subparser.add_parser("MAC", help="MAC Changer")
mac_subparsers = mac_parser.add_subparsers(dest="Insidemac")
mac_subparsers.metavar = 'MAC Changer'

# -------MAC Change-------------
macch_parser = mac_subparsers.add_parser('Ch', help="Change MAC Address")
macch_parser.add_argument('-i', '--iface', metavar="Interafce", default="eth10", type=str,
                               help='Interface to Launch Attack')
macch_parser.set_defaults()

# -------MAC Restore-------------
macre_parser = mac_subparsers.add_parser('Re', help="Restore MAC to Default")
macre_parser.add_argument('-i', '--iface', metavar="Interafce", default="eth10", type=str,
                               help='Interface to Launch Attack')
macre_parser.set_defaults()


args = parser.parse_args()
# print(args.MainTool)
# print(args.InsideTool)





# ____----------------------------------CONDITION--------------------------------------_____________

# ---------------------------------GRAPHICAL USER INTERFACE---------------------------------
if args.MainTool == None:
    parser.error('Please Choose the Option')

elif args.MainTool == "GUI" or args.MainTool == "gui":
    main.GUI()

#  ----------------------------------DHCP MAIN TOOL--------------------------
elif args.MainTool == "DHCP" or args.MainTool == "dhcp":
    print("Inside DHCP Tool")

    # -------DHCP Starvation--------------
    if args.InsideTool == "strv":
        print("Inside DHCP in Starvation")
        if args.pers:
            print("This is Persistant Mode")
        else:
            print("This is Normal Mode")

    # ----------Rouge DHCP Creator-------------
    elif args.InsideTool == "rdhcp":
        print("Inside DHCP in Rouge DHCP Attack")
        print(args.rougedhcp, args.iface, args.rougegateway, args.rougenetwork, args.subnet, args.domain, args.dns,args.dns)

    # -----------DHCP Starvation Detector-------
    elif args.InsideTool == "strvd":
        print("Inside DHCP in Starvation Detector")
        print(args.iface)

    # -------------Rouge DHCP Detector---------
    elif args.InsideTool == "rd":
        print("Inside DHCP in Rouge DHCP Detector")
        print(args.iface)

# -----------ARP-----------------
elif args.MainTool == "ARP":
    print("ARP")
    print(args.network)

# -----------STP MainTool-----------------
elif args.MainTool == "STP":
    print("Inside STP Tool")

    # -----------STP BPDU-----------------
    if args.Insidestp == "bpdu":
        print("This is BPDU Configuration Attack")
        print(args.iface)

    # -----------STP TCN-----------------
    elif args.Insidestp == "tcn":
        print("This is TCN Attack")
        print(args.iface)

    # -----------STP Root Role-----------------
    elif args.Insidestp == "root":
        print("This is Root Role Attack")
        print(args.iface)

# -----------CDP-----------------
elif args.MainTool == "CDP":
    print("CDP")
    print(args.iface)

# -----------VTP-----------------
elif args.MainTool == "VTP":
    print("VTP")
    print(args.iface)

# -----------DNS-----------------
elif args.MainTool == "DNS":
    print("DNS")
    print(args.dns)

# -----------Network Scanner-----------------
elif args.MainTool == "nets":
    print("Network Scanner")
    print(args.net)

# -----------MAC Changer MainTool-----------------
elif args.MainTool == "MAC":
    print("Inside MAC Changer Tool")

    # -----------MAC Change-----------------
    if args.Insidemac == "Ch":
        print(f"Changing MAC Address of {args.iface}")
        print(args.iface)

    # ------------MAC Restore---------------
    elif args.Insidemac == "Re":
        print(f"Restoring MAC Address of {args.iface}")
        print(args.iface)




"""----------------------------USUAGE-------------------------
Program.py maintool subtool parameters
eg: python argHandle.py GUI --> This command will redired to GUI mode
eg: python argHandle.py DHCP strv -p
    python argHandle.py DHCP rdhcp -i 10.0.0.1 -i eth0 -rg 10.0.0.1 -rn 192.168.0.0 -s 255.255.255.0 -d office.com -dn 10.0.0.1
"""