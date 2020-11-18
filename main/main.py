#!/usr/bin/python3

# reference for xml module
# https://docs.python.org/3/library/xml.etree.elementtree.html
# this was originally based off of this script https://gist.github.com/andersan/3f619becaebb7bb53c20c1772a77c3f9/revisions

import subprocess
# from subprocess import Popen
import requests
import xml.etree.ElementTree as ET
import random
import shlex
from shlex import split
import vlc

# setting the file path to vlc for later use per https://linuxconfig.org/how-to-play-audio-with-vlc-in-python
player = vlc.MediaPlayer("/usr/bin/vlc")
#player = vlc.MediaPlayer(vlc.Instance("-I dummy --no-video --aout=alsa --file-logging --logfile=vlc.txt"))

# specify the search query and send http request to TuneIn API 
query = {'cat'}
r = requests.get('http://opml.radiotime.com/Search.ashx?query=' + str(query))

# set the XML document root of the http response XML page
root = ET.fromstring(r.content)

# setting variables that hold empty lists so we can append strings to the list
x = 0 
URL_list = []
text_list = []
subtext_list = []
key_list = []
track_list = []

# setting a global variable for line_no to capture how many station results we get

def line_number_set():
   global line_no
   line_no  = 0 

line_number_set()

# for loop going through each string in 'outline' from the XML output 
# and appending each string to the respective list variable

for child in root.iter('outline'): 
    line_no = line_no + 1
    if 'URL' in child.attrib:
        URL = child.attrib['URL']
        URL_list.append(URL)
    if 'text' in child.attrib:
        text = child.attrib['text']
        text_list.append(text)
    if 'subtext' in child.attrib:
        subtext = child.attrib['subtext']
        subtext_list.append(subtext)
    if 'key' in child.attrib:
        key = child.attrib['key']
        key_list.append(key)
    if 'current_track' in child.attrib:
        track = child.attrib['current_track']
        track_list.append(track) 


# selecting my random radio station

def randomselect():
    global line_no
    total_stations = line_no
    line_no = random.randrange(0, line_no, 1)
    print("=========================================================")
    print("Station " + str(line_no) + " randomly selected out of " + str(total_stations) + " total stations found") # add function here for the keyword used for the search?
    print("=========================================================")
    print("Station Name: " + text_list[(line_no)]) 
    print("---------------------------------------------------------")
    print("Note: " + subtext_list[line_no]) 
    print("URL: " + URL_list[line_no])

def stream():
    
   # get the actual url
   url = requests.get(URL_list[(line_no)])
   print(url.text)
   #vlc_arg = 'vlc -I dummy --no-video --aout=alsa'
   #vlc_arg = split(vlc_arg) 
   #print(vlc_arg)
   #media = instance.media_new(url.text)
   #player.media_new_location(url.text)
   #player.set_media(media)
   
   i = vlc.Instance("-I dummy --avcodec-dr --avcodec-workaround-bugs=1 --no-video --aout=alsa --file-logging --logfile=vlc-log.txt --verbose 3")
   player = i.media_player_new()
   Media = i.media_new(url.text)
   Media.get_mrl()
   player.set_media(Media)
   #player.libvlc_media_new_location(url.txt)
   player.play()

randomselect()
stream()









# this is part of randomselect() that I wasn't able to get to work,
# if the track_list and key had a string for that particular station I wanted to print it

#    if track_list[line_no] == line_no:
#        print(track_list[(line_no)])
#        continue
#    if key[line_no] == line_no:
#        print(key[line_no])
#        continue
#    else:
#        print("done")

