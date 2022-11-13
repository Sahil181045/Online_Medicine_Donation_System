from dependencies import date


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
    errors = set()
    if expiry_date <= collection_time:
        errors.add("Collection time must be prior to the expiry date")
    if collection_time <= date.today() or expiry_date <= date.today():
        errors.add(
            "Collection time and Expiry date must be past the current date")
    return errors
