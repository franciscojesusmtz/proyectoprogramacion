def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un numero valido.")
            
def calcular_promedio (num1, num2, num3, num4):
    return(num1 + num2 + num3 +num4) / 4

def main(): 
      try:
          print("por favor, ingrese cuatro numeros para calcular su promedio.")
          num1 = obtener_numero("ingrese el primer numero: ")
          num2 = obtener_numero("ingrese el primer numero: ")
          num3 = obtener_numero("ingrese el primer numero: ")
          num4 = obtener_numero("ingrese el primer numero: ")
          
          promedio = calcular_promedio(num1, num2, num3, num4)
          print("el promedio de los cuatro numeros es:" , promedio)

      except KeyboardInterrupt:
         print("\n programa interrumpido.")
      except EOFError:
         print("\nFin del archivo de entrada.")
      except exception as e:
         print("error:", e)

if __name__ == "__main__":
  main()    
