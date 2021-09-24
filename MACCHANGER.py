#!/usr/bin/env python

"""Subprocess can execute any system commands. (Does not to be Linux Command only)
If you use it in Windows it will allow to execute Windows Commands, likewise if it
in MAC OS it will allow to run MAC Commands"""
# Libraries Used to Read the Interfaces of Linux
import socket
import array
import string
import struct
import fcntl

import subprocess
import re
import optparse
from random import choice, randint



class MAC_CH:

    #Function to CHange the MAC ADDRESS
    def Lets_Change_MAC(self,Interface, MACADDR):
        # subprocess.call(f"ifconfig {Interface} down", shell=True) #Turning down the interface
        subprocess.call(["ifconfig", Interface, "down"])  # Turning down the interface along with command filtering

        # subprocess.call(f"ifconfig {Interface} hw ether {MACADDR}", shell=True) #Executing MAC changing command
        subprocess.call(
            ["ifconfig", Interface, "hw", "ether", MACADDR])  # Executing MAC changing command along with command filtering

        # subprocess.call(f"ifconfig {Interface} up", shell=True) #Turning interface up
        subprocess.call(["ifconfig", Interface, "up"])  # Turning interface up along with command filtering


    # var_Interface = input("Please Enter The Interface Name: ")
    # var_MACADDR = input("Please Enter The MAC Address: ")
    # Lets_Change_MAC(var_Interface,var_MACADDR)



    # This Function will bring back the interface with its default MAC Address
    def Default_MAC(self,Interface_def):
        # subprocess.call("ifdown eth0", shell=True)
        subprocess.call(["ifdown", Interface_def])  # DIsabling Interface

        subprocess.call("ifconfig eth0 hw ether $(ethtool -P " + Interface_def + " | awk '{print $3}')",
                        shell=True)  # Restoring the Default MAC ADDRESS
        Permanent_MAC_Bytes = subprocess.check_output(["ethtool", "-P", Interface_def]) # Permanent MAC Address
        Permanent_MAC = Permanent_MAC_Bytes.decode("UTF-8")
        Permanent_MAC_Search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Permanent_MAC)

        # subprocess.call("ifup eth0", shell=True)
        subprocess.call(["ifup", Interface_def])  # Enabling Interface

        #Calling Function
        MAC_Now = MAC_CH.MAC_Address_Display(Interface_def)
        print(f"Current address: {MAC_Now}")
        if Permanent_MAC_Search.group(0) == MAC_Now: #The output of re search always comes in match groups, so we have to select inside the group
            print("MAC Address Successfully Restored to default")
    # Default_MAC("eth0")


    #Function To Read MAC Address
    def MAC_Address_Display(self,Interface):

        #Returns the Permanent MAC ADDRESS of the device
        Org_MAC_Bytes = subprocess.check_output(["ethtool", "-P", Interface]) # Original MAC Address
        Org_MAC = Org_MAC_Bytes.decode("UTF-8") #Decoding the bytes to string format
        print(Org_MAC, end="")

        #Checking Whether MAC Address has changed or not
        MAC_Result_Bytes = subprocess.check_output(["ifconfig", Interface]) #check output always gives output in bytes format
        Final_Result = MAC_Result_Bytes.decode("UTF-8") #Converting Bytes to String
        # print((Final_Result))

        #Searching for the MAC Address section in the output of ifconfig using self written code
        # MAC_word = "ether"
        # if MAC_word in Final_Result:
        #     split = Final_Result.index(MAC_word)
        #     Changed_MAC = Final_Result[split:]
        #     print(f"Changed Address: {Changed_MAC[6:23]}")


        #Searching for the MAC Address section in the output of ifconfig using regular expression library
        MAC_ADDR_Search= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Final_Result)
        if not MAC_ADDR_Search:
            print("This Interface Does Not have any MAC Address")
        else:
            print(MAC_ADDR_Search.group(0)) #The output of re search always comes in match groups, so we have to select inside the group

    # MAC_Now = MAC_Address_Display("eth0")
    # print(f"Current address: {MAC_Now}")
    # if var_MACADDR == MAC_Now:
    #     print(f"MAC Successfully Changed to {var_MACADDR}")
    # else:
    #     print("Sorry, MAC Address did not change")




    def Random_MAC_Generator(self):
        #Some Of the Organizationally Unique Identifier (OUI)
        Cisco = ["00","1E","49"]
        Dell = ["18","66","DA"]
        HP = ["00","00","63"]
        Apple = ["4C","32","75"]
        Samsung = ["00", "00","F0"]
        Acer = ["C0", "98", "79"]
        Lenovo = ["20", "76", "93"]
        IBM = ["34", "40", "B5"]
        Random_MAC = choice([Cisco, Dell, HP, Apple, Samsung, Acer, Lenovo, IBM])
        Random_Letters = "ABCDEF" #MAC Address only consists of Alphabets from A to F

        for i in range(3):
            """Inside the list first of all one random Number and one random Alphabet is generated, 
            then it chooses either a number or an alphabet randomly"""
            First = choice([str(randint(0, 9)), choice(Random_Letters)])

            #This is the alternative, long and clear view of aboce single line code
            # N1 = choice(str(randint(0,9))) #Choosing one random number
            # L1 = choice(Random_Letters) #Choosing one random letter
            # Pair1 = str(N1+L1) #Combining both number and letter in string format, eg: 1 and A = "1A"
            # Final1 = choice(Pair1) #Again Choosing either a number or a letter from above string.

            Second = choice([str(randint(0, 9)), choice(Random_Letters)])
            # This is the alternative, long and clear view of aboce single line code
            # N2 = choice(str(randint(0,9)))
            # L2 = choice(Random_Letters)
            # Pair2 = str(N2 + L2)
            # Final2 = choice(Pair2)

            Final_Pair = str(First + Second)  #Two random number or letters generated by First and Second are stored in FinalPair
            Random_MAC.append(Final_Pair) #The two number in each loops are appended in the randomly selected list in string format.
        rand = ":".join(Random_MAC) #Joining the strings elements of the Random_MAC using Join function with ':'
        return rand



    # THIS IS FOR GUI VERSION TO DETECT INTERFACE
    # Function That will return the name of all the interfaes present in the device
    # def get_local_interfaces(self):
    #     """ Returns a dictionary of name:ip key value pairs. """
    #     MAX_BYTES = 4096
    #     FILL_CHAR = b'\0'
    #     SIOCGIFCONF = 0x8912
    #     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     names = array.array('B', MAX_BYTES * FILL_CHAR)
    #     names_address, names_length = names.buffer_info()
    #     mutable_byte_buffer = struct.pack('iL', MAX_BYTES, names_address)
    #     mutated_byte_buffer = fcntl.ioctl(sock.fileno(), SIOCGIFCONF, mutable_byte_buffer)
    #     max_bytes_out, names_address_out = struct.unpack('iL', mutated_byte_buffer)
    #     namestr = names.tobytes()
    #     namestr[:max_bytes_out]
    #     bytes_out = namestr[:max_bytes_out]
    #     ip_dict = {}
    #     for i in range(0, max_bytes_out, 40):
    #         name = namestr[ i: i+16 ].split(FILL_CHAR, 1)[0]
    #         name = name.decode('utf-8')
    #         ip_bytes   = namestr[i+20:i+24]
    #         full_addr = []
    #         for netaddr in ip_bytes:
    #             if isinstance(netaddr, int):
    #                 full_addr.append(str(netaddr))
    #             elif isinstance(netaddr, str):
    #                 full_addr.append(str(ord(netaddr)))
    #         ip_dict[name] = '.'.join(full_addr)
    #
    #     return ip_dict
    #
    # if __name__ == "__main__":
    #     Main_int = []
    #     for iface, ip in get_local_interfaces().items():
    #         # Returns the Name of interfaces with its IP Address
    #         #interface = ("{ip:15s} {iface}".format(ip=ip, iface=iface))
    #         Available_interface = ("{iface}".format(iface=iface))
    #         Main_int.append(Available_interface)
    #     print(Main_int)
    # get_local_interfaces()

# objj = MAC_CH()
# objj.Random_MAC_Generator()

