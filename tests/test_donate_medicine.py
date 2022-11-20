from dependencies import unittest, date
from dependencies import users, donations
from classes.donation import Donation


class DonationTest(unittest.TestCase):
	def setUp(self):
		user = users.find_one({"email": "sahilkadam257@gmail.com"})
		self.user_id = user["_id"]
		self.medicine_name = "test_medicine"
		self.expiry_date = date(2023, 1, 2)
		self.quantity = 4
		self.collection_time = date(2022, 11, 12)

	def test(self):
		test_donation = Donation(self.user_id, self.medicine_name,
								 str(self.expiry_date), self.quantity, str(self.collection_time))
		self.donation_id = test_donation.donate_medicine()
		donations_list = list(donations.find())
		last_donation = donations_list[len(donations_list)-1]

		self.assertEqual(self.user_id, last_donation["user_id"])
		self.assertEqual(self.medicine_name, last_donation["medicine_name"])
		self.assertEqual(str(self.expiry_date), last_donation["expiry_date"])
		self.assertEqual(self.quantity, last_donation["quantity"])
		self.assertEqual(str(self.collection_time),last_donation["collection_time"])

	def tearDown(self):
		donations.delete_one({"_id": self.donation_id})


if __name__ == "__main__":
	unittest.main()
