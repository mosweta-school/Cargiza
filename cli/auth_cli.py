from services.auth_service import AuthService


class AuthCLI:
    def __init__(self):
        self.auth_service = AuthService()

    def show_login(self):
        """Displays login screen and handles authentication flow"""

        print("\n======================")
        print("     CARGIZA LOGIN    ")
        print("======================\n")

        username = input("Username: ")
        password = input("Password: ")

        user = self.auth_service.login(username, password)

        if user:
            print("\nLogin successful!")
            print(f"Welcome {user['username']} ({user['role']})\n")
            return user
        else:
            print("\nInvalid username or password!\n")
            return None

    def show_register(self):
        """Optional: register new users (useful for testing)"""

        print("\n===== REGISTER =====")

        username = input("Username: ")
        password = input("Password: ")

        print("\nSelect Role:")
        print("1. Admin")
        print("2. Customer")

        role_choice = input("Choice: ")

        role = "admin" if role_choice == "1" else "customer"

        user = self.auth_service.register(username, password, role)

        print("\nUser created successfully!")
        print(f"Username: {user['username']}, Role: {user['role']}\n")

        return user