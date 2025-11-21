precio = float(input("Introduce el precio del producto: "))

precioReal=float(input("Introduce el precio con descuento: "))


descuento = ((precio - precioReal) / precio) * 100

print(f"El porcentaje de descuento es: {descuento:.2f}%")