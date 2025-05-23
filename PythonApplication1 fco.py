FRANCISCO JESUS MARTINEZ LOPEZ
from lib2to3.pytree import Base


def calcular_perimetro(Base, altura):
    return 2 * (Base + altura)

def calcular_area(base, altura):
    return base * altura

def  obtener_numero(mensaje):

  while True:
    try:
        return float(input(mensaje))
    except ValueError:
        def main():
           (Base: float = obtener_numero("ingrrese la base del rectangulo: ")
    altura = obtener_numero("ingrese la altura del rectangulo: ")

perimetro = calcular_perimetro (Base:Any, altura:Any)
area = calcular_area (Base:, altura:Any)

print("el perimtro del rectangulo es: ", perimetro)
print("el area del rectangulo es: ", area)

if __name__ == "__main__":
    main:()
    