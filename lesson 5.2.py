# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:11:21 2019

@author: Dan Gaecklein

Write a program that repeatedly prompts a user for integer 
until the user enters 'done'. Once 'done' is entered,
print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number 
catch it with a try/except and 
put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below. 
 
 
 Invalid input
Maximum is 10
Minimum is 2
"""
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
#    print (n)
    if num == "done" : break
    try:
        n = int(num)
    except:
        n = None
    
    if n is None :
        inval_flg = 'Y'
        continue
    if smallest is None :
        smallest = n
    elif n < smallest :
        smallest = n
    elif largest is None :
        largest = n
    elif n > largest :
        largest = n
   
        
if inval_flg == 'Y' :
    print('Invalid input')
print("Maximum is", largest)
print("Minimum is", smallest)