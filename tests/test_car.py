from services.car_service import CarService


def test_add_car():
    service = CarService()

    car = service.add_car({
        "make": "Toyota",
        "model": "Prado",
        "category": "SUV",
        "daily_rate": 100
    })

    assert car["id"] > 0
    # to test updating of car details, we need to first add a car and then update it. So we will add a car with id 1 and then update it to have a new make "Honda". Finally, we will assert that the updated make is "Honda".
def test_update_car():
    service = CarService()

    car = {
        "id": 1,
        "make": "Toyota",
        "model": "Vitz",
        "category": "Hatchback",
        "daily_rate": 100
    }

    service.repo.save_data({"cars": [car], "users": [], "bookings": []})

    updated = service.update_car(1, {"make": "Honda"})

    assert updated["make"] == "Honda"
# This test deletes a car with id 1 and then asserts that the deletion was successful by checking that the delete_car method returns True. We will first add a car with id 1, then delete it, and finally assert that the deletion was successful.
def test_delete_car():
    service = CarService()

    car = {
        "id": 1,
        "make": "Toyota",
        "model": "Vitz",
        "category": "Hatchback",
        "daily_rate": 100
    }

    service.repo.save_data({"cars": [car], "users": [], "bookings": []})

    result = service.delete_car(1)

    assert result is True