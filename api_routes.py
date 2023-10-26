from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

app.config['DATABASE'] = 'concesionaria.db'

@app.route('/autos', methods=['GET', 'POST'])
def autos():
    if request.method == 'GET':
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM autos')
        autos = cursor.fetchall()
        conn.close()
        return jsonify(autos)
    elif request.method == 'POST':
        data = request.json

        if 'VIN' not in data or 'make' not in data or 'model' not in data or 'year' not in data or 'price' not in data or 'color' not in data or 'mileage' not in data or 'condition' not in data or 'features' not in data:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO autos (VIN, make, model, year, price, color, mileage, condition, features) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (data['VIN'], data['make'], data['model'], data['year'], data['price'], data['color'], data['mileage'], data['condition'], data['features']))
            conn.commit()
            conn.close()

            return jsonify({'message': 'Auto registrado exitosamente'})
        except sqlite3.IntegrityError:
            conn.close()
            return jsonify({'error': 'El VIN ya existe'}), 400

@app.route('/auto/<vin>', methods=['GET', 'PUT', 'DELETE'])
def auto(vin):
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM autos WHERE VIN = ?', (vin,))
        auto = cursor.fetchone()
        conn.close()
        if auto:
            return jsonify(auto)
        else:
            return jsonify({'error': 'Auto no encontrado'}), 404
    elif request.method == 'PUT':
        data = request.json

        if 'make' not in data or 'model' not in data or 'year' not in data or 'price' not in data or 'color' not in data or 'mileage' not in data or 'condition' not in data or 'features' not in data:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        cursor.execute('UPDATE autos SET make = ?, model = ?, year = ?, price = ?, color = ?, mileage = ?, condition = ?, features = ? WHERE VIN = ?',
                       (data['make'], data['model'], data['year'], data['price'], data['color'], data['mileage'], data['condition'], data['features'], vin))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Auto actualizado exitosamente'})
    elif request.method == 'DELETE':
        
        cursor.execute('DELETE FROM autos WHERE VIN = ?', (vin,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Auto eliminado exitosamente'})

@app.route('/ventas', methods=['GET', 'POST'])
def ventas():
    if request.method == 'GET':
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ventas')
        ventas = cursor.fetchall()
        conn.close()
        return jsonify(ventas)
    elif request.method == 'POST':
        data = request.json

        if 'VIN' not in data or 'date' not in data or 'price' not in data or 'buyer' not in data:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ventas (VIN, date, price, buyer) VALUES (?, ?, ?, ?)',
                       (data['VIN'], data['date'], data['price'], data['buyer']))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Venta registrada exitosamente'})

@app.route('/autos/make', methods=['GET'])
def autos_por_marca():
    marca = request.args.get('make')
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM autos WHERE make = ?', (marca,))
    autos = cursor.fetchall()
    conn.close()
    return jsonify(autos)