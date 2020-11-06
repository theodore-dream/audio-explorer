#!/usr/bin/python3

# simple HTTP requests command to TuneIn API - this is a development/debugger helper utility
# this will give you raw xml data of the results for any given query

import subprocess
import requests

query = {'animals'}
r = requests.get('http://opml.radiotime.com/Search.ashx?query=' + str(query))
print(r.text)
#print(r.headers)
