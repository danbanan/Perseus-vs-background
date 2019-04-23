# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:40:42 2019

Python Program that extracts the ObjectName. RA. DEC. RedSjoft. Redshift Flag
from a NED.txt file into a CSV file.

@author: Steven Li
"""

import csv
import os
import sys

#Setup
perseus = []
background = []

#Functions
def find_nth(line,char,n):
    start = line.find(char)
    while start >= 0 and n > 1:
        start = line.find(char , start+len(char))
        n -= 1
    return start

def extract(path):
    arr = []
    with open(path) as file:
        ln = file.readline()
        while ln and len(ln) > 1:
            name_start = find_nth(ln,'|',1)
            ra_start = find_nth(ln,'|',2)
            dec_start = find_nth(ln,'|',3)
            stop = find_nth(ln,'|',4)
            rs_start = find_nth(ln,'|',6)
            rsf_start = find_nth(ln,'|',7)
            end = find_nth(ln,'|',8)
            name = ln[name_start+2:ra_start-1].replace(" ","")
            ra = ln[ra_start+2:dec_start-1].replace(" ","")
            dec = ln[dec_start+2:stop-1].replace(" ","")
            rs = ln[rs_start+2:rsf_start-1].replace(" ","")
            rsf = ln[rsf_start+2:end-1].replace(" ","")
            arr.append([name,ra,dec,rs,rsf])
            ln = file.readline()
    arr.pop() #Throw away last empty
    return arr

def write(arr,name):
    with open(name,"w+", newline='') as my_csv:
        csvWriter = csv.writer(my_csv)
        csvWriter.writerows(arr)
        
def main():
    print('Converts NED .txt file in Name, RA, DEC .csv file. ')
    print('Input File Path: ')
    filepath = input().replace(" ","")
    print('Input New CSV name: ')
    filename = input().replace(" ","")

    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       exit
     
    array = extract(filepath)
      
    if os.path.isfile(filename+".csv"):
        print("File exists, overwrite (Y/N)?")
        x = input().lower()
        if ((x == 'y') or (x == 'yes')):
            if(write(array,filename+".csv")):
                print("{}.csv created succesfully.".format(filename))
            else:
                print("{}.csv created unsuccesfully.".format(filename))
        else:
            exit
    else:
        write(array,filename+".csv")

if __name__ == '__main__':  
   main()
