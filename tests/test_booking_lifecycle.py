from services.booking_service import BookingService
from storage.json_repository import JsonRepository


def test_booking_lifecycle():
    repo = JsonRepository()

    repo.save_data({
        "users": [],
        "cars": [{
            "id": 1,
            "make": "Toyota",
            "model": "Vitz",
            "daily_rate": 100,
            "category": "SUV"
        }],
        "bookings": []
    })

    service = BookingService(repo)

    # 1. CREATE
    booking = service.create_booking(
        1,
        {"id": 1, "make": "Toyota", "model": "Vitz", "daily_rate": 100},
        "2026-08-01",
        "2026-08-03"
    )

    assert "id" in booking

    booking_id = booking["id"]

    # 2. CANCEL
    cancelled = service.cancel_booking(booking_id)
    assert cancelled is True

    # 3. REBOOK (should now succeed again)
    booking2 = service.create_booking(
        1,
        {"id": 1, "make": "Toyota", "model": "Vitz", "daily_rate": 100},
        "2026-08-01",
        "2026-08-03"
    )

    assert "id" in booking2