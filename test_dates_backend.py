from error_validation import check_quantity, check_dates
from dependencies import unittest, date, timedelta

class test_backend_methods(unittest.TestCase):
	def setUp(self):
		self.quantity = ""
		self.expiry_date = date.today()
		self.collection_time = date.today()

	def test_quantity(self):
		#Test 1
		test_result = check_quantity(self.quantity)
		self.assertEqual(test_result, "Quantity is a required field!")

		#Test 2
		self.quantity = 0
		test_result = check_quantity(self.quantity)
		self.assertEqual(test_result, "Quantity must be greater than 0!")

		#Test 3
		self.quantity = -1
		test_result = check_quantity(self.quantity)
		self.assertEqual(test_result, "Quantity must be greater than 0!")
	
	def test_dates(self):
		#Test 1
		test_result = check_dates(self.expiry_date, self.collection_time)
		self.assertEqual(test_result, "Collection time and Expiry date must be past the current date")

		#Test 2
		self.expiry_date = self.expiry_date - timedelta(1)
		self.collection_time = self.collection_time - timedelta(1)
		test_result = check_dates(self.expiry_date, self.collection_time)
		self.assertEqual(test_result, "Collection time and Expiry date must be past the current date")

	def tearDown(self):
		self.quantity = ""
		self.expiry_date = date.today()
		self.collection_time = date.today()

if __name__ == "__main__":
	unittest.main()