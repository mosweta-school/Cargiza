from services.pricing_service import PricingService


def test_base_price():
    service = PricingService()

    result = service.calculate_pricing_breakdown(
        100,
        "2026-08-01",
        "2026-08-03"
    )

    assert result["base_price"] == 300
    assert result["weekend_days"] == 2
    assert result["final_price"] <= result["base_price"]

def test_weekend_and_holiday_discount():
    service = PricingService()

    result = service.calculate_pricing_breakdown(
        15000,
        "2026-06-01",
        "2026-06-10"
    )

    assert result["base_price"] == 150000

    assert result["weekend_days"] == 2
    assert result["weekend_discount"] == 3000

    assert len(result["holiday_details"]) == 1
    assert result["holiday_details"][0]["name"] == "Madaraka Day"

    assert result["holiday_discount"] == 2250

    assert result["total_discount"] == 5250

    assert result["final_price"] == 144750
