from ..dependencies import donations
from ..classes.client import *
from ..classes.medicine import *


class Admin(Client):
    @staticmethod
    def approve_donation(donation_id, approval_response):
        search_query = {"_id": donation_id}
        update_query = {"$set": {"is_approved": approval_response}}
        donations.update_one(search_query, update_query)

        if approval_response == True:

            donation = donations.find_one(search_query)
            medicine_name = donation["medicine_name"]
            expiry_date = donation["expiry_date"]
            quantity = donation["quantity"]

            medicine = Medicine(medicine_name, expiry_date, quantity)
            medicine.add_medicine()
