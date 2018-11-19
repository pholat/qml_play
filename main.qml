import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello")

    Rectangle {
        id: bg_rec
        color: "oldlace"
        height: parent.height
        width: parent.width
    }
    Rectangle {
        id: text_view_rect
        border.width: 4
        border.color: black
        width: parent.width
        height: parent.height * 0.8
        color: bg_rec.color

        Image {
            source: "chibi_bg.jpg"
            anchors.bottom: text_view.bottom
            anchors.horizontalCenter: parent.horizontalCenter
        }

        TextEdit {
            id: text_view
            objectName: "text_view"
            width: parent.width - 4
            height: parent.height - 4
            color: "black"
            text: qsTr("long class")
            font.pixelSize: 18
            anchors.margins: 5
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    Rectangle {
        anchors.top: text_view_rect.bottom
        border.width: 4
        color: bg_rec.color
        border.color: black
        width: parent.width
        height: parent.height - text_view_rect.height

        TextEdit {
            id: text_input
            width: parent.width - parent.border.width*2
            height: parent.height - parent.border.width*2
            color: "#ef1d1d"
            text: qsTr("")
            font.capitalization: Font.MixedCase
            font.pixelSize: 18
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }
}
