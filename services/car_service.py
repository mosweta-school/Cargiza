from storage.json_repository import JsonRepository


class CarService:

    def __init__(self):
        self.repo = JsonRepository()

    def add_car(self, car: dict):
        data = self.repo.load_data()
        car["id"] = len(data["cars"]) + 1
        data["cars"].append(car)
        self.repo.save_data(data)
        return car

    def get_all_cars(self):
        return self.repo.get_collection("cars")

    def get_by_category(self, category: str):
        cars = self.repo.get_collection("cars")
        return [c for c in cars if c["category"] == category]