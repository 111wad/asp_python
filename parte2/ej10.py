suma = 0

producto = 1


for i in range(1, 11):
    suma += i
    producto *= i

print(f"Los 10 primeros números naturales son: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
print(f"La suma es: {suma}")
print(f"El producto (10!) es: {producto}")