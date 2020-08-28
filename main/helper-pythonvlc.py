#!/usr/bin/env python3

# sudo apt install vlc python3-vlc   <<< run this first for dependencies
# i previously had this working and now it won't work any more, abandoning this direction for now.

import vlc


p = vlc.MediaPlayer('http://s1.voscast.com:8652')
p.play()
print(sys.executable)
