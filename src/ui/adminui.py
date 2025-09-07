class AdminUI:
    def __init__(self, user):
        self.user = user

    def show_menu(self):
        while True:
            print("\n=== Admin Menu ===")
            print("1. Manage Menu Items (placeholder)")
            print("2. View Orders/Reports (placeholder)")
            print("3. Logout")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                print("👉 [Placeholder] Manage menu items")
            elif choice == "2":
                print("👉 [Placeholder] View reports")
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid option.")
