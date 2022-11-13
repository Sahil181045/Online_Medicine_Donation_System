from dependencies import unittest
from error_validation import check_quantity


class QuantityValidator(unittest.TestCase):
    def test_1(self):
        quantity = ""
        test_result = check_quantity(quantity)
        expected_errors = {"Quantity is a required field!"}
        self.assertEqual(test_result, expected_errors)

    def test_2(self):
        quantity = "0"
        test_result = check_quantity(quantity)
        expected_errors = {"Quantity must be greater than 0!"}
        self.assertEqual(test_result, expected_errors)

    def test_3(self):
        quantity = "-1"
        test_result = check_quantity(quantity)
        expected_errors = {"Quantity must be greater than 0!"}
        self.assertEqual(test_result, expected_errors)

    def test_4(self):
        quantity = "2.5"
        test_result = check_quantity(quantity)
        expected_errors = {"Quantity must be an integer!"}
        self.assertEqual(test_result, expected_errors)

    def test_5(self):
        quantity = "-2.5"
        test_result = check_quantity(quantity)
        expected_errors = {
            "Quantity must be an integer!",
            "Quantity must be greater than 0!"
        }
        self.assertEqual(test_result, expected_errors)

    def test_6(self):
        quantity = "5.0"
        test_result = check_quantity(quantity)
        expected_errors = set()
        self.assertEqual(test_result, expected_errors)


if __name__ == "__main__":
    unittest.main()
