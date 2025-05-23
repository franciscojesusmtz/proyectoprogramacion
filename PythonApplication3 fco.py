def celsius_a_fahrenhit(celsius):
    fahrenhit = (celsius * 9/5) + 32
    return fahrenhit

def main():
    celsius = float(input("ingresa la temperatura en grados celsius: "))
    fahrenhit = celsius_a_fahrenhit(celsius)
    print("la temperatura en grados fahrenhit es: ", fahrenhit)
    
if __name__ == "__main__":
    main()
    
