from storage.json_repository import JsonRepository
from services.availability_service import AvailabilityService
from services.pricing_service import PricingService


class BookingService:

    def __init__(self):
        self.repo = JsonRepository()
        self.availability = AvailabilityService()
        self.pricing = PricingService()

    def create_booking(self, user_id, car, start_date, end_date):

        # 1. Check availability
        if not self.availability.is_available(car["id"], start_date, end_date):
            return {"error": "Car not available"}

        # 2. Calculate price
        pricing = self.pricing.calculate_pricing_breakdown(
            car["daily_rate"],
            start_date,
            end_date
        )

        total = pricing["final_price"]

        # 3. Load DB
        data = self.repo.load_data()

        booking = {
            "id": len(data["bookings"]) + 1,
            "user_id": user_id,
            "car_id": car["id"],
            "car_make": car["make"],
            "car_model": car["model"],
            "start_date": start_date,
            "end_date": end_date,
            "pricing": pricing,
            "total_cost": total
        }

        data["bookings"].append(booking)
        self.repo.save_data(data)

        return booking

    def get_user_bookings(self, user_id):
        data = self.repo.load_data()
        return [b for b in data["bookings"] if b["user_id"] == user_id]

    def get_all_bookings(self):
        return self.repo.load_data()["bookings"]