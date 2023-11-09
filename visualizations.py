import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('ventas.csv')

df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])

df = df.sort_values('date')

plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['price'], marker='o', linestyle='-', color='b')
plt.title('Ventas en Relación a la Fecha')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.grid(True)
plt.show()

sales_by_make = df['make'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(sales_by_make, labels=sales_by_make.index, autopct='%1.1f%%', startangle=140)
plt.title('Cantidad de Ventas por Marca de Auto')
plt.show()