import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1
import QtQuick.Window 2.2

Window{
    id: root
    title: "settings"
    modality: Qt.ApplicationModal
    flags: Qt.Dialog
    minimumHeight: 700
    minimumWidth: 700
    maximumHeight: 700
    maximumWidth: 700
    visible:  true

    GridLayout {
        id: gridLayout
        anchors.fill: parent
        columns: 4
        columnSpacing:10
        rowSpacing: 10
        anchors.margins: 10
        Layout.maximumWidth: 700
        Layout.fillWidth: true
        Layout.preferredHeight: 300
        Layout.preferredWidth: 700



        Button {
            id: button
            Layout.minimumWidth: 150
            Layout.minimumHeight: 100
            text: qsTr("DHCP \n Starvation")
            palette.buttonText: "white"
            font.pointSize: 8

            background: Rectangle {
                color: '#495163'
                border.width: 0
                border.color: "#55aaff"
                radius: 20
            }
        }


        Button {
            id: button1
            Layout.minimumWidth: 150
            Layout.minimumHeight: 100
            text: qsTr("VTP")
            palette.buttonText: "white"
            font.pointSize: 8

            background: Rectangle {
                color: '#495163'
                border.width: 0
                border.color: "#55aaff"
                radius: 20
            }
        }

        Button {
            id: button2
            Layout.minimumWidth: 150
            Layout.minimumHeight: 100
            text: qsTr("Rouge \n DHCP")
            palette.buttonText: "white"
            font.pointSize: 8

            background: Rectangle {
                color: '#495163'
                border.width: 0
                border.color: "#55aaff"
                radius: 20
            }
        }

        Button {
            id: button3
            Layout.minimumWidth: 150
            Layout.minimumHeight: 100
            text: qsTr("DHCP Starvation \n Detector")
            palette.buttonText: "white"
            font.pointSize: 8

            background: Rectangle {
                border.width: 0
                color: '#495163'
                border.color: "#55aaff"
                radius: 20
            }
        }


        Button {
            id: button4
            Layout.minimumWidth: 150
            Layout.minimumHeight: 100
            text: qsTr("ARP \n Spoofer")
            palette.buttonText: "white"
            font.pointSize: 8

            background: Rectangle {
                border.width: 0
                color: '#495163'
                border.color: "#55aaff"
                radius: 20
            }
        }

        Button {
            id: button5
            Layout.minimumWidth: 150
            Layout.minimumHeight: 100
            palette.buttonText: "white"
            text: qsTr("ARP Spoofer \n Detector")
            font.pointSize: 8

            background: Rectangle {
                color: '#495163'
                border.width: 0
                border.color: "#55aaff"
                radius: 20
            }
        }

        Button {
            id: button6
            Layout.minimumWidth: 150
            Layout.minimumHeight: 100
            text: qsTr("DNS \n Poisoning")
            palette.buttonText: "white"
            font.pointSize: 8

            background: Rectangle {
                border.width: 0
                color: '#495163'
                border.color: "#55aaff"
                radius: 20
            }
        }

        Button {
            id: button7
            Layout.minimumWidth: 150
            Layout.minimumHeight: 100
            text: qsTr("CDP")
            palette.buttonText: "white"
            font.pointSize: 8

            background: Rectangle {
                border.width: 0
                color: '#495163'
                border.color: "#55aaff"
                radius: 20
            }
        }

    }
}
