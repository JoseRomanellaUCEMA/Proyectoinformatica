import requests
import sqlite3
from external_api import get_exchange_rate

while True:
    print("1. Ver autos")
    print("2. Agregar auto")
    print("3. Ver detalles de un auto por VIN")
    print("4. Actualizar información de un auto por VIN")
    print("5. Eliminar un auto por VIN")
    print("6. Ver autos por marca")
    print("7. Ver ventas")
    print("8. Agregar venta")
    print("9. Ver ventas por marca")
    print("10. Actualizar precios en ARS")
    print("0. Salir")

    choice = input("Ingresa el número de la opción que deseas: ")

    if choice == "1":
        autos_response = requests.get('http://127.0.0.1:5000/autos')
        autos = autos_response.json()
        for auto in autos:
            print(auto)
    elif choice == "2":
        vin = input("Ingresa el VIN del auto: ")
        make = input("Ingresa la marca del auto: ")
        model = input("Ingresa el modelo del auto: ")
        year = input("Ingresa el año del auto: ")
        price = input("Ingresa el precio del auto: ")
        color = input("Ingresa el color del auto: ")
        mileage = input("Ingresa el kilometraje del auto: ")
        condition = input("Ingresa la condición del auto: ")
        features = input("Ingresa las características del auto: ")
        price_ars = input("Ingresa el precio en ARS del auto: ")

        data = {
            'VIN': vin,
            'make': make,
            'model': model,
            'year': year,
            'price': price,
            'color': color,
            'mileage': mileage,
            'condition': condition,
            'features': features,
            'price_ars': price_ars
        }
        
        response = requests.post('http://127.0.0.1:5000/autos', json=data)
        print(response.json())
    elif choice == "3":
        vin = input("Ingresa el VIN del auto: ")
        auto_response = requests.get(f'http://127.0.0.1:5000/autos/{vin}')
        auto = auto_response.json()
        print(auto)
    elif choice == "4":
        vin = input("Ingresa el VIN del auto a actualizar: ")
        make = input("Ingresa la nueva marca del auto: ")
        model = input("Ingresa el nuevo modelo del auto: ")
        year = input("Ingresa el nuevo año del auto: ")
        price = input("Ingresa el nuevo precio del auto: ")
        color = input("Ingresa el nuevo color del auto: ")
        mileage = input("Ingresa el nuevo kilometraje del auto: ")
        condition = input("Ingresa la nueva condición del auto: ")
        features = input("Ingresa las nuevas características del auto: ")
        price_ars = input("Ingresa el nuevo precio en ARS del auto: ")

        data = {
            'make': make,
            'model': model,
            'year': year,
            'price': price,
            'color': color,
            'mileage': mileage,
            'condition': condition,
            'features': features,
            'price_ars': price_ars
        }

        response = requests.put(f'http://127.0.0.1:5000/autos/{vin}', json=data)
        print(response.json())
    elif choice == "5":
        vin = input("Ingresa el VIN del auto a eliminar: ")
        response = requests.delete(f'http://127.0.0.1:5000/autos/{vin}')
        print(response.json())
    elif choice == "6":
        make = input("Ingresa la marca de los autos a buscar: ")
        autos_response = requests.get(f'http://127.0.0.1:5000/autos/make?make={make}')
        autos = autos_response.json()
        for auto in autos:
            print(auto)
    elif choice == "7":
        ventas_response = requests.get('http://127.0.0.1:5000/ventas')
        ventas = ventas_response.json()
        for venta in ventas:
            print(venta)
    elif choice == "8":
        vin = input("Ingresa el VIN del auto vendido: ")
        date = input("Ingresa la fecha de la venta: ")
        price = input("Ingresa el precio de la venta: ")
        make = input("Ingresa la marca del auto vendido: ")
        buyer = input("Ingresa el comprador: ")

        data = {
            'VIN': vin,
            'date': date,
            'price': price,
            'make': make,
            'buyer': buyer
        }

        response = requests.post('http://127.0.0.1:5000/ventas', json=data)
        print(response.json())
    elif choice == "9":
        make = input("Ingresa la marca de las ventas a buscar: ")
        ventas_response = requests.get(f'http://127.0.0.1:5000/ventas/make?make={make}')
        ventas = ventas_response.json()
        for venta in ventas:
            print(venta)
    elif choice == "10":

        conn = sqlite3.connect('concesionaria.db')
        cursor = conn.cursor()
        exchange_rate_ars = get_exchange_rate('USD', 'ARS')
        if exchange_rate_ars is not None:
            cursor.execute('UPDATE ventas SET price_ars = price * ?', (exchange_rate_ars,))
            cursor.execute('UPDATE autos SET price_ars = price * ?', (exchange_rate_ars,))
            conn.commit()
            print('Precios en ARS actualizados con éxito.')
        else:
            print('Error al obtener la tasa de cambio para ARS.')
    elif choice == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
