class FakeRepository:
    def __init__(self):
        self.data = {
            "users": [],
            "cars": [],
            "bookings": []
        }

    def load_data(self):
        return self.data

    def save_data(self, data):
        self.data = data