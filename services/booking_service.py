from services.availability_service import AvailabilityService
from services.pricing_service import PricingService
from storage.json_repository import JsonRepository


class BookingService:

    def __init__(self, repo=None):
        self.repo = repo or JsonRepository()
        self.availability = AvailabilityService(self.repo)
        self.pricing = PricingService()

    def create_booking(self, user_id, car, start_date, end_date):

        data = self.repo.load_data()

        #ENSURE CAR EXISTS IN DB
        car_exists = any(c["id"] == car["id"] for c in data["cars"])
        if not car_exists:
            return {"error": "Car not found"}

        if not self.availability.is_available(car["id"], start_date, end_date):
            return {"error": "Car not available"}

        pricing = self.pricing.calculate_pricing_breakdown(
            car["daily_rate"],
            start_date,
            end_date
        )

        booking = {
            "id": len(data["bookings"]) + 1,
            "user_id": user_id,
            "car_id": car["id"],
            "car_make": car["make"],
            "car_model": car["model"],
            "start_date": start_date,
            "end_date": end_date,
            "pricing": pricing,
            "total_cost": pricing["final_price"]
        }

        data["bookings"].append(booking)
        self.repo.save_data(data)

        return booking

    def get_user_bookings(self, user_id):
        data = self.repo.load_data()
        return [b for b in data["bookings"] if b["user_id"] == user_id]

    def get_all_bookings(self):
        return self.repo.load_data()["bookings"]
    def cancel_booking(self, booking_id):
        data = self.repo.load_data()

        data["bookings"] = [
            b for b in data["bookings"]
            if b["id"] != booking_id
        ]

        self.repo.save_data(data)
        print("Booking cancelled successfully.")
        return True