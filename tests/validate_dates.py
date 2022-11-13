from dependencies import unittest, date
from error_validation import check_dates


class DatesValidator(unittest.TestCase):
    def test_1(self):
        expiry_date = date.today()
        collection_time = date.today()
        test_result = check_dates(expiry_date, collection_time)
        expected_errors = {
            "Collection time and Expiry date must be past the current date",
            "Collection time must be prior to the expiry date"
        }
        self.assertEqual(test_result, expected_errors)

    def test_2(self):
        expiry_date = date(2023, 11, 9)
        collection_time = date(2023, 11, 12)
        test_result = check_dates(expiry_date, collection_time)
        expected_errors = {
            "Collection time must be prior to the expiry date"
        }
        self.assertEqual(test_result, expected_errors)

    def test_3(self):
        expiry_date = date(1999, 11, 12)
        collection_time = date.today()
        test_result = check_dates(expiry_date, collection_time)
        expected_errors = {
            "Collection time and Expiry date must be past the current date",
            "Collection time must be prior to the expiry date"
        }
        self.assertEqual(test_result, expected_errors)

    def test_4(self):
        expiry_date = date(2023, 1, 2)
        collection_time = date(2022, 12, 20)
        test_result = check_dates(expiry_date, collection_time)
        expected_errors = set()
        self.assertEqual(test_result, expected_errors)


if __name__ == "__main__":
    unittest.main()
