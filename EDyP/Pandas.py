import pandas as pnd

# Crear un DataFrame
datos = {
    "Nombre": ["Alan", "Carlos", "Diego", "Axel"],
    "Edad": [20, 22, 19, 21],
    "Calificacion": [90, 85, 95, 88]
}

df = pnd.DataFrame(datos)

print("DataFrame:")
print(df)

# Mostrar una columna
print("\nCalificaciones:")
print(df["Calificacion"])

# Calificación promedio
print("\nPromedio:")
print(df["Calificacion"].mean())

# Calificación máxima
print("\nCalificación máxima:")
print(df["Calificacion"].max())

# Filtrar estudiantes con calificación mayor a 90
print("\nEstudiantes con más de 90:")
print(df[df["Calificacion"] > 90])