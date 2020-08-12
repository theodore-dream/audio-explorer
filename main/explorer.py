#!/usr/bin/python3
# testing xml structuring before trying to do anything else with api output 
# https://docs.python.org/3/library/xml.etree.elementtree.html

import subprocess
import requests
import xml.etree.ElementTree as ET

# this is basically a python version of this bash script with custom additions for my purposes
# https://gist.github.com/andersan/3f619becaebb7bb53c20c1772a77c3f9/revisions

payload = {'music'}
r = requests.get('http://opml.radiotime.com/Search.ashx?query=' + str(payload))
#print(r.text)
#print(r.headers)

# set the XML document root

root = ET.fromstring(r.content)

# https://sdbrett.com/BrettsITBlog/2017/03/python-parsing-api-xml-response-data/
# this provides the topology elements, and each element contains attributes, 
# seems all stations are under "outline" element

#for child in root.iter('*'):
#    print(child.tag, child.attrib)
#    print(child.tag)

# this provides child attributes under the element, it shows the stations under "outline element"

#for child in root.iter('*'):
#     print(child.tag, child.attrib)

# now we can isolate key:value pairings within the child attribute 'outline'
# this shows us a slightly more nicely formatted list
#for child in root.iter('outline'):
#     print(child.attrib['URL'], child.attrib['text'])

#testing... 

x = 0 
URL_list = []
text_list = []
subtext_list = []

for child in root.iter('outline'): 
    x = x + 1
    print(x)
    if 'URL' in child.attrib:
        URL = child.attrib['URL']
        URL_list.append(URL)
    if 'text' in child.attrib:
        text = child.attrib['text']
        text_list.append(text)
    if 'subtext' in child.attrib:
        subtext = child.attrib['subtext']
        subtext_list.append(subtext)

print(URL_list)
print(text_list)
print(subtext_list)
  
print(URL_list[22])
print(text_list[22])
print(subtext_list[22])
