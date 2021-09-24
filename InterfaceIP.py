from scapy.all import *
import socket
import fcntl
import array
import struct


def Made_Function():
    def get_local_interfaces():
        """ Returns a dictionary of name:ip key value pairs. """

        MAX_BYTES = 4096
        FILL_CHAR = b'\0'
        SIOCGIFCONF = 0x8912
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        names = array.array('B', MAX_BYTES * FILL_CHAR)
        names_address, names_length = names.buffer_info()
        mutable_byte_buffer = struct.pack('iL', MAX_BYTES, names_address)
        mutated_byte_buffer = fcntl.ioctl(sock.fileno(), SIOCGIFCONF, mutable_byte_buffer)
        max_bytes_out, names_address_out = struct.unpack('iL', mutated_byte_buffer)
        namestr = names.tobytes()
        ip_dict = {}
        for i in range(0, max_bytes_out, 40):
            name = namestr[ i: i+16 ].split(FILL_CHAR, 1)[0]
            name = name.decode('utf-8')
            ip_bytes   = namestr[i+20:i+24]
            full_addr = []
            for netaddr in ip_bytes:
                if isinstance(netaddr, int):
                    full_addr.append(str(netaddr))
                elif isinstance(netaddr, str):
                    full_addr.append(str(ord(netaddr)))
            ip_dict[name] = '.'.join(full_addr)
        return ip_dict

    Main_int = []
    IP_int = []

    def Convert_dict(lst):
        for iface, ip in get_local_interfaces().items():
            # Returns the Name of interfaces with its IP Address
            interface = ("{ip:15s} {iface}".format(ip=ip, iface=iface))
            Main_int.append(interface)

        for i in range(len(Main_int)):
            spaces = Main_int[i].split(' ')  # This Splits all spaces present in the list
            # ----------------------------------
            for i in spaces:
                if i != "":
                    IP_int.append(i)
                elif i == "":
                    pass

        init = iter(IP_int)
        res_dct = dict(zip(init, init))
        # print(res_dct)                  #Self Made Dictionary All the way from unmanaged list

        if conf.iface not in res_dct.values():
            print("This Interface Does Not Exist or Does Not Have Any IP Address")
        else:
            # print(f"The {conf.iface} interface have IP:  {(list(res_dct.keys())[list(res_dct.values()).index(conf.iface)])}")
            return list(res_dct.keys())[list(res_dct.values()).index(conf.iface)]   #Stores the IP Address of Respective Interface
        get_local_interfaces()
    return Convert_dict(IP_int)


def Email_Generate():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "tiku.shr@gmail.com"
    password = "kugbqnueukuxvagq"
    toaddr = "pratik.shrr@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "!!! ALERT MESSAGE !!!"

    # string to store the body of the mail
    body = "Rouge DHCP DETECTED"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    server.send_message(msg)

    server.quit()


# BANNER
def Banner(Keyword, Color):
    from termcolor import colored
    from pyfiglet import Figlet
    f = Figlet(font="slant")
    print(colored(f.renderText(Keyword),Color))

