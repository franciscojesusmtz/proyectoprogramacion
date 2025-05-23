# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:31:48 2025

@author: Saul
"""

import random

def multiplos_fila(n):
    v = [random.randint(1, 9) for _ in range(n)]
    print("vector generado (fila):", v)
    m = []
    for i in range(n):
        fila = [v[j] * (i + 1) for j in range(n)]
        m.append(fila)
    for f in m:
        print(f)

def multiplos_columna(n):
    v = [random.randint(1, 9) for _ in range(n)]
    print("vector generado (columna):", v)
    m = []
    for i in range(n):
        columna = [v[i] * (j + 1) for j in range(n)]
        m.append(columna)
    for f in zip(*m):
        print(list(f))

n = 4

if n > 0:
    multiplos_fila(n)
    multiplos_columna(n)
else:
    print("error: el número debe ser entero y positivo.")
