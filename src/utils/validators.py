'''validate_price(), validate_id(), validate_quantity()'''

#validators.py

from utils.exceptions import ValidationError

def validate_price(price):
    """Validate that the price is a positive float."""
    try:
        price = float(price)
        if price < 0:
            raise ValidationError("Price cannot be negative!")
        return price
    except ValueError:
        raise ValidationError("Price must be a number!")
    
def validate_id(item_id):
    """Validate that the ID is a positive integer."""
    try:
        item_id = int(item_id)
        if item_id <= 0:
            raise ValidationError("ID must be a positive integer!")
        return item_id
    except ValueError:
        raise ValidationError("ID must be an integer!")
    
def validate_quantity(quantity):
    """Validate that the quantity is a positive integer."""
    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValidationError("Quantity must be a positive integer!")
        return quantity
    except ValueError:
        raise ValidationError("Quantity must be an integer!")