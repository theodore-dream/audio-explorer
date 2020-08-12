#!/usr/bin/python3

# simple HTTP requests command to API 

import subprocess
import requests

payload = {'sports'}
r = requests.get('http://opml.radiotime.com/Search.ashx?query=' + str(payload))
print(r.content)
#print(r.headers)
