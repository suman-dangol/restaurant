from src.services.auth_service import AuthService
from src.utils.exceptions import AuthError
from src.ui.adminui import AdminUI
from src.ui.staffui import StaffUI
from src.ui.customerui import CustomerUI

class MainUi:
    def __init__(self):
        self.auth_service = AuthService()
   
    def show_main_menu(self):
        """Display the main menu and handle navigation."""
        while True:
            print("\n=== Restaurant Ordering System ===")
            print("1. Login")
            print("2. Exit")

            choice = input("Enter your choice: ").strip()
            
            
            if choice == "1":
                self.handle_login()
            elif choice == "2":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def handle_login(self):
        """Authenticate user and redirect to their role-specific UI."""
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        try:
            user = self.auth_service.login(username, password)
            print(f"\n Welcome, {user.username}! (Role: {user.role})")
            
            self.redirect_to_role_ui(user)
        except AuthError as ae:
            print(f"Login failed: {ae.message}")
            
    def redirect_to_role_ui(self, user):
        """Redirect user to their role-specific UI."""
        if user.role == "admin":
           
            admin_ui = AdminUI(user)
            admin_ui.show_menu()
        elif user.role == "staff":
           
            staff_ui = StaffUI(user)
            staff_ui.show_menu()
        elif user.role == "customer":
            
            customer_ui = CustomerUI(user)
            customer_ui.show_menu()
        else:
            print(" Unknown user role. Cannot redirect.")