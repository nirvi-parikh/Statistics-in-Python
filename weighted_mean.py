# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#-----------------------
#taking input from user
#-----------------------
length=int(input())
numbers=list(map(int,input().split()))
weights=list(map(int,input().split()))

#----------------
#calculating weighted mean
#----------------
total=0
sum=0
i=0

while i<length:
    total=total+ numbers[i]*weights[i]
    sum=sum+weights[i]
    i=i+1

weighted_mean=(total/sum)

print("%.1f" %weighted_mean)

