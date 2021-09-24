import QtQuick 2.0
import QtQuick.Controls 2.15
import "../controls"
import QtQuick.Layouts 1.15

Item {
    visible: true
    Rectangle {
        id: rectangle
        width: 900
        height: 580
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
            anchors.rightMargin: 50
            anchors.leftMargin: 50
            anchors.topMargin: 40

            GridLayout {
                id: gridApp
                anchors.fill: parent
                anchors.rightMargin: 10
                anchors.leftMargin: 10
                rows: 1
                columns: 3

                CustomTextField {
                    id: textField
                    placeholderText: "Type your name"
                    Layout.fillWidth: true
                    Keys.onEnterPressed: {
                        backend.welcomeText(textField.text)
                        switchHome.checked = true
                        backend.showHideRectangle(switchHome.checked)
                    }
                    Keys.onReturnPressed: {
                        backend.welcomeText(textField.text)
                        switchHome.checked = true
                        backend.showHideRectangle(switchHome.checked)
                    }
                }

                CustomButton {
                    id: btnChangeName
                    text: "Login"
                    Layout.maximumWidth: 200
                    Layout.fillWidth: true
                    Layout.preferredHeight: 40
                    Layout.preferredWidth: 250
                    onClicked: {
                        backend.welcomeText(textField.text)
                        switchHome.checked = true
                        backend.showHideRectangle(switchHome.checked)
                    }
                }

                Switch {
                    id: switchHome
                    text: qsTr("Switch")
                    checked: false
                    Layout.preferredHeight: 40
                    Layout.preferredWidth: 68
                    // Change Show/Hide Frame
                    onToggled: {
                        backend.showHideRectangle(switchHome.checked)
                    }
                }
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
            anchors.rightMargin: 50
            anchors.leftMargin: 50
            anchors.topMargin: 10

            Label {
                id: labelTextName
                y: 15
                width: 200
                height: 25
                color: "#55aaff"
                text: qsTr("Welcome")
                anchors.left: parent.left
                anchors.right: parent.right
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.bold: false
                anchors.leftMargin: 12
                anchors.rightMargin: 8
                font.pointSize: 14
            }

            Label {
                id: labelDate
                height: 25
                color: "#5c667d"
                text: qsTr("Date")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                horizontalAlignment: Text.AlignRight
                verticalAlignment: Text.AlignVCenter
                anchors.topMargin: 15
                anchors.rightMargin: 12
                anchors.leftMargin: 10
                font.pointSize: 10
            }

            Rectangle {
                id: appContainer
                color: "#1d2128"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: labelRecent.bottom
                anchors.bottom: parent.bottom
                clip: true
                anchors.rightMargin: 25
                anchors.bottomMargin: 20
                anchors.leftMargin: 25
                anchors.topMargin: 5

                GridLayout {
                    id: gridLayout
                    anchors.fill: parent
                    columns: 4
                    columnSpacing: 10
                    rowSpacing: 5
                    anchors.margins: 10
                    clip: true
                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0
                    Layout.maximumWidth: 700
                    Layout.fillWidth: true
                    Layout.preferredHeight: 300
                    Layout.preferredWidth: 700

                    AppButton {
                        id: btnDHCP
                        text: "DHCP \nStarvation"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150
                        onClicked: {
                            btnHome.isActiveMenu = false
                            btnSettings.isActiveMenu = false
                            btnAllTools.isActiveMenu = false
                            stackView.push(Qt.resolvedUrl(
                                               "dhcp_starvation.qml"))
                        }
                    }

                    AppButton {
                        id: btnVTP
                        text: "DHCP Starvation\nDetector"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150
                        onClicked: {
                            btnHome.isActiveMenu = false
                            btnSettings.isActiveMenu = false
                            btnAllTools.isActiveMenu = false
                            stackView.push(Qt.resolvedUrl("dhcp_starvation_detector.qml"))
                        }
                    }

                    AppButton {
                        id: btnRouge_DHCP
                        text: "Rouge \n DHCP"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150
                        onClicked: {
                            btnHome.isActiveMenu = false
                            btnSettings.isActiveMenu = false
                            btnAllTools.isActiveMenu = false
                            stackView.push(Qt.resolvedUrl("rougeDHCP.qml"))
                        }
                    }

                    AppButton {
                        id: btnRDHCP_Detector
                        text: "Rouge DHCP \n Detector"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150
                        onClicked: {
                            btnHome.isActiveMenu = false
                            btnSettings.isActiveMenu = false
                            btnAllTools.isActiveMenu = false
                            stackView.push(Qt.resolvedUrl(
                                               "rougeDHCP_Detector.qml"))
                        }
                    }

                    AppButton {
                        id: btnARP_Spoofer
                        text: "Arp \nSpoofer"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150

                        onClicked: {
                            btnHome.isActiveMenu = false
                            btnSettings.isActiveMenu = false
                            btnAllTools.isActiveMenu = false
                            stackView.push(Qt.resolvedUrl("arp_spoofer.qml"))
                        }
                    }

                    AppButton {
                        id: btnASpoofer_Detector
                        text: "Arp Spoofer \n Detector"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150
                    }

                    AppButton {
                        id: btnDNS_Poison
                        text: "DNS \n Poisoning"
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150
                    }

                    AppButton {
                        id: btnCDP
                        text: "CDP"
                        Layout.fillHeight: false
                        Layout.maximumWidth: 200
                        Layout.fillWidth: true
                        Layout.preferredHeight: 120
                        Layout.preferredWidth: 150
                    }
                }
            }

            Label {
                id: labelRecent
                x: -40
                width: 200
                height: 25
                color: "#5c667d"
                text: qsTr("Recently Used Tools")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: labelTextName.bottom
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                anchors.topMargin: 30
                font.italic: true
                font.bold: false
                anchors.leftMargin: 25
                anchors.rightMargin: 10
                font.pointSize: 10
            }
        }
    }

    Connections {
        target: backend

        function onSetName(name) {
            labelTextName.text = name
        }

        function onPrintTime(time) {
            labelDate.text = time
        }

        function onIsVisible(isVisible) {
            rectangleVisible.visible = isVisible
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:800}
}
##^##*/

