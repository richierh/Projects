#!/usr/bin/python

import datetime

import datetime, time
then = datetime.datetime.now() + datetime.timedelta(seconds=10)
while then > datetime.datetime.now():
    print 'sleeping'
"""
l = datetime.timedelta(seconds=50)+datetime.datetime.now()
k = l.strftime("%H:%M:%S")
print (k) 
"""
"""
def timerunning(rec_time):
    strt_time = rec_time
    curtime=datetime.datetime.now()
    curtime = curtime.strftime("%H:%M:%S")
    while True:
        curtime = datetime.datetime.now()
        curtime=curtime.strftime("%H:%M:%S")

        if curtime !=rec_time:
            rec_time=curtime
            print (rec_time)
            print (strt_time)            
            #print (ad)
    return curtime,ad

if __name__=="__main__":
    rec_time = "20:18:15"
    strt_time = rec_time
    timerunning(rec_time)
"""