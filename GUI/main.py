import os
import datetime
import sys
sys.path.insert(1, '/home/pratik/PycharmProjects/Final_Assignment/Common-Assignment-Repo-Pratikshr')
import IPInterfaces
from DHCPStrv import DHCPStarve
from RD_Detector import DetectRD
from FloodingDetection import StarveDetect
from arpspoof_enhanced import lets_spoof


from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal, QTimer







class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.setTime())
        self.timer.start(1000)


    # Signals
    setName = Signal(str)
    printText = Signal(str)
    printTime = Signal(str)
    isVisible = Signal(bool)

    def result(self):
        return "\n\nActual Result of Tool!!! Here"

    #Set Time Function
    def setTime(self):
        now = datetime.datetime.now()
        formatDate = now.strftime("%H:%M %p \n %Y/%m/%d")
        self.printTime.emit(formatDate)


    #Function
    @Slot(str)
    def welcomeText(self, data):
        self.setName.emit('Welcome, ' + data)

    @Slot(str)
    def dhcp(self, data):
        self.setName.emit(data + self.result())


    @Slot(bool)
    def showHideRectangle(self, isChecked):
        """
        This Fuction give the Mode of Attack from GUI
        :param isChecked: Persistant or Normal Mode
        :return:
        """

        if isChecked == True:
            print("This is Persistant Mode")

        elif isChecked == None:
            print("This is also Normal Mode")

        elif isChecked == False:
            print("This is Normal Mode")

        else:
            print("Please Choose The Mode")

    @Slot(str)
    def getting(self, iface):
        """
        This function fetches interface selected in the GUI
        :param iface: Interface fetched from GUI's Combobox
        :return:
        """
        self.iface = iface


    # DHCP Strvation Attack Initiator
    @Slot(str)
    def startattack(self, iface_mode):
        int_mod = iface_mode.split(":")
        mode = int_mod[0]
        iface = int_mod[1]
        # print(mode)
        # print(iface)
        try:
            DHCPStarve().starve(iface, mode)
        except KeyboardInterrupt:
            sys.exit()

    # DHCP Starvation Detector
    @Slot(str)
    def StarveDetector(self, iface):
        self.setName.emit(iface)
        StarveDetect().Main()

    # Rouge DHCP
    @Slot(str)
    def RougeDHCP(self, data):
        data = data.split(":")
        rougeip = data[0]
        iface = data[1]
        Rgateway = data[2]
        Rnetwork = data[3]
        Rsubnet = data[4]
        Rdomain = data[5]
        Rdns = data[6]
        print(rougeip,iface,Rgateway,Rnetwork,Rsubnet,Rdomain, Rdns)
        # RougeDHCP().run(rougeip, iface, Rgateway, Rnetwork, Rsubnet, Rdomain, Rdns)

        # IPv4Pattern = re.compile(
        #     r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$')

        # if not IPv4Pattern.match(rougeip):
        #     print("Invalid Rouge IP")
        # if not IPv4Pattern.match(Rgateway):
        #     print("Invalid Rouge Gateway")
        # if not IPv4Pattern.match(Rnetwork):
        #     print("Invalid Rouge Network")
        # if not IPv4Pattern.match(Rsubnet):
        #     print("Invalid Rouge Subnet")
        # if not IPv4Pattern.match(Rdns):
        #     print("Invalid Rouge DNS ServerIP")
        #
        # if IPv4Pattern.match(rougeip) and IPv4Pattern.match(Rgateway) and IPv4Pattern.match(Rnetwork) and IPv4Pattern.match(Rsubnet) and IPv4Pattern.match(Rdns):
        #     print("All fields are Valid")


    # Rouge DHCP Detector
    @Slot(str)
    def RDDetector(self, iface):
        # print(iface)
        DetectRD().DetectRD(iface)

    # ARP Spoofer
    @Slot(str)
    def Arpspoofer(self, net):
        import re
        ip_net = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?')
        if ip_net.match(net):
            print(net)
            print("Valid")
            lets_spoof().Main(net)
        else:
            print("Invalid")







def GUI():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    comportComboModel = IPInterfaces.main()
    # Get Context
    main = MainWindow()
    engine.rootContext().setContextProperty("backend", main)
    engine.rootContext().setContextProperty("comModel", comportComboModel)

    # Set App Extra Info
    app.setOrganizationName("SAATHI")
    app.setOrganizationDomain("SOFTWARICA COLLEGE")

    # Load QML File
    engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
