from services.car_service import CarService
from services.booking_service import BookingService
from utils.validators import Validators
from tabulate import tabulate


class AdminCLI:

    def __init__(self, user):
        self.user = user
        self.car_service = CarService()
        self.booking_service = BookingService()

    def run(self):
        while True:
            print("\n===== ADMIN DASHBOARD =====")
            print("1. Add Car")
            print("2. View Cars")
            print("3. Update Car")
            print("4. Delete Car")
            print("5. View All Bookings")
            print("6. Logout")

            choice = input("Select option: ")

            if choice == "1":
                self.add_car()

            elif choice == "2":
                self.view_cars()

            elif choice == "3":
                self.update_car()
                
            elif choice == "4":
                self.delete_car()

            elif choice == "5":
                self.view_bookings()

            elif choice == "6":
                print("Logging out...\n")
                break

    def add_car(self):
        CAR_CATEGORIES = ["SUV", "Sedan", "Hatchback", "Truck", "Van"]
        print("\n--- Add New Car ---")

        make = input("Make: ")
        model = input("Model: ")

        print("\nSelect Category:")
        for i, c in enumerate(CAR_CATEGORIES, 1):
            print(f"{i}. {c}")

        cat_index = int(input("Choice: ")) - 1
        category = CAR_CATEGORIES[cat_index]

        rate = float(input("Daily Rate: "))

        car = {
            "make": make,
            "model": model,
            "category": category,
            "daily_rate": rate
        }

        self.car_service.add_car(car)
        print("\nCar added successfully!")

    def view_cars(self):
        cars = self.car_service.get_all_cars()

        table = [[c["id"], c["make"], c["model"], c["category"], c["daily_rate"]] for c in cars]

        print(tabulate(table, headers=["ID", "Make", "Model", "Category", "Rate"]))

    def view_bookings(self):
        bookings = self.booking_service.get_all_bookings()

        table = [[
            b["id"],
            b["user_id"],
            b["car_id"],
            b["start_date"],
            b["end_date"],
            b["total_cost"]
        ] for b in bookings]

        print(tabulate(table, headers=["ID", "User", "Car", "Start", "End", "Cost"]))

    def update_car(self):
        print("\n--- Update Car ---")

        cars = self.car_service.get_all_cars()

        for c in cars:
            print(f"{c['id']} - {c['make']} {c['model']} | {c['category']} | {c['daily_rate']}")

        car_id = int(input("\nEnter Car ID to update: "))

        print("\nLeave field blank to keep current value")

        make = input("New Make: ")
        model = input("New Model: ")
        category = input("New Category: ")
        rate = input("New Daily Rate: ")

        updates = {}

        if make:
            updates["make"] = make
        if model:
            updates["model"] = model
        if category:
            updates["category"] = category
        if rate:
            updates["daily_rate"] = float(rate)

        updated_car = self.car_service.update_car(car_id, updates)

        if updated_car:
            print("\nCar updated successfully!")
        else:
            print("\nCar not found!")

    def delete_car(self):
        print("\n--- Delete Car ---")

        cars = self.car_service.get_all_cars()

        for c in cars:
            print(f"{c['id']} - {c['make']} {c['model']}")

        try:
            car_id = int(input("\nEnter Car ID to delete: "))
        except ValueError:
            print("Invalid input!")
            return

        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() != "y":
            print("Cancelled.")
            return

        success = self.car_service.delete_car(car_id)

        if success:
            print("Car deleted successfully!")
        else:
            print("Car not found!")