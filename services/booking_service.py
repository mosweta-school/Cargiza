class BookingService:

    def create_booking(
        self,
        user_id: int,
        car_id: int,
        start_date: str,
        end_date: str
    ) -> Booking:
        """Creates and saves booking"""

    def get_user_bookings(self, user_id: int) -> list[Booking]:
        """Returns bookings for a user"""

    def get_all_bookings(self) -> list[Booking]:
        """Admin view of all bookings"""