import QtQuick 2.5
import QtQuick.Controls 2.5
import QtMultimedia


ApplicationWindow{

    visible:true
    width:600
    height:400
    title:"Play Video"

    MediaPlayer{

        id:player
        source:"Avengers.mp4"
        audioOutput:audioOutput
        videoOutput:videoOutput

    }

    AudioOutput{

        id:audioOutput
        volume:volumeSlider.value

    }

    VideoOutput{

        id:videoOutput
        anchors.fill:parent
    }


    Component.onCompleted : {
        player.play()
    }

    Slider {

        id:volumeSlider
        anchors.bottom:parent.bottom
        anchors.right:parent.right
        anchors.margins:10
        orientation:Qt.Horizontal
        value:0.5
    }

    Slider{

        id:progressSlider
        width:parent.width
        anchors.bottom:parent.bottom
        enabled:player.seekable
        value:player.duration > 0 ? player.position / player.duration : 0

    onMoved:function(){
        player.position = player.duration * progressSlider.position
    }
    }
}