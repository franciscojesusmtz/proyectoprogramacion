# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:48:46 2025

@author: Saul
"""
n = -3

try:
    n = int(n)
    if n > 0:
        print("el número es entero y positivo.")
    else:
        print("error: el número debe ser positivo.")
except:
    print("error: debes ingresar un número entero.")

