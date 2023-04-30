# -*- coding: utf-8 -*-
"""
Lesson 3.1

Write a program to prompt the user for hours and rate per hour using 
input to compute gross pay. Pay the hourly rate for the hours up 
to 40 and 1.5 times the hourly rate for all hours worked 
above 40 hours. Use 45 hours and a rate of 10.50 per hour 
to test the program (the pay should be 498.75). 
You should use input to read a string and float() 
to convert the string to a number.

Created on Sun Mar 17 12:41:24 2019

@author: Dan Gaecklein
"""

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
"ot_rate = float(rate) * 1.5"
ot_rate = float(rate) * 2.0
r = float(rate)

if h > 40.0:
    ot = h - 40
    base = h - ot
    print(ot)
    print(base)
    ot_pay = ot_rate * ot
    base_pay = r * base
    gross_pay = ot_pay + base_pay
    print(gross_pay)
else:
    base_pay = r * h
    print(base_pay)