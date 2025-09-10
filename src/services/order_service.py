from src.models.order import Order
from src.utils.file_manager import FileManager
from src.utils.exceptions import FileError, ValidationError, NotFoundError
from src.utils.validators import validate_id
import time

class OrderService:
    def __init__(self, order_file_path="src/data/orders.txt"):
        self.order_file_path = order_file_path
        self.orders = self.load_orders()

    def load_orders(self):
        """Loads orders from the orders file."""
        try:
            lines = FileManager.read_file(self.order_file_path)
            orders = []
    
            for line in lines[1:]:  # Skip header line
                order_data = line.strip().split("|")
                if len(order_data) == 8:
                    order_id, customer_username, item_name, quantity, unit_price, status, timestamp, handled_by = order_data
                    try:
                        order_id = int(order_id)
                        order_id = validate_id(order_id)
                        quantity = int(quantity)
                        unit_price = float(unit_price)
                        order = Order(order_id, customer_username, item_name, quantity, unit_price, status, timestamp, handled_by)
                        orders.append(order)
                    except ValueError:
                        print(f"Invalid data format in order file. Skipping line: {line}")
                        continue
                    except ValidationError as e:
                        print(f"Validation error loading order: {e}")
                        continue
                else:
                    print(f"Skipping line due to incorrect format (expected 8 parts). Line: {line}")
                    continue
            return orders
        except FileError as e:
            print(f"Error loading orders: {e}")
            return []
 
    def create_order(self, customer_username, item_ids, menu_service):
        """Creates a new order."""
        try:
            if not customer_username or not item_ids or not menu_service:
                raise ValidationError("Missing required parameters")

            # Fetch all menu items at once
            menu_items = {item.item_id: item for item in menu_service.menu_items}
            
            # Generate new order ID
            new_order_id = 1
            if self.orders:
                new_order_id = max(int(order.order_id) for order in self.orders) + 1

            timestamp = str(int(time.time()))
            new_orders = []

            # Create separate order entries for each item
            for item_id in item_ids:
                if item_id not in menu_items:
                    raise ValidationError(f"Invalid item ID: {item_id}")

                item = menu_items[item_id]

                # Ask for quantity with validation
                while True:
                    try:
                        quantity = int(input(f"Enter quantity for {item.name} (1-99): "))
                        if 0 < quantity < 100:
                            break
                        print("Please enter a quantity between 1 and 99.")
                    except ValueError:
                        print("Please enter a valid number.")

                # Create new order
                new_order = Order(
                    order_id=new_order_id,
                    customer_username=customer_username,
                    item_name=item.name,
                    quantity=quantity,
                    unit_price=item.price,
                    status="pending",
                    timestamp=timestamp,
                    handled_by="N/A"
                )

                # Convert order to string format
                order_str = str(new_order)

                try:
                    # Save to file
                    FileManager.append_file(self.order_file_path, order_str)
                    
                    # Update in-memory list and new_orders list
                    self.orders.append(new_order)
                    new_orders.append(new_order)
                    
                    new_order_id += 1
                except FileError as fe:
                    print(f"Error saving order to file: {fe}")
                    return None

            return new_orders

        except ValidationError as e:
            print(f"Validation error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return None
    def get_orders_by_customer_id(self, customer_id):
        """Returns a list of orders for a given customer ID."""
        return [order for order in self.orders if order.customer_id == customer_id]

    def update_order_status(self, order_id, status):
        """Updates the status of an order."""
        try:
            order_id = validate_id(order_id)
            order = self.get_order_by_id(order_id)
            if not order:
                raise NotFoundError(f"Order with ID {order_id} not found.")

            order.status = status
            self._save_orders_to_file()
            return True
        except FileError as e:
            print(f"Error updating order status: {e}")
            return False
        except ValidationError as e:
            print(f"Validation error: {e}")
            return False
        except NotFoundError as e:
            print(f"{e}")
            return False

    def _save_orders_to_file(self):
        """Saves the current orders to the file."""
        try:
            lines = ["order_id|customer_username|item_name|quantity|unit_price|status|timestamp|handled_by"] + [str(order) for order in self.orders]
            FileManager.write_file(self.order_file_path, lines)
        except FileError as e:
            print(f"Error saving orders to file: {e}")

    def get_all_orders(self):
        """Returns all orders."""
        return self.orders

    def generate_sales_report(self):
        print("\n=== Sales Report ===")
        if not self.orders:
            print("No orders found.")
            return
        """Generates a sales report."""
        total_revenue = sum(order.total for order in self.orders)
        orders_by_category = {}  # This would require menu item category info in orders
        # For simplicity, this example does not include category breakdown
        
        print(f"Total Revenue: ${total_revenue:.2f}, Orders Count: {len(self.orders)}")
        return {
            'total_revenue': total_revenue,
            'orders_by_category': orders_by_category
        }