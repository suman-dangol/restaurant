class Order:
    def __init__(self, order_id, customer_username, item_name, quantity, unit_price, status, timestamp, handled_by):
        self.order_id = order_id
        self.customer_username = customer_username
        self.item_name = item_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.status = status
        self.timestamp = timestamp
        self.handled_by = handled_by

    def __str__(self):
        return f"{self.order_id}|{self.customer_username}|{self.item_name}|{self.quantity}|{self.unit_price}|{self.status}|{self.timestamp}|{self.handled_by}"