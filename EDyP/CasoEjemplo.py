import pandas as pnd

# Datos de ventas
datos = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Laptop"],
    "Cantidad": [2, 10, 5, 3, 1],
    "Precio": [15000, 300, 700, 4500, 15000]
}

ventas = pnd.DataFrame(datos)

# Calcular el total de cada venta
ventas["Total"] = ventas["Cantidad"] * ventas["Precio"]

print("Ventas:")
print(ventas)

# Total vendido
print("\nTotal de ventas:")
print(ventas["Total"].sum())

# Promedio de venta
print("\nPromedio de venta:")
print(ventas["Total"].mean())