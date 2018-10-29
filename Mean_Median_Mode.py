# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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

#-------------------
#calculating median
#-------------------

data.sort()
if (len%2==0):
    median = (data[len//2] + data[(len//2)-1])/2
else:
    median = data[len//2]

#--------------------
# count the frequency of each number in the data into a dictionary
#--------------------
numbers = dict()

for item in data:
    if item not in numbers:
        numbers[item] = 1
    else:
        numbers[item] = numbers[item] + 1

#--------------------
# calulate the mode
#--------------------

max_count = 0

for key in numbers:
    if numbers[key] > max_count:
        max_count = numbers[key]

max_modal_elements = []

for key in numbers:
    if numbers[key] == max_count:
        max_modal_elements.append(key)
        
mode = min(max_modal_elements)
    
#--------------------
# print the output
#--------------------

print("%.1f" % mean)
print("%.1f" % median)
print(mode)
