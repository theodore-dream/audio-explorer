#!/usr/bin/python3

# this version of the script is basically barely working for the intended goal, but trying to increase code reusability and flexibility by moving away from only functions and also using classes
# reference for xml module
# https://docs.python.org/3/library/xml.etree.elementtree.html
# this was originally based off of this script https://gist.github.com/andersan/3f619becaebb7bb53c20c1772a77c3f9/revisions

import subprocess
import requests
import xml.etree.ElementTree as ET
import random
import shlex
from shlex import split


# specify the search query and send http request to TuneIn API 

def tunein_query():
    query = {'wxyc'}
    r = requests.get('http://opml.radiotime.com/Search.ashx?query=' + str(query))
    return r.content

def xml_parse(raw_query_result):
    # set the XML document root of the http response XML page
    root = ET.fromstring(raw_query_result)
    # setting variables that hold empty lists so we can append strings to the list
    x = 0 
    URL_list = []
    text_list = []
    subtext_list = []
    key_list = []
    track_list = []
    return root

# for loop going through each string in 'outline' from the XML output 
# and appending each string to the respective list variable

def iterate(set_root):
    URL_list, text_list, subtext_list, key_list, track_list, station_data = [], [], [], [], [], []
    root = set_root 
    for child in root.iter('outline'): 
        line_no = 0
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
    return URL_list, text_list, subtext_list, key_list, track_list

# selecting my random radio station - we're going to need URL_list and selected 
 
def stream(url):
    try:
        cmd = 'cvlc -I dummy --no-video --aout=alsa --alsa-audio-device default --file-logging --logfile=vlc-log.txt --verbose 3 ' + str(url)
        args = shlex.split(cmd)
        print(args)
        subprocess.run(args, shell=False)
    except subprocess.TimeoutExpired:
        print("connection timeout") 


def randomselect(URL_list, text_list, subtext_list, key_list, track_list):    

    def stream():
        try:
            cmd = 'cvlc -I dummy --no-video --aout=alsa --alsa-audio-device default --file-logging --logfile=vlc-log.txt --verbose 3 ' + str(url)
            args = shlex.split(cmd)
            print(args)
            subprocess.run(args, shell=False)
        except subprocess.TimeoutExpired:
            print("connection timeout")
    
    while True:      # [I can later add a button to interrupt this]
        try:        
            total_stations = len(URL_list)
            selected = random.randrange(1, total_stations, 1)
            print("=========================================================")
            print("Station " + str(selected) + " randomly selected out of " + str(total_stations) + " total stations found") # add function here for the keyword used for the search?
            print("=========================================================")
            print("Station Name: " + text_list[(selected)])  
            print("---------------------------------------------------------")
            print("Note: " + subtext_list[selected]) 
            print("URL: " + URL_list[selected])
            url = requests.get(URL_list[(selected)])
            url = url.text
            print(url)
            stream()
           #cmd = 'cvlc -I dummy --no-video --aout=alsa --alsa-audio-device default --file-logging --logfile=vlc-log.txt --verbose 3 ' +  str(url.text)
           #args = shlex.split(cmd)
           #print(args)
           #subprocess.run(args, shell=False) 
       # except subprocess.TimeoutExpired:
           # print("connection timeout") 
        except: 
           print('all done, bye')

def gather_stream():
    # first we get raw xml from tunein query 
    raw_query_result = tunein_query()
    # then we set the root of the xml document and create empty list variables
    set_root = xml_parse(raw_query_result)
    # then iterate through the xml document children of 'outline' where the tunein results are
    # place the lists that we created into a list of lists 
    [URL_list, text_list, subtext_list, key_list, track_list] = iterate(set_root)
    # now we place those child lists into randomselect function and print what we've selected
    randomselect(URL_list, text_list, subtext_list, key_list, track_list)


gather_stream()








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
