# 🚗 Cargiza - Car Rental Management System

Cargiza is a Python-based Command Line Interface (CLI) application for managing car rentals. It allows administrators to manage vehicle inventory and customers to book cars based on availability, rental duration, and pricing rules.

The system includes dynamic availability checking, pricing calculations with discounts, and persistent data storage using JSON.

---

## 📌 Features

### 👨‍💼 Admin Features
- Add new cars to the system
- Update car details (price, category, etc.)
- Remove cars from inventory
- View all registered cars

### 👤 Customer Features
- View available cars by category
- Book a car for a selected date range
- Receive automatic price calculations
- Apply discounts for:
  - Weekend days (Saturday & Sunday)
  - Public holidays (if applicable)
- View booking history

### ⚙️ System Features
- Real-time car availability checking
- Date range booking system
- Overlapping booking prevention
- Persistent data storage using `db.json`
- Structured and modular design

---

## 🧠 How It Works

1. The user starts the CLI application.
2. Customer selects booking dates and duration.
3. The system checks `db.json` for existing bookings.
4. Available cars in the selected category are displayed.
5. User selects a car.
6. System calculates total cost:
   - Daily rate × number of days
   - Applies 10% discount for weekends
   - Applies holiday discounts (if any)
7. Booking is confirmed and saved to `db.json`.
8. Users can view their booking history anytime.

---

## 🏗️ Project Structure

```
cargiza/
│
├── main.py
├── cli/
│ └── commands.py
├── models/
│ ├── car.py
│ ├── booking.py
│ └── user.py
├── services/
│ ├── booking_service.py
│ ├── pricing_service.py
│ └── availability_service.py
├── utils/
│ ├── file_handler.py
│ └── date_utils.py
├── data/
│ └── db.json
└── tests/
└── test_booking.py
```

---

## 💾 Data Storage (db.json)

The system uses JSON file storage to persist data:

```json
{
  "user":[],
  "cars": [],
  "bookings": []
}
```

This ensures all bookings and car data remain available even after the program is closed.

## 🧮 Pricing Rules

The system calculates rental cost using:

- Base price = daily_rate × number_of_days
- Weekend discount = 10% off Saturday & Sunday
- Holiday discount = 10% off applicable public holidays

## 🧪 Testing

The project uses pytest for testing core logic such as:

- Booking validation
- Date overlap detection
- Price calculation
- Availability filtering

Run tests using:

- pytest

## 🚀 How to Run
1. Clone the repository
git clone https://github.com/mosweta/cargiza.git
cd cargiza
2. Install dependencies
pip install -r requirements.txt
3. Run the application
python main.py

## 🛠️ Technologies Used
- Python 3
- JSON for persistence
- argparse (CLI interface)
- pytest (testing)

## 📈 Future Improvements
- Add user authentication system
- Convert CLI into a web application (Flask/Django)
- Add payment simulation system
- Improve UI with rich terminal interface (Textual / curses)
- Integrate real holiday API for dynamic holiday detection
👨‍💻 Author
Deogracious Moriasi