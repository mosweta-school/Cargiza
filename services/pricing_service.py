from dateutil.parser import parse
from datetime import timedelta
from dateutil.parser import parse
import holidays


class PricingService:

    def __init__(self):
        self.kenya_holidays = holidays.Kenya()

    def calculate_pricing_breakdown(self, daily_rate, start_date, end_date):

        start = parse(start_date)
        end = parse(end_date)

        current = start

        base_price = 0
        weekend_days = 0

        holiday_details = []  # 👈 NEW

        while current <= end:

            base_price += daily_rate

            # Weekend tracking
            if current.weekday() in [5, 6]:
                weekend_days += 1

            # Holiday tracking (ENHANCED)
            if current.date() in self.kenya_holidays:
                holiday_name = self.kenya_holidays[current.date()]
                holiday_details.append({
                    "date": str(current.date()),
                    "name": str(holiday_name),
                    "discount": daily_rate * 0.15
                })

            current += timedelta(days=1)

        # Weekend discount
        weekend_discount = (weekend_days * daily_rate) * 0.10

        # Holiday discount
        holiday_discount = sum(h["discount"] for h in holiday_details)

        total_discount = weekend_discount + holiday_discount
        final_price = base_price - total_discount

        return {
            "base_price": base_price,
            "weekend_days": weekend_days,
            "weekend_discount": weekend_discount,
            "holiday_details": holiday_details,  # 👈 NEW
            "holiday_discount": holiday_discount,
            "total_discount": total_discount,
            "final_price": final_price
        }