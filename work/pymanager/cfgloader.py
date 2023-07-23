#!/usr/bin/python3
import json
import sys
import time
import os.path

class myClass:
    def __init__(self, my_name):
        self.my_name = my_name
        self.counter = 0
    def run(self):
        while True:
           time.sleep(1)
           self.counter += 1

    def saveMe(self):
        return json.dumps(self.__dict__)
    def loadMe(self,dict):
        self.__dict__ = json.loads(dict)

if len(sys.argv) < 2:
    sys.argv.append("test")

a = myClass(f"{sys.argv[1]}")

cfg = ""
if os.path.isfile(f"{sys.argv[0]}.cfg"):
    with open(f"{sys.argv[0]}.cfg") as f:
        cfg = f.readline()
        a.loadMe(cfg)
try:
    print(f"Running: {cfg}")
    a.run()
except:
    with open(f"{sys.argv[0]}.cfg","w") as f:
        f.write(a.saveMe())
    sys.exit(1)