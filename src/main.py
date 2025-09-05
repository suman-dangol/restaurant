import os
from utils.file_manager import FileManager

#filepath Setup
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'data', 'users.txt')
menu_file_path = os.path.join(script_dir, 'data', 'menu.txt')
user_file_path = os.path.join(script_dir, 'data', 'current_user.txt')
# Read users from file

users = FileManager.read_file(data_file_path)
menu = FileManager.read_file(menu_file_path)

print(menu)