from storage.json_repository import JsonRepository
from services.availability_service import AvailabilityService
from services.booking_service import BookingService





def test_booking_creation_success():
    repo = JsonRepository()

    # CLEAN STATE
    repo.save_data({
        "users": [],
        "cars": [],
        "bookings": []
    })

    service = BookingService(repo)

    car = {
        "id": 1,
        "make": "Toyota",
        "model": "Vitz",
        "daily_rate": 100
    }

    # 👉 IMPORTANT STEP: ADD CAR TO DB
    data = repo.load_data()
    data["cars"].append(car)
    repo.save_data(data)

    result = service.create_booking(
        1,
        car,
        "2026-08-01",
        "2026-08-03"
    )

    assert "id" in result





def test_booking_unavailable():
    service = BookingService()

    car = {
        "id": 1,
        "make": "Toyota",
        "model": "Vitz",
        "daily_rate": 100
    }

    # simulate existing booking in DB
    service.repo.save_data({
        "users": [],
        "cars": [car],
        "bookings": [{
            "id": 1,
            "car_id": 1,
            "start_date": "2026-08-01",
            "end_date": "2026-08-05"
        }]
    })

    result = service.create_booking(
        2,
        car,
        "2026-08-03",
        "2026-08-06"
    )

    assert "error" in result

def test_no_bookings_returns_true():
    repo = JsonRepository()
    repo.save_data({"users": [], "cars": [], "bookings": []})

    service = AvailabilityService(repo)

    result = service.is_available(1, "2026-08-01", "2026-08-03")

    assert result is True

def test_edge_overlap_case():
    repo = JsonRepository()

    repo.save_data({
        "users": [],
        "cars": [],
        "bookings": [{
            "id": 1,
            "car_id": 1,
            "start_date": "2026-08-01",
            "end_date": "2026-08-05"
        }]
    })

    service = AvailabilityService(repo)

    # exact overlap boundary
    result = service.is_available(1, "2026-08-05", "2026-08-07")

    assert result is False

def test_multiple_bookings_check():
    repo = JsonRepository()

    repo.save_data({
        "users": [],
        "cars": [],
        "bookings": [
            {
                "id": 1,
                "car_id": 1,
                "start_date": "2026-08-01",
                "end_date": "2026-08-03"
            },
            {
                "id": 2,
                "car_id": 1,
                "start_date": "2026-08-10",
                "end_date": "2026-08-12"
            }
        ]
    })

    service = AvailabilityService(repo)

    result = service.is_available(1, "2026-08-02", "2026-08-04")

    assert result is False

def test_booking_unavailable_error():
    service = BookingService()

    service.repo.save_data({
        "users": [],
        "cars": [{"id": 1, "daily_rate": 100}],
        "bookings": [{"car_id": 1, "start_date": "2026-01-01", "end_date": "2026-01-05"}]
    })

    result = service.create_booking(1, {"id": 1, "daily_rate": 100}, "2026-01-02", "2026-01-03")

    assert "error" in result