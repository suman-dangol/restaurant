from services.auth_service import AuthService
from utils.exceptions import AuthError


auth_service = AuthService('data/users.txt')

try:
    user = auth_service.login("admin", "admin123")
    print("Login successful:", user)
except:
    AuthError("Invalid username or password")
