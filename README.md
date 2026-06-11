# 🚗 Cargiza - Car Rental Management System
---
Cargiza is a Python-based Command Line Interface (CLI) application for managing a car rental system. It supports role-based access (Admin & Customer), booking management, dynamic pricing, and persistent storage using JSON.

The system is designed using object-oriented principles, service-layer architecture, and automated testing with pytest.
---
## 📌 Features
### 👨‍💼 Admin Features
- Add new cars to inventory
- Update car details (price, category, availability)
- Delete/remove cars from system
- View all registered vehicles
  
### 👤 Customer Features
- View available cars by category and date
- Book cars using date-range selection
- Automatic pricing calculation
- View booking history
  
### ⚙️ System Features
- Real-time availability checking (prevents overlapping bookings)
- Date-range booking system
- Persistent JSON-based storage (db.json)
- Modular service-oriented architecture
- Role-based access control (Admin / Customer)
  
## 🧠 How It Works
- User starts the CLI application (python main.py)
- User logs in or registers an account
- Role determines access (Admin or Customer)
- Customer selects booking dates
- System checks:
  1. Car availability
  2. Existing bookings (overlap detection)
  3. Pricing engine calculates total cost:
  4. Base rate × number of days
  5. Weekend discount applied (if applicable)
  6. Holiday discount applied (if applicable)
- Booking is saved into db.json
## 🏗️ System Architecture

The system follows a layered architecture:
```
CLI Layer
   ↓
Service Layer
(Auth / Booking / Pricing / Availability)
   ↓
Repository Layer
(JSON Persistence)
```

## 📂 Project Structure
```
cargiza/
│
├── main.py
│
├── cli/
│   ├── auth_cli.py
│   ├── admin_cli.py
│   └── customer_cli.py
│
├── services/
│   ├── auth_service.py
│   ├── booking_service.py
│   ├── pricing_service.py
│   ├── availability_service.py
│   └── car_service.py
│
├── storage/
│   └── json_repository.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_booking.py
│   ├── test_booking_lifecycle.py
│   ├── test_pricing.py
│   ├── test_availability.py
│   └── test_cli_integration.py
│
├── data/
│   └── db.json
│
├── requirements.txt
└── README.md
```
## 💾 Data Storage

The system uses a JSON file (db.json) for persistence:
```
{
  "users": [],
  "cars": [],
  "bookings": []
}
```

## 🧮 Pricing Rules

Pricing is computed dynamically based on booking duration:

Formula:
Base price = daily_rate × number_of_days
Discounts:
Weekend discount (Saturday & Sunday)
Holiday discount (public holidays if applicable)

Note: Holiday detection is implemented using holidays python package

## 🧪 Testing Strategy

The project uses pytest for automated testing.

Coverage Includes:
- Authentication logic
- Booking creation & validation
- Availability checks
- Pricing calculations
- Repository persistence
- CLI integration flows
- Booking lifecycle scenarios
Run tests:
```
python3 -m pytest
```
Run coverage:
```
python3 -m pytest --cov=services --cov-report=html
```
Current coverage:
- 94%
![Coverage](https://img.shields.io/badge/coverage-94%25-brightgreen)

## 🚀 How to Run
1. Clone repository
```bash
git clone https://github.com/opiyo/cargiza.git
cd cargiza
```
3. Create virtual environment
```bash
python3 -m venv .env
```
3. Activate environment
```bash
source .env/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run application
```bash
python main.py
```

## 🧑‍💻 Git Workflow
Branching Strategy:
```
main → production-ready code
development → integration branch
feature/* → feature development
```
Workflow:
```
git checkout development
git pull origin development
git checkout -b feature/new-feature
```
Commit changes:
```
git add .
git commit -m "Add feature"
```
Push:
```
git push origin feature/new-feature
```
Merge flow:
```
feature → development → main
```

## 🛠️ Technologies Used
- Python 3
- JSON for persistence
- argparse (CLI interface)
- pytest (testing) + pytest-cov (test coverage)
- bcrypt (password hashing)
- tabulate	(Professional CLI tables)
- holidays	(Detect Kenyan public holiday)
- python-dateutil	(Date calculations and parsing)
- GitHub Actions CI

## 📈 Future Improvements
- Convert CLI into a web application (Flask/Django)
- Add payment simulation system
- Improve UI with rich terminal interface (Textual / curses)
- Integrate real holiday API for dynamic holiday detection
👨‍💻 Author
Deogracious Moriasi
