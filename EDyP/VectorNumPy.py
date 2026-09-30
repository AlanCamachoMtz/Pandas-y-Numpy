import numpy as npy

# Crear un vector
numeros = npy.array([10, 20, 30, 40, 50])

print("Vector:")
print(numeros)

# Acceder a un elemento
print("Primer elemento:", numeros[0])

# Suma
print("Suma:", npy.sum(numeros))

# Promedio
print("Promedio:", npy.mean(numeros))

# Máximo
print("Máximo:", npy.max(numeros))

# Mínimo
print("Mínimo:", npy.min(numeros))
