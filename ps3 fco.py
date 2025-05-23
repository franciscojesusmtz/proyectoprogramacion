# -*- coding: utf-8 -*-
"""
Created on Fri Feb 7  20:51:51 2025

@author: FRANCISCO JESUS MARTINEZ LOPEZ
"""

import random

n = 6

if n > 0:
    v = [random.randint(1, 9) for _ in range(n)]
    print("vector generado:", v)
    m = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(v[j] * (i + 1))
        m.append(fila)
    for f in m:
        print(f)
else:
    print("error: el número debe ser entero y positivo.")
