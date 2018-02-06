#!/usr/bin/python

#import timer


#gui = timer.FullScreenApp()
import csv
class Csv():
    def __init__(self,parent):
        self.parent = parent
        self.a=None
        self.k = self.bacacsv()
        pass

    def kondisi(self):
        if self.parent == self.k:
            self.masukancsv()
        else :
            pass

    def bacacsv(self):
        with open('pass.csv', 'r') as csvfile:
            spamreader = csv.reader(csvfile)#, delimiter=' ', quotechar='|')
            for row in spamreader:
                self.a = ', '.join(row)
        return self.a
    
    def masukancsv(self):
        if self.parent == self.bacacsv():
            data =['ok']
            with open("pass.csv", "w") as csv_file:
                writer = csv.writer(csv_file)#, delimiter=',')
                self.hasil = writer.writerow(data)
        else :
            pass
        
        return self.hasil
        

maink = Csv("admin")
maink.kondisi()
print (maink.bacacsv())