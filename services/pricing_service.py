class PricingService:

    def calculate_base_price(
        self,
        daily_rate: float,
        start_date: str,
        end_date: str
    ) -> float:
        """Calculates raw rental cost"""

    def apply_weekend_discount(
        self,
        amount: float,
        start_date: str,
        end_date: str
    ) -> float:
        """Applies 10% weekend discount"""

    def apply_holiday_discount(
        self,
        amount: float,
        start_date: str,
        end_date: str
    ) -> float:
        """Applies holiday discount using holidays package"""

    def calculate_total(
        self,
        daily_rate: float,
        start_date: str,
        end_date: str
    ) -> float:
        """Final price after all rules"""