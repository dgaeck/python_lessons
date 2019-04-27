# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:16:00 2019

@author: Dan Gaecklein

Count these lines and extract the floating point values 
from each of the lines and compute the average of those 
values and produce an output as shown below. 
Do not use the sum() function or a 
variable named sum in your solution. 
"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter filename: ")
fh = open(fname)
count=0
num = 0
avg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    start_loc = line.find("0")
    #print(start_loc)
    final = line[start_loc:start_loc+6]
    #print(final)
    final_num=float(final)
    num = num + final_num
    print(line)
    print(num)
avg = num / count
#print (avg)
#print("Done")
print("Average spam confidence:", avg)
