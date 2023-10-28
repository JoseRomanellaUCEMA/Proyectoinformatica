from flask import Flask
from api_routes import get_autos, add_auto, get_auto, update_auto, delete_auto, get_ventas, add_venta, get_autos_by_make,get_ventas_by_make

app = Flask(__name__)

app.config['DATABASE'] = 'concesionaria.db'

app.add_url_rule('/autos', view_func=get_autos, methods=['GET'])
app.add_url_rule('/autos', view_func=add_auto, methods=['POST'])
app.add_url_rule('/autos/<vin>', view_func=get_auto, methods=['GET'])
app.add_url_rule('/autos/<vin>', view_func=update_auto, methods=['PUT'])
app.add_url_rule('/autos/<vin>', view_func=delete_auto, methods=['DELETE'])
app.add_url_rule('/autos/make', view_func=get_autos_by_make, methods=['GET'])
app.add_url_rule('/ventas', view_func=get_ventas, methods=['GET'])
app.add_url_rule('/ventas', view_func=add_venta, methods=['POST'])
app.add_url_rule('/ventas/make', view_func=get_ventas_by_make, methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True)

