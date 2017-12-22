#/usr/bin/python

import os

print os.getcwd()
path = "/mpos"
lists = os.listdir(os.getcwd()+path)

for thelist in xrange(len(lists)):    
    print(lists[thelist])
    executing = lists[thelist]
    os.system("2to3 -w -f except {}".format(executing))