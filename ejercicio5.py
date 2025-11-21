

import math

radioLong=float(input("Introduce la longitud de un radio: "))

diametro = 2 * radioLong


long_circunferencia = math.pi * diametro

area_circulo = math.pi * radioLong**2


volumen_esfera = (4/3) * math.pi * radioLong**3

print(f"Longitud de la circunferencia: {long_circunferencia:.2f}")
print(f"Área del círculo: {area_circulo:.2f}")
print(f"Volumen de la esfera: {volumen_esfera:.2f}")