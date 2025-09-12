#users.py
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        
    def __repr__(self):
            return f"User(username={self.username}, role={self.role})"


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, role='admin')  
       
        
class Staff(User):
    def __init__(self, username, password):
        super().__init__(username, password, role='staff')  
       
        
class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password, role='customer')  
       