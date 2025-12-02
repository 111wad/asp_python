hay_negativo = False
positivos = 0
negativos = 0
numero = -1.0 

while numero != 0:
    try:
        numero = float(input("Introduce un número (0 para terminar): "))
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        continue

    if numero != 0:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
            hay_negativo = True

print("--- Análisis de la Secuencia ---")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

if hay_negativo:
    print("Conclusión: SÍ se leyó al menos un número negativo.")
else:
    print("Conclusión: NO se leyó ningún número negativo.")