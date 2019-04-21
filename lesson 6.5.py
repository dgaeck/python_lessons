# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:43:45 2019

@author: Dan Gaecklein

Write code using find() and string slicing (see section 6.10)
to extract the number at the end of the line below.
Convert the extracted value to a floating point number 
and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475";
start_loc = text.find("0")
#print(start_loc)
stop_loc = text.find("5",start_loc)
#print(stop_loc)
final = text[start_loc:stop_loc+1]
#print(final)
final_num=float(final)
print(final_num)