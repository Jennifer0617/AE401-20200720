# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:26:14 2020

@author: 林玉鑫
"""


scores = []
total = 0
avg=0

n = input("班上有幾位同學?")
n = int(n)

for i in range(n):
   name=input("請輸入名字:")
   scores.append(name)


   score = input("輸入同學成績:") 
   score = int(score)
   scores.append(score)
   
for item in range(1,n*2,2):
    total = total+scores[item]

print ("平均分",(total/n))
    
highest = 0
for i in range(1,n*2,2):
    if scores[i] > highest:
        highest = scores[i]
        highestname = scores[i-1]
        
lowest = 100
for i in range(1,n*2,2):
    if scores[i] < lowest:
        lowest = scores[i]
        lowestname = scores[i-1]
        
print (highestname,"最高分",highest)
print (lowestname,"最低分",lowest)
print 