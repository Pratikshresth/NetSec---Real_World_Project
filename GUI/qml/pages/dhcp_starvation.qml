import QtQuick 2.15
import QtQuick.Controls 2.15
import "../controls"
import "../pages"
import QtQuick.Layouts 1.15

Item {
    Rectangle {
        id: rectangle
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

            AppButton {
                id: btnBack
                text: "< Back"
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.leftMargin: 9
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
                width: 200
                color: "#55aaff"
                text: qsTr("DHCP Starvation Attack")
                anchors.left: btnBack.right
                anchors.right: rectangleMode.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.bottomMargin: 10
                anchors.topMargin: 10
                font.bold: false
                anchors.leftMargin: 25
                anchors.rightMargin: 25
                font.pointSize: 14
            }

            Rectangle {
                id: rectangleMode
                x: 230
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.topMargin: 10
                anchors.bottomMargin: 10
                anchors.rightMargin: 10
                color: "#5c667d"
                width: 300

                Label {
                    id: labelNormal
                    width: 90
                    color: "#fdfdfd"
                    text: qsTr("Normal Mode")
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.pointSize: 9
                    anchors.leftMargin: 15
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0
                }

                Label {
                    id: labelPersistent
                    width: 90
                    color: "#ffffff"
                    text: qsTr("Persistent Mode")
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.rightMargin: 15
                    anchors.topMargin: 0
                    font.pointSize: 9
                    anchors.bottomMargin: 0
                }

                Switch {
                    id: switchMode
                    anchors.left: labelNormal.right
                    anchors.right: labelPersistent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0
                    position:0
                    function marker()
                        {
                            checked = false
                            if(position==0)
                            {
                                checked = false

                            }
                            return checked
                        }
                    checked : backend.showHideRectangle(marker())
                    onToggled: {
                        backend.showHideRectangle(switchMode.checked)
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
            anchors.topMargin: 15

            Label {
                id: labelTextName
                color: "white"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: comboBox.bottom
                anchors.bottom: row.top
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignTop
                anchors.rightMargin: 10
                anchors.leftMargin: 10
                anchors.topMargin: 15
                anchors.bottomMargin: 20
                font.bold: false
                font.pointSize: 10
            }

            Row {
                id: row
                x: 327
                y: 273
                width: 90
                height: 41
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 15
                anchors.rightMargin: 20
                spacing: 12

                Button {
                    id: buttonStart
                    width: 90
                    height: 40
                    text: qsTr("Start")
                    font.letterSpacing: 1.5
                    font.bold: false
                    font.pointSize: 10
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    palette {
                        button: "#5c667d"
                        buttonText: "#fdfdfd"
                    }
                    onClicked: {
                        backend.dhcp("Starting DHCP Starvation .....")
                        // console.log("The mouse was pressed")
                        // console.log(comboBox.currentText)
                        // backend.getting(comboBox.currentText)
                        backend.startattack(switchMode.checked + ":" + comboBox.currentText)
                    }
                }
            }
            Rectangle {
                id: rectangleVisibleP
                visible: false
                color: "#1d2128"
                radius: 10
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: rectangleTop.bottom
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 27
                anchors.rightMargin: 50
                anchors.leftMargin: 50
                anchors.topMargin: 15

                CustomTextField {
                    id: textFieldP
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: rowP.top
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                    anchors.bottomMargin: 20
                    anchors.topMargin: 20
                }

                Row {
                    id: rowP
                    x: 329
                    y: 267
                    width: 203
                    height: 41
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 10
                    anchors.rightMargin: 10
                    spacing: 12

                    Button {
                        id: buttonStartP
                        width: 60
                        height: 40
                        text: qsTr("Start")
                        font.letterSpacing: 1
                        font.pointSize: 9
                        palette {
                            button: "#5c667d"
                            buttonText: "#fdfdfd"
                        }
                    }

                    Button {
                        id: buttonPause
                        width: 60
                        height: 40
                        text: qsTr("Pause")
                        font.letterSpacing: 1
                        font.pointSize: 9
                        palette {
                            button: "#5c667d"
                            buttonText: "#fdfdfd"
                        }
                    }

                    Button {
                        id: buttonStop
                        width: 60
                        height: 40
                        text: qsTr("Stop")
                        font.letterSpacing: 1
                        font.pointSize: 9
                        palette {
                            button: "#5c667d"
                            buttonText: "#fdfdfd"
                        }
                    }
                }
            }

            Label {
                id: labelInterface
                x: 251
                width: 126
                color: "#55aaff"
                text: qsTr("Select Interface ")
                font.pointSize: 11
                anchors.right: comboBox.left
                anchors.top: parent.top
                anchors.bottom: labelTextName.top
                anchors.bottomMargin: 20
                anchors.topMargin: 20
                anchors.rightMargin: 15
            }

            ComboBox {
                id: comboBox
                x: 380
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 10
                anchors.topMargin: 10
                model: comModel


        }
        Connections {
            target: backend

            function onSetName(name) {
                labelTextName.text = name
            }

            function onIsVisible(isVisible) {
                rectangleVisibleP.visible = isVisible
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:10}D{i:19}
}
##^##*/

}