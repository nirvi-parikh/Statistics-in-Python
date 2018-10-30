# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:04:51 2018

@author: nirvi
"""

from math import sqrt

#-----------------------
#taking input from user
#-----------------------
len=int(input())
data=list(map(int,input().split()))

#----------------
#calculating mean
#----------------
total=0
for items in data:
    total=total+items

mean=(total/len)

#------------------------------
#calculating standard deviation
#------------------------------
i=0
sum=0
difference=0
while i < len:
    difference= data[i] - mean
    sum=sum+difference**2
    i=i+1

sd=sqrt(sum/len)

print("%.1f" % sd)
