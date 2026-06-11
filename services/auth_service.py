import bcrypt
from storage.json_repository import JsonRepository


class AuthService:

    def __init__(self, repo=None):
        self.repo = repo or JsonRepository()

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed.encode())

    def register(self, username, password, role):
        data = self.repo.load_data()

        for user in data["users"]:
            if user["username"] == username:
                return {"error": "User already exists"}

        hashed = self.hash_password(password)

        user = {
            "id": len(data["users"]) + 1,
            "username": username,
            "password": hashed,   # ✅ MUST always exist
            "role": role
        }

        data["users"].append(user)
        self.repo.save_data(data)

        return user

    def login(self, username: str, password: str):
        data = self.repo.load_data()

        for user in data["users"]:
            if user["username"] == username:
                if self.verify_password(password, user["password"]):
                    return user

        return None
    def get_route(self, user):
        if user["role"] == "admin":
            return "admin_dashboard"
        return "customer_dashboard"