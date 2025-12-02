try:
    altura = int(input("Introduce la altura de la escalera: "))
except ValueError:
    print("Error: Debes introducir un número entero.")
    exit()

if altura <= 0:
    print("La altura debe ser un número positivo.")
else:
    for i in range(1, altura + 1):
        print("*" * i)