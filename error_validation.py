from dependencies import date
def check_quantity(quantity):
	if quantity == "":
		return "Quantity is a required field!"
	elif not float(quantity).is_integer():
		return "Quantity must be an integer!"
	elif int(quantity) <= 0:
		return "Quantity must be greater than 0!"

def check_dates(expiry_date, collection_time):
	if expiry_date == "":
		return "Expiry date is a required field!"
	if collection_time == "":
		return "Collection time is a required field!"
	if expiry_date < collection_time:
		return "Collection time must be prior to the expiry date"
	if collection_time <= date.today() or expiry_date <= date.today():
		return "Collection time and Expiry date must be past the current date"