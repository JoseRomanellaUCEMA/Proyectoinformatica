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
        features TEXT
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
        FOREIGN KEY (VIN) REFERENCES autos (VIN)
    )
''')

conn.commit()

conn.close()
