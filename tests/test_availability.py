from services.availability_service import AvailabilityService


def test_no_overlap_available():
    service = AvailabilityService()

    result = service._dates_overlap(
        "2026-08-10", "2026-08-15",
        "2026-08-16", "2026-08-18"
    )

    assert result is False


def test_overlap_detected():
    service = AvailabilityService()

    result = service._dates_overlap(
        "2026-08-10", "2026-08-15",
        "2026-08-12", "2026-08-14"
    )

    assert result is True