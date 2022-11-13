from dependencies import unittest, date
from dependencies import donations, users
from classes.admin import Admin
from classes.donation import Donation


class ApproveDonationsTest(unittest.TestCase):
    def setUp(self):
        user = users.find_one({"email": "sahilkadam257@gmail.com"})
        user_id = user["_id"]
        medicine_name = "test_medicine"
        expiry_date = date(2023, 1, 2)
        quantity = 4
        collection_time = date(2022, 11, 12)
        test_donation = Donation(user_id, medicine_name,
                                 str(expiry_date), quantity, str(collection_time))
        self.donation_id = test_donation.donate_medicine()

    def tearDown(self):
        donations.delete_one({"_id": self.donation_id})

    def test(self):
        Admin.approve_donation(self.donation_id, "Approved")
        test_result = donations.find_one({"_id": self.donation_id})[
            'approval_status']
        self.assertEqual(test_result, "Approved")


if __name__ == "__main__":
    unittest.main()
