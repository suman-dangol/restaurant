from src.utils.exceptions import ValidationError
import re  # Import the regular expression module

def validate_id(item_id):
    """Validates if an ID is a positive integer."""
    try:
        item_id = int(item_id)
        if item_id <= 0:
            raise ValidationError("ID must be a positive integer.", details={"value": item_id})
        return item_id
    except ValueError:
        raise ValidationError("Invalid ID format. Must be a positive integer.", details={"value": item_id})
    except TypeError:
        raise ValidationError("ID must not be None.", details={"value": item_id})

def validate_price(price):
    """Validates if a price is a non-negative float."""
    try:
        price = float(price)
        if price < 0:
            raise ValidationError("Price cannot be negative.", details={"value": price})
        if price > 10000:
            raise ValidationError("Price cannot be that high.", details={"value": price})
        return price
    except ValueError:
        raise ValidationError("Invalid price format. Must be a non-negative number.", details={"value": price})
    except TypeError:
        raise ValidationError("Price must not be None.", details={"value": price})

def validate_quantity(quantity):
    """Validates if a quantity is a positive integer."""
    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValidationError("Quantity must be a positive integer.", details={"value": quantity})
        if quantity > 1000:
             raise ValidationError("Quantity cannot be that high.", details={"value": quantity})
        return quantity
    except ValueError:
        raise ValidationError("Invalid quantity format. Must be a positive integer.", details={"value": quantity})
    except TypeError:
        raise ValidationError("Quantity must not be None.", details={"value": quantity})

def validate_string(value):
    """Validates if a value is a non-empty string."""
    if value is None:
        raise ValidationError("String value must not be None.")
    if not isinstance(value, str):
        raise ValidationError("Value must be a string.", details={"value": value})
    value = value.strip()
    if not value:
        raise ValidationError("Value must be a non-empty string.")
    return value

def validate_category(category):
    """Validates if a category is a valid menu category."""
    valid_categories = ["Starter", "Main", "Dessert", "Beverage"]
    if category not in valid_categories:
        raise ValidationError(f"Invalid category. Must be one of: {', '.join(valid_categories)}", details={"value": category})
    return category

def validate_username(username):
    """Validates if a username is valid (alphanumeric and between 3 and 20 characters)."""
    username = validate_string(username)  # Ensure it's a non-empty string first
    if not re.match("^[a-zA-Z0-9]{3,20}$", username):
        raise ValidationError("Invalid username format. Must be alphanumeric and 3-20 characters long.", details={"value": username})
    return username

def validate_password(password):
    """Validates if a password is valid (at least 8 characters)."""
    if not isinstance(password, str):
        raise ValidationError("Password must be a string.")
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    return password