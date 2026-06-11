from services.auth_service import AuthService

class AuthCLI:

    def __init__(self, repo=None):
        self.service = AuthService(repo)

    def show_login(self, username=None, password=None):
        """Handles login flow (interactive + testable)"""

        print("\n======================")
        print("     CARGIZA LOGIN    ")
        print("======================\n")

        #  TEST MODE (no input())
        if username is not None and password is not None:
            user = self.service.login(username, password)

            if user:
                print("\nLogin successful!")
                print(f"Welcome {user['username']} ({user['role']})\n")
                return user

            print("\nInvalid username or password!\n")
            return None

        #  INTERACTIVE MODE (real CLI)
        username = input("Username: ")
        password = input("Password: ")

        user = self.service.login(username, password)

        if user:
            print("\nLogin successful!")
            print(f"Welcome {user['username']} ({user['role']})\n")
            return user

        print("\nInvalid username or password!\n")
        return None

    def show_register(self):
        """Register new users"""

        print("\n===== REGISTER =====")

        username = input("Username: ")
        password = input("Password: ")

        print("\nSelect Role:")
        print("1. Admin")
        print("2. Customer")

        role_choice = input("Choice: ")
        role = "admin" if role_choice == "1" else "customer"

        user = self.service.register(username, password, role)

        # ✅ HANDLE ERROR CASE
        if "error" in user:
            print("\nRegistration failed:", user["error"])
            return user

        print("\nUser created successfully!")
        print(f"Welcome {user['username']} ({user['role']})")

        return user