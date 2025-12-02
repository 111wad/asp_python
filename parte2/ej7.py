# Inicializamos una bandera que estará en False por defecto
hay_negativo = False

# Usamos un bucle for para repetir el proceso 100 veces
for _ in range(100):
    # Solicitamos el número
    try:
        numero = float(input("Introduce un número no nulo (quedan por introducir): "))
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        # Se puede añadir una lógica para reintentar o simplemente ignorar esta iteración
        continue

    # Verificamos si el número es negativo y actualizamos la bandera
    if numero < 0:
        hay_negativo = True

    # Opcional: Si ya encontramos un negativo, podríamos salir del bucle (optimización)
    # if hay_negativo:
    #     break

# Mostramos el resultado al final de las 100 iteraciones
print("--- Resultado ---")
if hay_negativo:
    print("SÍ se ha leído al menos un número negativo.")
else:
    print("NO se ha leído ningún número negativo.")