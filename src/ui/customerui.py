import time
from src.utils.file_manager import FileManager
from src.utils.exceptions import FileError

class CustomerUI:
    def __init__(self, user):
        self.user = user
        self.menu_file_path = "src/data/menu.txt"
        self.orders_file_path = "src/data/orders.txt"

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
            print(f"Error viewing menu: {e}")

    def place_order(self):
        print("\n=== Place Order ===")
        try:
            order_id = input("Enter order ID: ").strip()
            item_name = input("Enter item name: ").strip()
            quantity = input("Enter quantity: ").strip()
            unit_price = input("Enter unit price: ").strip()

            timestamp = str(int(time.time()))
            status = "pending"
            handled_by = "N/A"  # No staff is assigned when the order is placed

            order_string = f"{order_id}|{self.user.username}|{item_name}|{quantity}|{unit_price}|{status}|{timestamp}|{handled_by}"

            FileManager.append_file(self.orders_file_path, order_string)
            print("Order placed successfully!")

        except FileError as e:
            print(f"Error placing order: {e}")

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
