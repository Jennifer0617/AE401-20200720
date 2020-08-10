# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:36:05 2020

@author: 林玉鑫
"""


import random 

ans = random.randint(1,20)
time=0
while time<5:

    guess = input("請輸入一個數字")
    guess=int(guess)
    
    if guess>ans:
        if time==4:
            print("你已經猜五次了")
        else:
            print("猜小一點")
        time=time+1
    elif guess<ans:
        if time==4:
            print("你猜五次了!!")
        else:
            print("猜大一點")
            time=time+1
    else:
        print("答對了")
        time=time+1
        print("總共猜了"+str(time)+"猜對的")
        break