# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:30:38 2020

@author: 林玉鑫
"""
import random
ans = random.randint(1,10)
n=input("猜一個數字")
n=int(n)
if ans == n:
   print("你很棒")
else:
   print("你加油 答案是",ans)