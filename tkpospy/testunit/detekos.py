#!/usr/bin/env python
import platform

class osplatform(object):
    #making simple class to identfy os platform
    def __init__(self,platform):
        self.platform = platform
        
    def checkplatform(self):
        if self.platform.system()=="Linux":
            print ("this is {}".format(platform.system()))
        elif self.platform.system()=="Windows":
            print ("this is {}".format(platform.system()))
        elif self.platform.system()=="Mac OS":
            print ("this is {}".format(platform.system()))
        else :
            print ("this is {}, unrecognize".format(platform.system()))    

if __name__=="__main__":            
    mypc = osplatform(platform)
    mypc.checkplatform()