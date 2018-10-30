# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:36:54 2018

@author: nirvi
"""

#-----------------------
#taking input from user
#-----------------------
length=int(input())
data=list(map(int,input().split()))
data.sort()
#-------------------
#calculating median
#-------------------

def median(data):
    l=len(data)
    if (l%2==0):
        median = (data[l//2] + data[(l//2)-1])/2
    else:
        median = data[l//2]
        
    return median
    
mid=length//2
if (length%2==0):
    lowerQ = data[:mid]
    upperQ = data[mid:]
    
else:
    lowerQ = data[:mid]
    upperQ = data[mid+1:]
    

Q1= median(data)
Q2= median(lowerQ)
Q3= median(upperQ)

print("%d" %Q2)
print("%d" %Q1)
print("%d" %Q3)
