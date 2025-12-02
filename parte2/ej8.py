positivos = 0
negativos = 0

for _ in range(100):
    try:
        numero = float(input(f"Introduce un número no nulo: "))
        
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        continue

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("--- Recuento Final ---")
print(f"Números positivos leídos: {positivos}")
print(f"Números negativos leídos: {negativos}")