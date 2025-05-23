# FRANCISCO JESUS MARTINEZ LOPEZ
# Importamos la función derivative de scipy
from scipy.misc import derivative

# Definimos la función a derivar
def funcion_ejemplo(x): 
    return -x**2 - x/2 + 4

# Valores de h para las derivadas
pasos_h = [0.2, 0.1]
punto = 0

# Función para derivada hacia adelante
def derivada_adelante(func, x, h):
    fx_h = func(x + h)
    fx_2h = func(x + 2*h)
    return (-fx_2h + 4*fx_h - 3*func(x)) / (2*h)

# Función para derivada hacia atrás
def derivada_atras(func, x, h):
    fx_h = func(x - h)
    fx_2h = func(x - 2*h)
    return (3*func(x) - 4*fx_h + fx_2h) / (2*h)

# Función para derivada centrada
def derivada_centrada(func, x, h):
    fx_h = func(x + h)
    fx_2h = func(x + 2*h)
    fx_menosh = func(x - h)
    fx_menos2h = func(x - 2*h)
    return (-fx_2h + 8*fx_h - 8*fx_menosh + fx_menos2h) / (12*h)

# Mostramos resultados analíticos
print('*********** Resultados Analíticos **************\n')
for h_valor in pasos_h:
    deriv = derivative(funcion_ejemplo, punto, dx=h_valor)
    print(f'Con h = {h_valor}: Derivada analítica = {deriv}')

# Mostramos resultados numéricos
print('\n*********** Resultados Numéricos **************')
for h_valor in pasos_h:
    print(f'\nPara h = {h_valor}:')
    adelante = derivada_adelante(funcion_ejemplo, punto, h_valor)
    atras = derivada_atras(funcion_ejemplo, punto, h_valor)
    centrada = derivada_centrada(funcion_ejemplo, punto, h_valor)
    
    print(f'  Derivada hacia adelante: {adelante}')
    print(f'  Derivada hacia atrás: {atras}')
    print(f'  Derivada centrada: {centrada}')