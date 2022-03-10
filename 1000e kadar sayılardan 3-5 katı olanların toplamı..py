# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:14:58 2022

@author: PC
"""
sum = 0
for i in range(1000):
	if i % 3 == 0 or i % 5 == 0:
                        sum+= i
        
print(sum)