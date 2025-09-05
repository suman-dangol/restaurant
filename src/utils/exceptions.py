
'''AUTH ERROR, FILE ERROR, NOT FOUND ERROR, VALIDATION ERROR'''

# exceptions.py
class AuthError(Exception):
    """Raised when login fails or unauthorized access occurs"""
    def __init__(self, message="Authentication failed"):
        self.message = message
        super().__init__(self.message)

class ValidationError(Exception):
    """Raised when input validation fails"""
    def __init__(self, message="Invalid input"):
        self.message = message
        super().__init__(self.message)

class FileError(Exception):
    """Raised when file operations fail"""
    def __init__(self, message="File operation failed"):
        self.message = message
        super().__init__(self.message)

class NotFoundError(Exception):
    """Raised when a required item or user is not found"""
    def __init__(self, message="Item not found"):
        self.message = message
        super().__init__(self.message)
