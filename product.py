class Auto:

    def __init__(self, VIN, make, model, year, price, color, mileage, condition, features, price_ars) -> None:
        self.VIN = VIN
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.color = color
        self.mileage = mileage
        self.condition = condition
        self.features = features
        self.price_ars = price_ars

    def serialize(self):
        return {
            'VIN': self.VIN,
            'make': self.make,
            'model': self.model,
            'year': self.year
        }

    def serialize_details(self):
        return {
            'VIN': self.VIN,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'price': self.price,
            'color': self.color,
            'mileage': self.mileage,
            'condition': self.condition,
            'features': self.features,
            'price_ars': self.price_ars
        }

