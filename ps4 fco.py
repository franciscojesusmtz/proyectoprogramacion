# -*- coding: utf-8 -*-
"""
Created on Thu Fri  7 22:42:10 2025

@author: Saul
"""

import random

n = 5

if n > 0:
    v = [random.randint(1, 9) for _ in range(n)]
    print("vector generado:", v)
    m = []
    for i in range(n):
        columna = []
        for j in range(n):
            columna.append(v[i] * (j + 1))
        m.append(columna)
    for f in zip(*m):
        print(list(f))
else:
    print("error: el número debe ser entero y positivo.")
