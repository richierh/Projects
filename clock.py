#!/usr/bin/python

import time

def timerunning():
    rectime = ""
    ad="tes"
    curtime=time.strftime("%H:%M:%S")
    ad = curtime
    while True:
        curtime = time.strftime("%H:%M:%S")

        if curtime !=rectime:
            rectime=curtime

            
            #print (ad)
    return curtime,ad

if __name__=="__main__":
    timerunning()