from services.car_service import CarService
from services.booking_service import BookingService
from services.availability_service import AvailabilityService
from tabulate import tabulate


class CustomerCLI:

    def __init__(self, user):
        self.user = user
        self.car_service = CarService()
        self.booking_service = BookingService()
        self.availability_service = AvailabilityService()

    def run(self):
        while True:
            print("\n===== CUSTOMER DASHBOARD =====")
            print("1. View Cars")
            print("2. Book Car")
            print("3. View My Bookings")
            print("4. Cancel Booking")
            print("5. Logout")

            choice = input("Select option: ")

            if choice == "1":
                self.view_cars()

            elif choice == "2":
                self.book_car()

            elif choice == "3":
                self.view_bookings()

            elif choice == "4":
                self.cancel_booking()

            elif choice == "5":
                print("Logging out...\n")
                break

    def view_cars(self):
        cars = self.car_service.get_all_cars()

        table = [[c["id"], c["make"], c["model"], c["category"], c["daily_rate"]] for c in cars]

        print(tabulate(table, headers=["ID", "Make", "Model", "Category", "Rate"]))

    def book_car(self):
        CAR_CATEGORIES = ["SUV", "Sedan", "Hatchback", "Truck", "Van"]
        print("\n--- Book a Car ---")

        print("\nSelect Category:")

        for i, c in enumerate(CAR_CATEGORIES, 1):
            print(f"{i}. {c}")

        cat_index = int(input("Choice: ")) - 1
        category = CAR_CATEGORIES[cat_index]
        start_date = input("Start Date (YYYY-MM-DD): ")
        end_date = input("End Date (YYYY-MM-DD): ")

        available_cars = self.availability_service.get_available_cars(
            category,
            start_date,
            end_date
        )

        if not available_cars:
            print("No cars available for selected dates.")
            return

        table = [[c["id"], c["make"], c["model"], c["daily_rate"]] for c in available_cars]
        print(tabulate(table, headers=["ID", "Make", "Model", "Rate"]))

        car_id = int(input("Enter Car ID to book: "))

        selected_car = next((c for c in available_cars if c["id"] == car_id), None)

        if not selected_car:
            print("Invalid car selection.")
            return

        booking = self.booking_service.create_booking(
            self.user["id"],
            selected_car,
            start_date,
            end_date
        )

        print("\nBooking successful!")
        print("\n===== HOLIDAY BREAKDOWN =====")

        if booking["pricing"]["holiday_details"]:
            for h in booking["pricing"]["holiday_details"]:
                print(f"{h['name']} ({h['date']}) → Discount: {h['discount']}")
        else:
            print("No holidays in selected period")
        print("\n===== BOOKING CONFIRMATION =====")
        print(f"Base Price: {booking['pricing']['base_price']}")
        print(f"Weekend Days: {booking['pricing']['weekend_days']}")
        
        print(f"Weekend Discount: {booking['pricing']['weekend_discount']}")
        print(f"Holiday Discount: {booking['pricing']['holiday_discount']}")
        print(f"Total Discount: {booking['pricing']['total_discount']}")
        print(f"FINAL PRICE: {booking['pricing']['final_price']}")
        print(f"Total Cost: {booking['total_cost']}")

    def view_bookings(self):
        bookings = self.booking_service.get_user_bookings(self.user["id"])

        table = [[
            b["id"],
            b["car_id"],
            b["car_make"],
            b["car_model"],
            b["start_date"],
            b["end_date"],
            b["total_cost"]
        ] for b in bookings]

        print(tabulate(table, headers=["ID", "CarId","Make","Model", "Start", "End", "Cost"]))
    def cancel_booking(self):
        print("\n===== CANCEL BOOKING =====")

        bookings = self.booking_service.get_user_bookings(self.user["id"])

        if not bookings:
            print("No bookings found.")
            return

        table = [[
            b["id"],
            b["car_id"],
            b["start_date"],
            b["end_date"],
            b["total_cost"]
        ] for b in bookings]

        print(tabulate(table, headers=["ID", "Car ID", "Start", "End", "Cost"]))

        booking_id = int(input("\nEnter Booking ID to cancel: "))

        result = self.booking_service.cancel_booking(booking_id)

        if isinstance(result, dict) and "error" in result:
            print("\n❌", result["error"])
        else:
            print("\n✅ Booking cancelled successfully!")