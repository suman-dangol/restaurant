import time
from src.utils.file_manager import FileManager
from src.utils.exceptions import FileError, ValidationError
from src.services.menu_service import MenuService
from src.services.order_service import OrderService

class CustomerUI:
    def __init__(self, user):
        self.user = user
        self.menu_file_path = "src/data/menu.txt"
        self.orders_file_path = "src/data/orders.txt"
        self.menu_service = MenuService()
        self.order_service = OrderService()

    def show_menu(self):
        while True:
            print("\n=== Customer Menu ===")
            print("1. View Menu")
            print("2. Place Order")
            print("3. View Order History")
            print("4. Logout")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.view_menu()
            elif choice == "2":
                self.place_order()
            elif choice == "3":
                self.view_order_history()
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid option.")

    def view_menu(self):
        try:
            menu_lines = FileManager.read_file(self.menu_file_path)
            print("\n=== Menu ===")
            for line in menu_lines:
                print(line)
        except FileError as e:
            print(f"Error viewing menu: {e}, #customerui.py")

    def place_order(self):
        print("\n=== Place Order ===")
        try:
            # Display available menu items with IDs
            print("\n=== Menu ===")
            for item in self.menu_service.menu_items:
                print(f"{item.item_id}: {item.name} - ${item.price}")

            while True:
                try:
                    # Input item IDs
                    item_ids_input = input("\nEnter item IDs (comma-separated): ").strip()
                    if not item_ids_input:
                        print("Please enter at least one item ID.")
                        continue
                    
                    item_ids = [int(item_id.strip()) for item_id in item_ids_input.split(",")]
                    
                    # Validate item IDs
                    valid_ids = [item.item_id for item in self.menu_service.menu_items]
                    invalid_ids = [id for id in item_ids if id not in valid_ids]
                    
                    if invalid_ids:
                        print(f"Invalid item IDs: {invalid_ids}. Please try again.")
                        continue
                    
                    break
                except ValueError:
                    print("Invalid input. Please enter comma-separated numbers.")

            # Create the order using OrderService
            new_orders = self.order_service.create_order(self.user.username, item_ids, self.menu_service)

            if new_orders:
                print("\nOrder placed successfully!")
                print("\n=== Order Details ===")
                total = 0
                for order in new_orders:
                    subtotal = order.unit_price * order.quantity
                    print(f"Item: {order.item_name}")
                    print(f"Quantity: {order.quantity}")
                    print(f"Price per unit: ${order.unit_price:.2f}")
                    print(f"Subtotal: ${subtotal:.2f}\n")
                    total += subtotal
                print(f"Total Order Amount: ${total:.2f}")
            else:
                print("Failed to place order.")

        except Exception as e:
            print(f"Error placing order: {str(e)}")
    def view_order_history(self):
        print("\n=== Order History ===")
        try:
            orders = FileManager.read_file(self.orders_file_path)
            
            # Print header
            print(f"{'Order ID':<10} {'Item Name':<20} {'Quantity':<8} {'Unit Price':<12} {'Status':<10}")
            print("-" * 70)
            
            for order in orders:
                order_data = order.strip().split("|")
                if len(order_data) == 8:
                    order_id, username, item_name, quantity, unit_price, status, timestamp, handled_by = order_data
                    if username == self.user.username:
                        print(f"{order_id:<10} {item_name:<20} {quantity:<8} {unit_price:<12} {status:<10}")
        except FileError as e:
            print(f"Error viewing order history: {e}")
