try:
    altura = int(input("Introduce la altura de la escalera (número entero positivo): "))
except ValueError:
    print("Error: Debes introducir un número entero.")
    exit()

if altura <= 0:
    print("La altura debe ser un número positivo.")
else:
    for i in range(1, altura + 1):
        linea = ""
        # Bucle interno para construir la secuencia de 1 hasta el número de la línea (i)
        for j in range(1, i + 1):
            linea += str(j)
        
        print(linea)