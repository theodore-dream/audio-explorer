#!/usr/bin/python3

# can now only flilter on live stations
# still need to eliminate anything where a endpoint url gives an xml stylesheet instead of just playing the station, because that's a problem 
# i note that URLs that lead to XML sheets with recordings (even if they are item=station) all have URLs with "pbrowse" or "Browse.ashx" in them
# also need to add some kind of basic logging

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
    query = {'house party'}
    r = requests.get('http://opml.radiotime.com/Search.ashx?query=' + str(query))
    return r.content

def xml_parse(raw_query_result):
    # set the XML document root of the http response XML page
    root = ET.fromstring(raw_query_result)
    # setting variables that hold empty lists so we can append strings to the list
    return root

# for loop going through each string in 'outline' from the XML output 
# and appending each string to the respective list variable

def iterate(set_root):
    item_list, URL_list, text_list, subtext_list, track_list, station_data = [], [], [], [], [], []
    root = set_root 
    for child in root.iter('outline'): 
        line_no = 0
        line_no = line_no + 1
        if 'item' in child.attrib:
            item = child.attrib['item']
            item_list.append(item)
        if 'URL' in child.attrib: 
            URL = child.attrib['URL']
            URL_list.append(URL)
        if 'text' in child.attrib:
            text = child.attrib['text']
            text_list.append(text)
        if 'subtext' in child.attrib:
            subtext = child.attrib['subtext']
            subtext_list.append(subtext)
        if 'current_track' in child.attrib:
            track = child.attrib['current_track']
            track_list.append(track) 
    return item_list, URL_list, text_list, subtext_list, track_list

# this function seperates out anything that is not "item=station" which removes anything that isn't a live show 

def stationsfilter(item_list, URL_list, text_list, subtext_list, track_list):
    items, URLs, texts, subtexts, keys, tracks = [], [], [], [], [], []
    for i in range(len(item_list)):
       if (item_list[i]) == "topic":
          continue
       if (item_list[i]) == "show":
          continue
       items.append(item_list[i])
       URLs.append(URL_list[i])
       texts.append(text_list[i])
       subtexts.append(subtext_list[i])
       tracks.append(track_list[i])
       # this shows me only stations are returning
       # print(items[i])
       # print(URLs[i])
    return items, URLs, texts, subtexts, tracks       
    
   
def randomselect(items, URLs, texts, subtexts, tracks):     
    total_stations = len(URLs)
    selected = random.randrange(1, total_stations, 1)
    random_URL = URLs[selected]
    random_text = texts[selected]
    random_subtext = subtexts[selected]
    random_track = tracks[selected]
    print (random_text)
    print (random_subtext)
    print (random_track)
    print (random_URL)
    # will need to add a way to check real URL somewhere)
    return items, random_URL, random_text, random_subtext, random_track          

#def randomselect(items, URLs, texts, subtexts, keys, tracks):     
#            total_stations = len(URLs)
#            selected = random.randrange(1, total_stations, 1)
#            print("=========================================================")
#            print("Station " + str(selected) + " randomly selected out of " + str(total_stations) + " total stations found") # add function here for the keyword used for the search?
#            print("=========================================================")
#            print("Station Name: " + texts[(selected)])  
#            print("---------------------------------------------------------")
#            print("Station Type: " + items[selected])
#            print("Note: " + subtexts[selected]) 
#            print("URL: " + URLs[selected])
#            url = requests.get(URLs[(selected)])
#            url = url.text
#            print(url)

# removing total stations here, should log it somewhere though, was giving error could not return it from above function

def stream(random_URL, random_text, random_subtext, random_track):
    try:
        cmd = 'cvlc -I dummy --no-video --aout=alsa --alsa-audio-device default --file-logging --logfile=vlc-log.txt --verbose 3 ' + str(random_URL)
        args = shlex.split(cmd)
        print(args)
#        print("testing connection to station " + str(selected) + " randomly selected out of " + str(total_stations) + "." 
#        print(args)
        subprocess.run(args, shell=False)
        logging.info()
        print("am i still doing stuff")
    except subprocess.TimeoutExpired:
        print("connection timeout") 
        


def gather_stream():
    # first we get raw xml from tunein query 
    raw_query_result = tunein_query()
    # then we set the root of the xml document and create empty list variables
    set_root = xml_parse(raw_query_result)
    # then iterate through the xml document children of 'outline' where the tunein results are
    # place the lists that we created into a list of lists 
    [item_list, URL_list, text_list, subtext_list, track_list] = iterate(set_root)
    # now we filter those lists to check for what is a live station and what isn't
    [items, URLs, texts, subtexts, tracks] = stationsfilter(item_list, URL_list, text_list, subtext_list, track_list) 
    # now we place these new filtered lists into randomselect function and stream
    [item, random_URL, random_text, random_subtext, random_track] = randomselect(items, URLs, texts, subtexts, tracks)
    stream(random_URL, random_text, random_subtext, random_track) 

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

