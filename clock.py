#!/usr/bin/python

import time

rectime = ""
i = 0
ad="tes"
while True:
    curtime = time.strftime("%H:%M:%S")
    if curtime!=rectime and i == 0:
        ad=curtime
        print(ad)
        i=i+1
    elif curtime !=rectime:
        rectime=curtime
        print (curtime)
        print (ad)
        i=i+1

