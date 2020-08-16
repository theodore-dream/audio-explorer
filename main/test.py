#!/usr/bin/python3

import vlc

# setting the file path to vlc for later use per https://linuxconfig.org/how-to-play-audio-with-vlc-in-python
player = vlc.MediaPlayer("/usr/bin/vlc")

def stream():

   url = "http://s1.voscast.com:8652/"
   i = vlc.Instance("-I dummy --no-video --aout=alsa --file-logging --logfile=vlc-log.txt --verbose 3")
   player = i.media_player_new()
   Media = i.media_new(url)
   player.set_media(Media)
   player.play()

stream()



## alternative very simple test... 
#p = vlc.MediaPlayer("http://s1.voscast.com:8652/")
#p.play()






