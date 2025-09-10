import os
from src.models.user import Admin, Staff, Customer
from src.utils.file_manager import FileManager
from src.utils.exceptions import FileError, AuthError


class AuthService:
    def __init__(self, user_file_path = "src/data/users.txt"):
        self.user_file_path = user_file_path
        self.current_user = None

    def login(self, username, password):
        try:
            if not FileManager.file_exists(self.user_file_path):
                raise FileError(f"User file not found: {self.user_file_path}, this error is generated in auth_service.")
            
            users = FileManager.read_file(self.user_file_path)
            
            for line in users:
                user_data = line.strip().split("|")
                if len(user_data) != 3:
                    continue
                
                u_name, u_password, u_role = user_data
            
                if username == u_name and password == u_password:
                    if u_role == "admin":
                        self.current_user = Admin(username, u_password)
                        
                        
                    elif u_role == "staff":
                        self.current_user = Staff(username, u_password)
                    elif u_role == "customer":
                        self.current_user = Customer(username, u_password)
                    else:
                        raise AuthError("Invalid user role found in the file.")
                    return self.current_user
            
            raise AuthError("Invalid username or password.")
        
        except FileError as fe:
            raise fe
        except AuthError as ae:
            raise ae
        except Exception as e:
            raise AuthError(f"Login failed: {e}")