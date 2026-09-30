import numpy as npy

# Crear una matriz de 3 filas y 3 columnas
matriz = npy.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matriz:")
print(matriz)

# Acceder a un elemento
print("Elemento fila 1, columna 2:", matriz[0, 1])

# Obtener una fila
print("Primera fila:")
print(matriz[0])

# Obtener una columna
print("Primera columna:")
print(matriz[:, 0])

# Sumar todos los elementos
print("Suma total:", npy.sum(matriz))

# Promedio
print("Promedio:", npy.mean(matriz))