# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:11:06 2020

@author: Acer
"""

a=[1,2,-3,3.15,355,-2.5]
n=1
import math
for b in a:
    print("giá trị của phần tử thứ ",n,"=",b)
    n+=1
    if b>0:
        print('logarit tự nhiên của phần tử thứ ',n,'=',math.log(b))
    else :
        print("không có logarit tự nhiên của phần tử thứ ",n)