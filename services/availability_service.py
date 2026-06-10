class AvailabilityService:

    def is_available(
        self,
        car_id: int,
        start_date: str,
        end_date: str
    ) -> bool:
        """Checks if car is free in given period"""

    def get_available_cars(
        self,
        category: str,
        start_date: str,
        end_date: str
    ) -> list[Car]:
        """Returns available cars only"""