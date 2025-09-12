from src.utils.file_manager import FileManager
from src.utils.exceptions import FileError, ValidationError
from src.services.menu_service import MenuService
from src.services.order_service import OrderService

class StaffUI:
    def __init__(self, user):
        self.user = user
        self.menu_service = MenuService()
        self.order_service = OrderService()

    def show_menu(self):
        while True:
            print("\n=== Staff Menu ===")
            print("1. View All Orders")
            print("2. Update Order Status")
            print("3. Manage Menu")
            print("4. View Sales Report")
            print("5. Logout")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.view_all_orders()
            elif choice == "2":
                self.update_order_status()
            elif choice == "3":
                self.manage_menu()
            elif choice == "4":
                self.view_sales_report()
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid option.")

    def view_all_orders(self):
        print("\n=== All Orders ===")
        orders = self.order_service.get_all_orders()
        if not orders:
            print("No orders found.")
            return

        print(f"{'Order ID':<10} {'Customer':<15} {'Item':<20} {'Qty':<5} {'Price':<8} {'Status':<10} {'Handled By':<15}")
        print("-" * 85)
        
        for order in orders:
            print(f"{order.order_id:<10} {order.customer_username:<15} {order.item_name:<20} {order.quantity:<5} "
                  f"${order.unit_price:<7} {order.status:<10} {order.handled_by:<15}")

    def update_order_status(self):
        print("\n=== Update Order Status ===")
        try:
            order_id = int(input("Enter Order ID: "))
            print("\nAvailable statuses:")
            print("1. Preparing")
            print("2. Ready")
            print("3. Delivered")
            print("4. Cancelled")
            
            status_choice = input("Enter status choice (1-4): ").strip()
            
            status_map = {
                "1": "preparing",
                "2": "ready",
                "3": "delivered",
                "4": "cancelled"
            }
            
            if status_choice not in status_map:
                print("Invalid status choice.")
                return
                
            new_status = status_map[status_choice]
            if self.order_service.update_order_status(order_id, new_status):
                print(f"Order {order_id} status updated to {new_status}")
            else:
                print("Failed to update order status")
                
        except ValueError:
            print("Invalid input. Please enter a valid order ID.")

    def manage_menu(self):
        while True:
            print("\n=== Manage Menu ===")
            print("1. View Menu")
            print("2. Add Menu Item")
            print("3. Update Menu Item")
            print("4. Delete Menu Item")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.view_menu()
            elif choice == "2":
                self.add_menu_item()
            elif choice == "3":
                self.update_menu_item()
            elif choice == "4":
                self.delete_menu_item()
            elif choice == "5":
                break
            else:
                print("Invalid option.")

    def view_menu(self):
        print("\n=== Current Menu ===")
        print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Price':<8}")
        print("-" * 50)
        for item in self.menu_service.menu_items:
            print(f"{item.item_id:<5} {item.name:<20} {item.category:<15} ${item.price:<7.2f}")

    def add_menu_item(self):
        print("\n=== Add Menu Item ===")
        try:
            name = input("Enter item name: ").strip()
            category = input("Enter category: ").strip()
            price = float(input("Enter price: "))

            if self.menu_service.add_menu_item(name, category, price):
                print("Menu item added successfully!")
            else:
                print("Failed to add menu item.")
        except ValueError:
            print("Invalid price format. Please enter a number.")

    def update_menu_item(self):
        print("\n=== Update Menu Item ===")
        try:
            self.view_menu()
            item_id = int(input("\nEnter item ID to update: "))
            
            print("\nLeave blank to keep current value")
            name = input("Enter new name (or press Enter to skip): ").strip()
            category = input("Enter new category (or press Enter to skip): ").strip()
            price_str = input("Enter new price (or press Enter to skip): ").strip()
            
            price = float(price_str) if price_str else None
            
            if self.menu_service.update_menu_item(item_id, name or None, category or None, price):
                print("Menu item updated successfully!")
            else:
                print("Failed to update menu item.")
        except ValueError:
            print("Invalid input. Please enter valid values.")

    def delete_menu_item(self):
        print("\n=== Delete Menu Item ===")
        try:
            self.view_menu()
            item_id = int(input("\nEnter item ID to delete: "))
            
            confirm = input(f"Are you sure you want to delete item {item_id}? (y/n): ").lower()
            if confirm == 'y':
                if self.menu_service.delete_menu_item(item_id):
                    print("Menu item deleted successfully!")
                else:
                    print("Failed to delete menu item.")
            else:
                print("Deletion cancelled.")
        except ValueError:
            print("Invalid input. Please enter a valid item ID.")

    def view_sales_report(self):
        self.order_service.generate_sales_report()
