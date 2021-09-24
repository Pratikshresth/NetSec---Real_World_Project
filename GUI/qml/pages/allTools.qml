import QtQuick 2.0
import QtQuick.Controls 2.15
import "../controls"
import QtQuick.Layouts 1.15

Item {
    Rectangle {
        id: rectangle
        color: "#2c313c"
        width: 900
        height: 580
        anchors.fill: parent

        Rectangle {
            id: rectangleTop
            x: 50
            y: 30
            height: 51
            color: "#495163"
            radius: 10
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.leftMargin: 50
            anchors.rightMargin: 50
            anchors.topMargin: 30

            GridLayout {
                id: gridSearch
                x: -40
                y: -40
                anchors.fill: parent
                anchors.rightMargin: 10
                anchors.leftMargin: 10
                rows: 1
                columns: 2
                CustomTextField {
                    id: searchField
                    placeholderText: "Search"
                    Layout.fillWidth: true
                }

                CustomButton {
                    id: btnSearch
                    text: "Search"
                    Layout.maximumWidth: 200
                    Layout.fillWidth: true
                    Layout.preferredHeight: 40
                    Layout.preferredWidth: 250
                }
            }
        }

        Rectangle {
            id: category_container
            x: 20
            y: 101
            width: 520
            color: "#1d2128"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: rectangleTop.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: 50
            anchors.leftMargin: 50
            anchors.bottomMargin: 20
            anchors.topMargin: 20

            ScrollView {
                id: scrollView
                x: -40
                y: -40
                width: 520
                anchors.fill: parent
                anchors.rightMargin: 10
                anchors.leftMargin: 10
                anchors.bottomMargin: 20
                anchors.topMargin: 20
                clip: true
                ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
                ScrollBar.vertical.policy: ScrollBar.AlwaysOff

                GridLayout {
                    id: gridAttack
                    anchors.fill: parent
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                    anchors.bottomMargin: 10
                    anchors.topMargin: 10
                    columns: 4
                    columnSpacing: 30
                    rowSpacing: 20
                    Layout.maximumWidth: 70
                    Layout.fillWidth: true
                    Layout.preferredHeight: 300
                    Layout.preferredWidth: 700

                    AppButton {
                        id: btnDHCP
                        text: "DHCP \nStarvation"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 175
                        onClicked: {
                            btnHome.isActiveMenu = false
                            btnSettings.isActiveMenu = false
                            btnAllTools.isActiveMenu = false
                            stackView.push(Qt.resolvedUrl(
                                               "dhcp_starvation.qml"))
                        }
                    }

                    AppButton {
                        id: btnRouge_DHCP
                        text: "Rouge \nDHCP"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 175
                        onClicked: {
                            btnHome.isActiveMenu = false
                            btnSettings.isActiveMenu = false
                            btnAllTools.isActiveMenu = false
                            stackView.push(Qt.resolvedUrl("rougeDHCP.qml"))
                        }
                    }

                    AppButton {
                        id: btnARP_Spoofer
                        text: "Arp \nSpoofer"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 175
                    }

                    AppButton {
                        id: btnASpoofer_Detector
                        text: "Arp Spoofer \nDetector"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 175
                        onClicked: {
                            btnHome.isActiveMenu = false
                            btnSettings.isActiveMenu = false
                            btnAllTools.isActiveMenu = false
                            stackView.push(Qt.resolvedUrl(
                                               "rougeDHCP_Detector.qml"))
                        }
                    }
                    AppButton {
                        id: btnDHCPS_Detector
                        text: "DHCP Starvation \nDetector"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 175
                        onClicked: {
                            btnHome.isActiveMenu = false
                            btnSettings.isActiveMenu = false
                            btnAllTools.isActiveMenu = false
                            stackView.push(Qt.resolvedUrl(
                                               "dhcp_stavation_detector.qml"))
                        }
                    }
                    AppButton {
                        id: btnRDHCP_Detector
                        text: "Rouge DHCP \nDetector"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 175
                    }

                    AppButton {
                        id: btnDNS_Poison
                        text: "DNS\nPoisoning"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 175
                    }

                    AppButton {
                        id: btnDNSP_Detector
                        text: "DNS Poisoning\nDetector"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 175
                    }
                    AppButton {
                        id: btnVTP
                        text: "VTP"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 175
                    }
                    AppButton {
                        id: btnDCDP
                        text: "CDP"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 175
                    }
                    AppButton {
                        id: btnRouge_DHC4
                        text: "Rouge \n DHCP"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150
                    }
                    AppButton {
                        id: btnRouge_DHC5
                        text: "Rouge \n DHCP"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150
                    }
                    AppButton {
                        id: btnRouge_DHC6
                        text: "Rouge \n DHCP"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150
                    }
                }
            }
        }
    }
    Connections {
        target: backend
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/

