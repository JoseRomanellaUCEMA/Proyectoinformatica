from flask import Flask

app = Flask(__name__)

app.config['DATABASE'] = 'concesionaria.db'

from api_routes import autos, auto, ventas, autos_por_marca

app.add_url_rule('/autos', view_func=autos)
app.add_url_rule('/auto/<vin>', view_func=auto)
app.add_url_rule('/autos/make',view_func=autos_por_marca)
app.add_url_rule('/ventas', view_func=ventas)

if __name__ == '__main__':
    app.run(debug=True)
