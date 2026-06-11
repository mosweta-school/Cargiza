from services.availability_service import AvailabilityService
from storage.json_repository import JsonRepository
from dateutil.parser import parse


def test_is_available_true():
    repo = JsonRepository()
    repo.save_data({"users": [], "cars": [], "bookings": []})

    service = AvailabilityService(repo)

    result = service.is_available(1, "2026-08-01", "2026-08-03")

    assert result is True


def test_is_available_false():
    repo = JsonRepository()
    repo.save_data({
        "users": [],
        "cars": [],
        "bookings": [
            {
                "car_id": 1,
                "start_date": "2026-08-02",
                "end_date": "2026-08-05"
            }
        ]
    })

    service = AvailabilityService(repo)

    result = service.is_available(1, "2026-08-01", "2026-08-03")

    assert result is False


def test_get_available_cars():
    repo = JsonRepository()
    repo.save_data({
        "users": [],
        "cars": [
            {"id": 1, "category": "SUV"},
            {"id": 2, "category": "SUV"}
        ],
        "bookings": [
            {
                "car_id": 1,
                "start_date": "2026-08-01",
                "end_date": "2026-08-03"
            }
        ]
    })

    service = AvailabilityService(repo)

    result = service.get_available_cars(
        "SUV",
        "2026-08-01",
        "2026-08-03"
    )

    assert isinstance(result, list)


def test_no_overlap_available():
    service = AvailabilityService()

    result = service._dates_overlap(
        parse("2026-08-10"), parse("2026-08-15"),
        parse("2026-08-16"), parse("2026-08-18")
    )

    assert result is False


def test_overlap_detected():
    service = AvailabilityService()

    result = service._dates_overlap(
        parse("2026-08-10"), parse("2026-08-15"),
        parse("2026-08-12"), parse("2026-08-14")
    )

    assert result is True

def test_availability_empty_db():
    service = AvailabilityService()
    service.repo.save_data({"users": [], "cars": [], "bookings": []})

    assert service.is_available(1, "2026-01-01", "2026-01-02") is True

