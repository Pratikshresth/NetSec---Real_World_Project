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
                text: qsTr(" DHCP Starvation Detection")
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
                        backend.StarveDetector("Starting Starvation")
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
