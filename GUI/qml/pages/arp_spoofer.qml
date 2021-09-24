import QtQuick 2.15
import QtQuick.Controls 2.15
import "../controls"
import "../pages"
import QtQuick.Layouts 1.15

Item {
    Rectangle {
        id: rectangle
        visible: true
        color: "#2c313c"
        anchors.fill: parent

        Rectangle {
            id: rectangleTop
            height: 69
            color: "#495163"
            radius: 10
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.rightMargin: 80
            anchors.leftMargin: 80
            anchors.topMargin: 40

            AppButton {
                id: btnBack
                text: "< Back"
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.leftMargin: 10
                anchors.bottomMargin: 10
                anchors.topMargin: 10
                font.pointSize: 9
                width: 150
                onClicked: {
                    btnHome.isActiveMenu = true
                    btnSettings.isActiveMenu = false
                    btnAllTools.isActiveMenu = false
                    stackView.push(Qt.resolvedUrl("homePage.qml"))
                }
            }
            Label {
                id: labelHeading
                color: "#55aaff"
                text: qsTr(" ARP Spoofer")
                anchors.left: btnBack.right
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.bottomMargin: 10
                anchors.topMargin: 10
                font.bold: false
                anchors.leftMargin: 30
                anchors.rightMargin: 70
                font.pointSize: 14
            }
        }

        Rectangle {
            id: rectangleVisible
            visible: true
            color: "#1d2128"
            radius: 10
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: rectangleTop.bottom
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 27
            anchors.rightMargin: 80
            anchors.leftMargin: 80
            anchors.topMargin: 20

            Rectangle {
                id: rectangleLabel
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
                anchors.topMargin: 20

                GridLayout {
                    id: gridSearch
                    x: -40
                    y: -40
                    anchors.fill: parent
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                    rows: 1
                    columns: 2
                    columnSpacing: 10
                    CustomTextField {
                        id: scanField
                        placeholderText: "Enter the Network to Scan with /CIDR. eg: 192.168.1.0/24"
                        Layout.fillWidth: true
                        implicitHeight: 40
                    }

                    CustomButton {
                        id: btnSpoof
                        text: "Scan & Start"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 40
                        Layout.preferredWidth: 250
                        onClicked: {
                        backend.Arpspoofer(scanField.text)
                    }
                    }
                }
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/

