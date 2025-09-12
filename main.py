import os
from src.ui.mainui import MainUi

#filepath Setup
script_dir = os.path.dirname(os.path.abspath(__file__))
user_file_path = os.path.join(script_dir, 'data', 'users.txt')
menu_file_path = os.path.join(script_dir, 'data', 'menu.txt')


def main():
    print("Welcome to the Restaurant Management System")
    
    main_ui = MainUi()
    main_ui.show_main_menu()
        
if __name__ == "__main__":
    main()