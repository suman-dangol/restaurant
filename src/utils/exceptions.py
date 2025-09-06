
# exceptions.py
class AuthError(Exception):
    def __init__(self, message="Authentication failed"):
        self.message = message
        super().__init__(self.message)

class ValidationError(Exception):
    def __init__(self, message="Invalid input"):
        self.message = message
        super().__init__(self.message)

class FileError(Exception):
    def __init__(self, message="File operation failed"):
        self.message = message
        super().__init__(self.message)

class NotFoundError(Exception):
    def __init__(self, message="Item not found"):
        self.message = message
        super().__init__(self.message)
