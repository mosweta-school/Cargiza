from services.booking_service import BookingService


def test_booking_creation():
    service = BookingService()

    car = {
        "id": 1,
        "daily_rate": 100
    }

    booking = service.create_booking(
        1,
        car,
        "2026-08-01",
        "2026-08-03"
    )

    assert "id" in booking
    assert booking["user_id"] == 1