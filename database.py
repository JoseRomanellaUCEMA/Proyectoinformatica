import sqlite3

conn = sqlite3.connect('concesionaria.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS autos (
        VIN TEXT PRIMARY KEY,
        make TEXT,
        model TEXT,
        year INTEGER,
        price REAL,
        color TEXT,
        mileage REAL,
        condition TEXT,
        features TEXT,
        price_ars REAL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        ID INTEGER PRIMARY KEY,
        VIN TEXT,
        date TEXT,
        price REAL,
        make TEXT,
        buyer TEXT,
        price_ars REAL,
        FOREIGN KEY (VIN) REFERENCES autos (VIN)
    )
''')

conn.commit()

conn.close()
