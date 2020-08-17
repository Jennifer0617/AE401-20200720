# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:39:08 2020

@author: 林玉鑫
"""


scores = []
total = 0
highest = 0
lowest = 100


n = input("班上有幾位同學?")
n = int(n)

for i in range(n):
    s = input("輸入成績:")
    s = int(s)
    scores.append(s)
    total = total+s
    
for j in range(n):
    if scores[j] > highest:
        highest = scores[j]
    if scores[j] < lowest:
        lowest = scores[j]
    
    
print(scores)
print("總分是",total)
print("平均分數是",total/n)
print("最高分數是",highest)
print("最低分數是",lowest)
        