from src.services.menu_service import MenuService
from src.services.order_service import OrderService  # Import OrderService
import datetime
class AdminUI:
    def __init__(self, user):
        self.user = user
        self.menu_service = MenuService()  # Instantiate MenuService
        self.order_service = OrderService() # Instantiate OrderService

    def show_menu(self):
        while True:
            print("\n=== Admin Menu ===")
            print("1. Manage Menu Items")
            print("2. View Orders/Reports")
            print("3. Logout")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.manage_menu_items()
            elif choice == "2":
                self.view_orders_reports()
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid option.")

    def manage_menu_items(self):
        while True:
            print("\n--- Manage Menu Items ---")
            print("1. Add Item")
            print("2. Edit Item")
            print("3. Remove Item")
            print("4. View Menu")
            print("5. Back to Admin Menu")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_menu_item()
            elif choice == "2":
                self.edit_menu_item()
            elif choice == "3":
                self.remove_menu_item()
            elif choice == "4":
                self.view_menu()
            elif choice == "5":
                break
            else:
                print("Invalid option.")

    def add_menu_item(self):
        name = input("Enter item name: ").strip()
        category = input("Enter item category: ").strip()
        while True:
            try:
                price = float(input("Enter price: ").strip())
                break
            except ValueError:
                print("Invalid price. Please enter a number.")

        if self.menu_service.add_menu_item(name, category, price):
            print(f"Added {name} to the menu.")
        else:
            print("Failed to add item to menu.")

    def edit_menu_item(self):
        item_id = input("Enter item ID to edit: ").strip()
        try:
            item_id = int(item_id)
        except ValueError:
            print("Invalid item ID. Please enter a number.")
            return

        name = input("Enter new name (or leave blank): ").strip()
        category = input("Enter new category (or leave blank): ").strip()
        price_str = input("Enter new price (or leave blank): ").strip()

        price = None
        if price_str:
            try:
                price = float(price_str)
            except ValueError:
                print("Invalid price. Edit cancelled.")
                return

        if self.menu_service.update_menu_item(item_id, name, category, price):
            print(f"Menu item {item_id} updated.")
        else:
            print(f"Failed to update menu item {item_id}.")

    def remove_menu_item(self):
         item_id = input("Enter item ID to remove: ").strip()
         try:
             item_id = int(item_id)
         except ValueError:
             print("Invalid item ID. Please enter a number.")
             return

         if self.menu_service.delete_menu_item(item_id):
             print(f"Menu item {item_id} removed.")
         else:
             print(f"Failed to remove menu item {item_id}.")

    def view_menu(self):
        menu_items = self.menu_service.menu_items
        if not menu_items:
            print("Menu is empty.")
            return

        print("\n--- Current Menu ---")
        for item in menu_items:
            print(f"{item.item_id}. {item.name} ({item.category}) - ${item.price:.2f}")

    def view_orders_reports(self):
        while True:
            print("\n--- View Orders/Reports ---")
            print("1. View All Orders")
            print("2. Generate Sales Report")
            print("3. Back to Admin Menu")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.view_all_orders()
            elif choice == "2":
                self.generate_sales_report()
            elif choice == "3":
                break
            else:
                print("Invalid option.")

    def view_all_orders(self):
        orders = self.order_service.get_all_orders()
        if not orders:
            print("No orders found.")
            return


        print("\n--- All Orders ---")
        for order in orders:
            # print(f"Order ID: {order.order_id}, Total: ${order.total:.2f}, Status: {order.status}")
            # print(f"  Items: {order.items}") # Just printing item IDs for brevity
            
            print(f"Order ID: {order.order_id}, Customer: {order.customer_username}, Item: {order.item_name}, Quantity: {order.quantity}, Unit Price: ${order.unit_price:.2f}, Status: {order.status}, Handled By: {order.handled_by}")

    def generate_sales_report(self):
        try:
            self.order_service.generate_sales_report()
        except Exception as e:
            print(f"Error generating sales report: {e}")        