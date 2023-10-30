from flask import Flask, request, jsonify
from product import Auto
from sale import Venta
import sqlite3

app = Flask(__name__)

app.config['DATABASE'] = 'concesionaria.db'

@app.route('/autos', methods=['GET'])
def get_autos():
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM autos')
    autos_data = cursor.fetchall()
    conn.close()
    
    autos = []
    for auto_data in autos_data:
        auto = Auto(*auto_data)
        autos.append(auto.serialize_details())
    
    return jsonify(autos)

@app.route('/autos', methods=['POST'])
def add_auto():
    data = request.json

    if 'VIN' not in data or 'make' not in data or 'model' not in data or 'year' not in data or 'price' not in data or 'color' not in data or 'mileage' not in data or 'condition' not in data or 'features' not in data:
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    auto = Auto(data['VIN'], data['make'], data['model'], data['year'], data['price'], data['color'], data['mileage'], data['condition'], data['features'])

    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO autos (VIN, make, model, year, price, color, mileage, condition, features) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (auto.VIN, auto.make, auto.model, auto.year, auto.price, auto.color, auto.mileage, auto.condition, auto.features))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Auto registrado exitosamente'})
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({'error': 'El VIN ya existe'}), 400

@app.route('/autos/<vin>', methods=['GET'])
def get_auto(vin):
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM autos WHERE VIN = ?', (vin,))
    auto_data = cursor.fetchone()
    conn.close()
    
    if auto_data:
        auto = Auto(*auto_data)
        return jsonify(auto.serialize_details())
    else:
        return jsonify({'error': 'Auto no encontrado'}), 404

@app.route('/autos/<vin>', methods=['PUT'])
def update_auto(vin):
    data = request.json

    if 'make' not in data or 'model' not in data or 'year' not in data or 'price' not in data or 'color' not in data or 'mileage' not in data or 'condition' not in data or 'features' not in data:
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    auto = Auto(vin, data['make'], data['model'], data['year'], data['price'], data['color'], data['mileage'], data['condition'], data['features'])

    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('UPDATE autos SET make = ?, model = ?, year = ?, price = ?, color = ?, mileage = ?, condition = ?, features = ? WHERE VIN = ?',
                   (auto.make, auto.model, auto.year, auto.price, auto.color, auto.mileage, auto.condition, auto.features, vin))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Auto actualizado exitosamente'})

@app.route('/autos/<vin>', methods=['DELETE'])
def delete_auto(vin):
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('DELETE FROM autos WHERE VIN = ?', (vin,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Auto eliminado exitosamente'})

@app.route('/autos/make', methods=['GET'])
def get_autos_by_make():
    marca = request.args.get('make')
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM autos WHERE make = ?', (marca,))
    autos_data = cursor.fetchall()
    conn.close()
    
    autos = []
    for auto_data in autos_data:
        auto = Auto(*auto_data)
        autos.append(auto.serialize_details())
    
    if not autos:
        return jsonify({'error': 'No se encontraron autos de la marca especificada'}), 404
    return jsonify(autos)

@app.route('/ventas', methods=['GET'])
def get_ventas():
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ventas')
    ventas_data = cursor.fetchall()
    conn.close()
    
    ventas = []
    for venta_data in ventas_data:
        venta = Venta(*venta_data)
        ventas.append(venta.serialize())
    
    return jsonify(ventas)

@app.route('/ventas', methods=['POST'])
def add_venta():
    data = request.json

    if 'VIN' not in data or 'date' not in data or 'price' not in data or 'make' not in data or 'buyer' not in data:
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    venta = Venta(None, data['VIN'], data['date'], data['price'], data['make'], data['buyer'])

    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ventas (VIN, date, price, make, buyer) VALUES (?, ?, ?, ?, ?)',
                   (venta.VIN, venta.date, venta.price, venta.make, venta.buyer))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Venta registrada exitosamente'})

@app.route('/ventas/make', methods=['GET'])
def get_ventas_by_make():
    marca = request.args.get('make')
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ventas WHERE make = ?', (marca,))
    ventas_data = cursor.fetchall()
    conn.close()
    
    ventas = []
    for venta_data in ventas_data:
        venta = Venta(*venta_data)
        ventas.append(venta.serialize())
    
    if not ventas:
        return jsonify({'error': 'No se encontraron ventas de autos de la marca especificada'}), 404
    return jsonify(ventas)

if __name__ == '__main__':
    app.run(debug=True)

