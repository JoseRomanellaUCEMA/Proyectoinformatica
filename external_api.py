import sqlite3
import requests

conn = sqlite3.connect('concesionaria.db')
cursor = conn.cursor()

def get_exchange_rate(base_currency, target_currency):
    api_key = 'be0c6e0c81b77a2836587494'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}' 
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['conversion_rates'].get(target_currency)
        return exchange_rate
    else:
        return None

exchange_rate_ars = get_exchange_rate('USD', 'ARS')

if exchange_rate_ars is not None:
    cursor.execute('UPDATE ventas SET price_ars = price * ?', (exchange_rate_ars,))
    cursor.execute('UPDATE autos SET price_ars = price * ?', (exchange_rate_ars,))
    conn.commit()
    print('Precios en ARS actualizados con éxito.')
else:
    print('Error al obtener la tasa de cambio para ARS.')

conn.close()



