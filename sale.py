class Venta:
    def __init__(self, ID, VIN, date, price, buyer) -> None:
        self.ID = ID
        self.VIN = VIN
        self.date = date
        self.price = price
        self.buyer = buyer

    def serialize(self):
        return {
            'ID': self.ID,
            'VIN': self.VIN,
            'date': self.date,
            'price': self.price,
            'buyer': self.buyer
        }
