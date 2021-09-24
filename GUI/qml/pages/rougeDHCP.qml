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
                text: qsTr("Rouge DHCP Attack")
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
            anchors.topMargin: 10

            Rectangle {
                id: rectangleLabel
                height: 101
                color: "#495163"
                radius: 10
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 10
                anchors.leftMargin: 10
                anchors.topMargin: 10

                GridLayout {
                    id: gridApp
                    anchors.fill: parent
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                    anchors.bottomMargin: 20
                    anchors.topMargin: 5
                    rows: 2
                    columns: 4
                    CustomTextField {
                        id: textField
                        placeholderText: "Rouge IP"
                        implicitWidth: 100
                        implicitHeight: 40
                        Layout.maximumWidth: 300
                        Layout.fillWidth: true
                        Layout.preferredHeight: 40
                        Layout.preferredWidth: 90
                    }
                    CustomTextField {
                        id: textField1
                        placeholderText: "Rouge Gateway"
                        implicitWidth: 100
                        implicitHeight: 40
                        Layout.maximumWidth: 300
                        Layout.fillWidth: true
                        Layout.preferredHeight: 40
                        Layout.preferredWidth: 90
                    }
                    CustomTextField {
                        id: textField2
                        placeholderText: "Rouge Network"
                        implicitWidth: 100
                        implicitHeight: 40
                        Layout.maximumWidth: 300
                        Layout.fillWidth: true
                        Layout.preferredHeight: 40
                        Layout.preferredWidth: 90
                    }
                    CustomTextField {
                        id: textField3
                        placeholderText: "Rouge Subnet"
                        implicitWidth: 100
                        implicitHeight: 40
                        Layout.maximumWidth: 300
                        Layout.fillWidth: true
                        Layout.preferredHeight: 40
                        Layout.preferredWidth: 90
                    }
                    CustomTextField {
                        id: textField4
                        placeholderText: "Rouge Domain"
                        implicitWidth: 100
                        implicitHeight: 40
                        Layout.maximumWidth: 300
                        Layout.fillWidth: true
                        Layout.preferredHeight: 40
                        Layout.preferredWidth: 90
                    }
                    CustomTextField {
                        id: textField5
                        placeholderText: "Rouge DNS"
                        implicitWidth: 100
                        implicitHeight: 40
                        Layout.maximumWidth: 300
                        Layout.fillWidth: true
                        Layout.preferredHeight: 40
                        Layout.preferredWidth: 90
                    }
                    Label {
                        id: labelInterface
                        color: "#55aaff"
                        text: qsTr("Select Interface ")
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: 11
                        Layout.maximumWidth: 300
                        Layout.fillWidth: true
                        Layout.preferredHeight: 40
                        Layout.preferredWidth: 90
                    }

                    ComboBox {
                        id: comboBox
                        implicitWidth: 90
                        implicitHeight: 40
                        Layout.maximumWidth: 300
                        Layout.fillWidth: true
                        Layout.preferredHeight: 40
                        Layout.preferredWidth: 90
                        model: comModel
                    }
                }
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
                        backend.dhcp("Starting Rouge DHCP Server .....")
                        // console.log("The mouse was pressed")
                        // console.log(comboBox.currentText)
                        // backend.getting(comboBox.currentText)
                        backend.RougeDHCP(textField.text + ":" + comboBox.currentText + ":" + textField1.text + ":" + textField2.text + ":" + textField3.text
                        + ":" + textField4.text + ":" + textField5.text)
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

