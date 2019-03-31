# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:02:04 2019

@author: Dan Gaecklein

Write a program to prompt the user for hours and rate per hour 
using input to compute gross pay. Pay should be the normal rate 
for hours up to 40 and time-and-a-half for the hourly rate for
all hours worked above 40 hours. Put the logic to do the 
computation of pay in a function called computepay() and use 
the function to do the computation. 
The function should return a value. Use 45 hours 
and a rate of 10.50 per hour to test the program (the pay should
 be 498.75). You should use input to read a string and float() 
to convert the string to a number. Do not worry about error 
checking the user input unless you want to - 
you can assume the user types numbers properly. 
Do not name your variable sum or use the sum() function. 
"""

def computepay(h,r):
    if h > 40.0:
        ot = h - 40
        base = h - ot
        print(ot)
        print(base)
        ot_pay = ot_rate * ot
        base_pay = r * base
        gross_pay = ot_pay + base_pay
        print(gross_pay)
        return gross_pay
    else:
        base_pay = r * h
        print(base_pay)
        

    
hours = input("Enter Hours:")
rate = input("Enter Rate:")

try:
   h =float(hours)      
except:
    h = -1

try:
   r =float(rate)      
except:
    r = -1    
    
ot_rate = float(rate) * 1.5   
    
p = computepay(h,r)
print("Pay",p)