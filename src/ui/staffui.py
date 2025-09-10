class StaffUI:
    def __init__(self, user):
        self.user = user

    def show_menu(self):
        while True:
            print("\n=== Staff Menu ===")
            print("1. View Orders (placeholder)")
            print("2. Update Order Status (placeholder)")
            print("3. Logout")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                print("👉 [Placeholder] Viewing orders...")
            elif choice == "2":
                print("👉 [Placeholder] Updating order status...")
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid option.")
