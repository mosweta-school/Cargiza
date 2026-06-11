import re
from datetime import datetime


class Validators:

    @staticmethod
    def is_valid_username(username: str) -> bool:
        """Checks if username is valid (simple rules)"""
        return len(username) >= 3 and username.isalnum()

    @staticmethod
    def is_valid_password(password: str) -> bool:
        """
        Password rules:
        - At least 4 characters (simple for coursework)
        """
        return len(password) >= 4

    @staticmethod
    def is_valid_role(role: str) -> bool:
        """Ensures role is either admin or customer"""
        return role in ["admin", "customer"]

    @staticmethod
    def is_valid_date(date_str: str) -> bool:
        """Validates YYYY-MM-DD format"""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_positive_number(value: str) -> bool:
        """Checks if input is a positive integer"""
        return value.isdigit() and int(value) > 0