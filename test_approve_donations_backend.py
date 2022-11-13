from dependencies import donations, medicines, unittest, date
from classes.admin import Admin
from classes.donation import Donation


class test_backend_methods(unittest.TestCase):
	def setUp(self):
		self.dummy_donation = Donation(100, "Dummy_Med_Name", str(date.today()), 10, str(date.today()))
		self.dummy_donation.donate_medicine()

	def test_approve_donations(self):
		recent_donation = donations.find_one({"approval_status": "Pending", "medicine_name": "Dummy_Med_Name"})
		donation_id = recent_donation["_id"]
		Admin.approve_donation(donation_id, "Approved")
		test_result = donations.find_one({"_id": donation_id})['approval_status']
		self.assertEqual(test_result, "Approved")

	def tearDown(self):
		recent_donation = donations.find_one({"approval_status": "Approved", "medicine_name": "Dummy_Med_Name"})
		donation_id = recent_donation["_id"]
		donations.delete_one({"_id": donation_id})

		recent_donation = medicines.find_one({"medicine_name": "Dummy_Med_Name"})
		donation_id = recent_donation["_id"]
		medicines.delete_one({"_id": donation_id})

if __name__ == "__main__":
	unittest.main()