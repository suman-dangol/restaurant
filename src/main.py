import os
from src.utils.file_manager import FileManager

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
    
    auth = auth_service.AuthService(user_file_path)
    try:
        auth.login("admin", "adminpass")
        print(f"Logged in as: {auth.current_user}")
    except Exception as e:
        print(f"Login failed: {e}")
        
if __name__ == "__main__":
    main()