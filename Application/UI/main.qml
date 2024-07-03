import QtQuick
import QtQuick.Controls.Basic
import QtMultimedia

ApplicationWindow {
    visible: true
    width: 600
    height: 300
    flags: Qt.FramelessWindowHint | Qt.Window
    title: "trafficTracker"

    property string currTime: "00:00:00"
    property QtObject backend

    Rectangle {
        anchors.fill: parent
    
        //Video {
        //    id: video
        //    width : parent.width
        //    height : parent.height
        //    source: "./videos/video.mp4"
            
        //    MouseArea {
        //        anchors.fill: parent
        //        onClicked: {
        //            video.play()
        //        }
        //    }

        //    Keys.onSpacePressed: video.playbackState == MediaPlayer.PlayingState ? video.pause() : video.play()
        //    Keys.onLeftPressed: video.seek(video.position - 5000)
        //    Keys.onRightPressed: video.seek(video.position + 5000)
        //}

        Image {
                sourceSize.width: parent.width
                sourceSize.height: parent.height
                source: "./videos/doorway.jpg"
                fillMode: Image.PreserveAspectFit
        }

        Text {
            anchors {
                bottom: parent.bottom
                bottomMargin: 60
                left: parent.left
                leftMargin: 12
            }
            text: "People In:"
            font.pixelSize: 24
            color: "black"
        }

        Text {
            anchors {
                bottom: parent.bottom
                bottomMargin: 36
                left: parent.left
                leftMargin: 12
            }
            text: "People Out:"
            font.pixelSize: 24
            color: "black"
        }

        Text {
            anchors {
                bottom: parent.bottom
                bottomMargin: 12
                left: parent.left
                leftMargin: 12
            }
            text: currTime
            font.pixelSize: 24
            color: "black"
        }
    }
    
    Connections {
        target: backend

        function onUpdated(msg) {
            currTime = msg;
        }
    }    
}