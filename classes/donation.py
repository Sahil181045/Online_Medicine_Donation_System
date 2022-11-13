from dependencies import donations


class Donation:
    def __init__(self, user_id, medicine_name, expiry_date, quantity, collection_time) -> None:
        self.user_id = user_id
        self.medicine_name = medicine_name
        self.expiry_date = expiry_date
        self.quantity = quantity
        self.collection_time = collection_time

    def donate_medicine(self):
        document = {
            "user_id": self.user_id,
            "medicine_name": self.medicine_name,
            "expiry_date": self.expiry_date,
            "quantity": self.quantity,
            "collection_time": self.collection_time,
            "approval_status": "Pending"
        }
        return donations.insert_one(document).inserted_id
