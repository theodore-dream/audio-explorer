
import subprocess
import requests
import xml.etree.ElementTree as ET
import random
import shlex
from shlex import split


query = {'pop'}
r = requests.get('http://opml.radiotime.com/Search.ashx?query=' + str(query))
root = r.content

root = ET.fromstring(r.content)
print(root.tag)
print(root.attrib)

for child in root:
   print(child.tag, child.attrib)

