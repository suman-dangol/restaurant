#users.py


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
    
   # def check_password(self, password):
   ##   return self.password == password
        
    def __repr__(self):
            return f"User(username={self.username}, role={self.role})"


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, role='admin')  
        # Admin-specific attributes can be added here 
        
class Staff(User):
    def __init__(self, username, password):
        super().__init__(username, password, role='staff')  
        # Staff-specific attributes can be added here
        
class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password, role='customer')  
        # Customer-specific attributes can be added here