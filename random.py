# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:30:38 2020

@author: 林玉鑫
"""
import random
ans = random.randint(1,10)
i = 0

while i<5:
    n=input("猜一個數字")
    n=int(n)
    if ans < n :
       print("小一點")
    elif ans>n:
        print("大一點")
    else:
        print("猜對了")
        break
    i=i+1
       