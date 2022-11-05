from ..dependencies import users


class Client:
    def __init__(self, email, password, first_name=None, last_name=None, phone=None, address=None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.password = password

    def register(self):
        user = users.find_one({"email": self.email})
        if user:
            return "already_exists"
        document = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "password": self.password
        }
        users.insert_one(document)
        return "success"

    def authenticate(self):
        user = users.find_one({"email": self.email})
        if not user:
            return "no_user"
        if user["password"] == self.password:
            return "success"
        else:
            return "failure"
