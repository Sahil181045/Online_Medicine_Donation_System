from dependencies import medicines


class Medicine:
    def __init__(self, medicine_name, expiry_date, quantity) -> None:
        self.medicine_name = medicine_name
        self.expiry_date = expiry_date
        self.quantity = quantity

    def add_medicine(self):
        document = {
            "medicine_name": self.medicine_name,
            "expiry_date": self.expiry_date,
            "quantity": self.quantity
        }
        medicines.insert_one(document)
