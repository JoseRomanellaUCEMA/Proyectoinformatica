class Venta:
    def __init__(self, ID, VIN, date, price, make, buyer, price_ars) -> None:
        self.ID = ID
        self.VIN = VIN
        self.date = date
        self.price = price
        self.make = make
        self.buyer = buyer

    def serialize(self):
        return {
            'ID': self.ID,
            'VIN': self.VIN,
            'date': self.date,
            'price': self.price,
            'make': self.make,
            'buyer': self.buyer,
        }
