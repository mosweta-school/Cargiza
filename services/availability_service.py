from storage.json_repository import JsonRepository
from dateutil.parser import parse


class AvailabilityService:

    def __init__(self):
        self.repo = JsonRepository()

    def _dates_overlap(self, start1, end1, start2, end2):
        """Core overlap logic"""
        return start1 <= end2 and start2 <= end1

    def is_available(self, car_id: int, start_date: str, end_date: str) -> bool:
        data = self.repo.load_data()

        new_start = parse(start_date)
        new_end = parse(end_date)

        for booking in data["bookings"]:
            if booking["car_id"] == car_id:
                existing_start = parse(booking["start_date"])
                existing_end = parse(booking["end_date"])

                if self._dates_overlap(new_start, new_end, existing_start, existing_end):
                    return False

        return True

    def get_available_cars(self, category: str, start_date: str, end_date: str):
        data = self.repo.load_data()

        available = []

        for car in data["cars"]:
            if car["category"] == category:
                if self.is_available(car["id"], start_date, end_date):
                    available.append(car)

        return available