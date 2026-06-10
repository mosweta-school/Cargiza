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