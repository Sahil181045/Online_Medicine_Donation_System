from dependencies import date
<<<<<<< HEAD
=======


>>>>>>> 97ef3b7f56cc58bc50f964c085d3d3e85930c19e
def check_quantity(quantity):
    errors = set()
    if quantity == "":
        errors.add("Quantity is a required field!")
        return errors
    quantity = float(quantity)
    if not quantity.is_integer():
        errors.add("Quantity must be an integer!")
    if int(quantity) <= 0:
        errors.add("Quantity must be greater than 0!")
    return errors


def check_dates(expiry_date, collection_time):
<<<<<<< HEAD
	if expiry_date == "":
		return "Expiry date is a required field!"
	if collection_time == "":
		return "Collection time is a required field!"
	if expiry_date < collection_time:
		return "Collection time must be prior to the expiry date"
	if collection_time <= date.today() or expiry_date <= date.today():
		return "Collection time and Expiry date must be past the current date"
=======
    errors = set()
    if expiry_date <= collection_time:
        errors.add("Collection time must be prior to the expiry date")
    if collection_time <= date.today() or expiry_date <= date.today():
        errors.add(
            "Collection time and Expiry date must be past the current date")
    return errors
>>>>>>> 97ef3b7f56cc58bc50f964c085d3d3e85930c19e
