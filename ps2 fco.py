# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:46:20 2025

@author: Saul
"""
from random import randint

n = 5

if n > 0:
    v = []
    for i in range(n):
        v.append(randint(1, 9))
    print("vector generado:", v)
else:
    print("error: el número debe ser entero y positivo.")