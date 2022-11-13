from dependencies import donations, unittest, date, timedelta
from classes.admin import Admin
from classes.donation import Donation
from error_validation import check_quantity, check_dates

class test_backend_methods(unittest.TestCase):
	def setUp(self):
		self.dummy_donation = Donation(100, "Dummy_Med_Name", str(date.today()), 10, str(date.today()))
		self.dummy_donation.donate_medicine()

		# self.quantity = ""
		# self.expiry_date = date.today()
		# self.collection_time = date.today()

	def test_approve_donations(self):
		recent_donation = donations.find_one({"approval_status": "Pending", "medicine_name": "Dummy_Med_Name"})
		donation_id = recent_donation["_id"]
		Admin.approve_donation(donation_id, "Approved")
		test_result = donations.find_one({"_id": donation_id})['approval_status']
		self.assertEqual(test_result, "Approved")

	# def test_quantity(self):
	# 	#Test 1
	# 	test_result = check_quantity(self.quantity)
	# 	self.assertEqual(test_result, "Quantity is a required field!")

	# 	#Test 2
	# 	self.quantity = 0
	# 	test_result = check_quantity(self.quantity)
	# 	self.assertEqual(test_result, "Quantity must be greater than 0!")

	# 	#Test 3
	# 	self.quantity = -1
	# 	test_result = check_quantity(self.quantity)
	# 	self.assertEqual(test_result, "Quantity must be greater than 0!")
	
	# def test_dates(self):
	# 	#Test 1
	# 	test_result = check_dates(self.expiry_date, self.collection_time)
	# 	self.assertEqual(test_result, "Collection time and Expiry date must be past the current date")

	# 	#Test 2
	# 	self.expiry_date = self.expiry_date - timedelta(1)
	# 	self.collection_time = self.collection_time - timedelta(1)
	# 	test_result = check_dates(self.expiry_date, self.collection_time)
	# 	self.assertEqual(test_result, "Collection time and Expiry date must be past the current date")

	def tearDown(self):
		recent_donation = donations.find_one({"approval_status": "Approved", "medicine_name": "Dummy_Med_Name"})
		donation_id = recent_donation["_id"]
		donations.delete_one({"_id": donation_id})

		# self.quantity = ""
		# self.expiry_date = date.today()
		# self.collection_time = date.today()

if __name__ == "__main__":
	unittest.main()