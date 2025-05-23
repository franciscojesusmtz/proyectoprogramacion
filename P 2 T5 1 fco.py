# FRANCISCO JESUS MARTINEZ LOPEZ 
# -*- coding: utf-8 -*-

# Importamos las bibliotecas necesarias
import numpy as np
from sympy import symbols, integrate 

# Definimos las funciones a integrar
def f1(x): return 2*np.cos(2*x)
def f2(x): return -x**2 - x/2 + 4
def f3(x): return np.exp(-x**2)  

# Límites de integración para cada función
limites_a = [0, 0.5, 0]
limites_b = [np.pi/4, 1.5, 1]
lista_funciones = [f1, f2, f3]

# Método de Simpson 1/3 para integración numérica
def simpson_un_tercio(func, a, b):
    punto_medio = (a + b) / 2
    altura = b - a
    resultado = altura * (func(a) + 4*func(punto_medio) + func(b)) / 6
    return round(resultado, 4)

# Mostramos resultados analíticos
print('---------- Resultados Analíticos -----------')
variable = symbols('x')

for i, funcion in enumerate(lista_funciones):
    integral = integrate(funcion(variable), variable)
    print(f'Función {i+1}: Integral = {integral}')

# Mostramos resultados numéricos
print('\n******** Resultados Simpson 1/3 ***********')
for i in range(len(limites_a)):
    resultado = simpson_un_tercio(lista_funciones[i], limites_a[i], limites_b[i])
    print(f'Función {i+1}: Integral aproximada = {resultado}')