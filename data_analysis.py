import sqlite3
import csv

conn = sqlite3.connect('concesionaria.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM ventas')
ventas_data = cursor.fetchall()

conn.close()

nombre_archivo = 'ventas.csv'

with open(nombre_archivo, 'w', newline='') as archivo_csv:
    encabezados = ['VIN', 'date', 'price', 'make', 'buyer']
    writer = csv.DictWriter(archivo_csv, fieldnames=encabezados)
    writer.writeheader()
    for venta in ventas_data:
        writer.writerow({
            'VIN': venta[1], 
            'date': venta[2],
            'price': venta[3],
            'make': venta[4],
            'buyer': venta[5]
        })

print(f'Los datos se han exportado a {nombre_archivo}')
