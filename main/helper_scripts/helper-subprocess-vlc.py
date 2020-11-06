#!/usr/bin/python3
# this is a simple helper script to test using vlc with subprocess to play a specific url 

import subprocess
import shlex
from subprocess import * 



cmd = 'cvlc -I dummy --no-video --aout=alsa --alsa-audio-device default --file-logging --logfile=vlc-log.txt --verbose 3 http://s1.voscast.com:8652'
args = shlex.split(cmd)
print(args)



vlc = subprocess.run(args, shell=False)
poll = p.poll()
if poll == None:
   print("running...")
