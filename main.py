import os
from src.utils.file_manager import FileManager
from src.ui.mainui import MainUi

#filepath Setup
script_dir = os.path.dirname(os.path.abspath(__file__))
user_file_path = os.path.join(script_dir, 'data', 'users.txt')
menu_file_path = os.path.join(script_dir, 'data', 'menu.txt')
# Read users from file

# users = FileManager.read_file(data_file_path)
# menu = FileManager.read_file(menu_file_path)

# print(menu)
import src.services.auth_service as auth_service

def main():
    print("Welcome to the Restaurant Management System")
    # Further implementation will go here
    
    main_ui = MainUi()
    main_ui.show_main_menu()
        
if __name__ == "__main__":
    main()