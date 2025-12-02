try:
    altura = int(input("Introduce la altura de la pirámide invertida (número entero positivo): "))
except ValueError:
    print("Error: Debes introducir un número entero.")
    exit()

if altura <= 0:
    print("La altura debe ser un número positivo.")
else:
    for i in range(altura, 0, -1):

        espacios = " " * (altura - i)
        
        asteriscos = "*" * (2 * i - 1)
        
        print(espacios + asteriscos)