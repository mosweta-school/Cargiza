from services.pricing_service import PricingService


def test_base_price():
    service = PricingService()

    result = service.calculate_base_price(
        100, "2026-08-01", "2026-08-03"
    )

    assert result == 3 * 100