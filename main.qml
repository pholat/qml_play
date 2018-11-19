import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello")

    TextEdit {
        id: text_view
        objectName: "text_view"
        x: 0
        y: 0
        width: parent.width
        height: parent.height * 0.8
        color: "black"
        text: qsTr("long class")
        font.pixelSize: 12
        anchors.margins: 5
    }

    TextEdit {
        id: text_input
        anchors.top: text_view.bottom
        width: parent.width
        height: parent.height - text_view.height
        color: "#ef1d1d"
        text: qsTr("")
        font.capitalization: Font.MixedCase
        font.pixelSize: 12
    }
}
