#!/usr/bin/python3

# simple HTTP requests command to API 

import subprocess
import requests

query = {'animals'}
r = requests.get('http://opml.radiotime.com/Search.ashx?query=' + str(query))
print(r.text)
#print(r.headers)
