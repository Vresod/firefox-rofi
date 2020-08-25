#!/usr/bin/env python3

from rofi import Rofi
import json
import subprocess
r = Rofi()

with open("websitelist.json","r") as websitelist:
	websiteList = json.loads(websitelist.read())

index, key = r.select_with_entry('website',websiteList)

#print(index)
#print(key)

#if (key == -1):
#	exit()

#subprocess.run(["firefox","--new-tab",websiteList[index]])