import json
import os


class JsonRepository:

    def __init__(self, file_path="data/db.json"):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Creates db.json if it doesn't exist"""
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({
                    "users": [],
                    "cars": [],
                    "bookings": []
                }, f, indent=4)

    def load_data(self) -> dict:
        """Load entire database safely (CI-proof)"""
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        # ✅ GUARANTEE STRUCTURE
        data.setdefault("users", [])
        data.setdefault("cars", [])
        data.setdefault("bookings", [])

        return data

    def save_data(self, data: dict) -> None:
        """Save entire database"""
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_collection(self, name: str):
        """Get users/cars/bookings list"""
        data = self.load_data()
        return data.get(name, [])

    def update_collection(self, name: str, items: list):
        """Update a specific collection"""
        data = self.load_data()
        data[name] = items
        self.save_data(data)