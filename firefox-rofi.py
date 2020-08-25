#!/usr/bin/env python3

from rofi import Rofi
import json
import subprocess
r = Rofi()

with open("websitelist.json","r") as websitelist:
	websiteList = json.loads(websitelist.read())

index, key = r.select('website', websiteList)

if (key == -1):
	exit()

subprocess.run(["firefox","--new-tab",websiteList[index]])