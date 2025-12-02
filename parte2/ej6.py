try:
    N = int(input("Introduce un número entero positivo N para calcular su factorial: "))
except ValueError:
    print("Error: La entrada debe ser un número entero.")
    exit()

if N < 0:
    print("El factorial solo está definido para números positivos o cero.")
elif N == 0:
    print(f"El factorial de {N}! es: 1")
else:
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i

    print(f"El factorial de {N}! es: {factorial}")