# Movie Reservation System (Backend API)

## Project Overview
This is a comprehensive backend API for a Movie Reservation System built as a Computer Science Capstone Project. It facilitates the management of movies, cinema halls, and showtimes, while handling the core logic for user reservations.

The system is designed to be **secure** and **stateless**, using JWT (JSON Web Tokens) for authentication. It features a robust relational database design that ensures data integrity, specifically preventing "double-booking" scenarios where two users attempt to book the same seat for the same showtime.

##  Key Features

###  Authentication & Security
* **JWT Authentication:** Secure, stateless login using Access and Refresh tokens.
* **Role-Based Access:** Standard users can only view and book; they cannot modify movie schedules.
* **Data Scoping:** Users can only retrieve their *own* reservation history (privacy protection).

### Reservation Logic
* **Smart Booking Engine:** Links specific users to specific seats at specific times.
* **Conflict Prevention:** Database-level constraints (`unique_together`) ensure it is impossible to double-book a seat.
* **Validation:** Automatic checks to ensure the requested seat and showtime actually exist.

### Inventory Management
* **Movies:** Manage details like title, description, duration, and release date.
* **Cinema Halls:** Define physical rooms and their total capacity.
* **Showtimes:** Schedule specific movies in specific halls at set times with pricing.
* **Seats:** granular management of individual seats (Row/Number) including VIP status.

---

## Tech Stack
* **Language:** Python 3.12.10
* **Framework:** Django 
* **API Toolkit:** Django REST Framework (DRF)
* **Authentication:** Simple JWT
* **Database:** SQLite (Dev) / MySQL (Prod ready)

---

## Installation & Setup 

Follow these steps to run the API locally:

### 1. Clone the Repository

git clone <repo here>
cd <Your Folder here>

### 2. Create a Virtual Environment

# Windows
python -m venv venv
venv\Scripts\activate

### 3. Install Dependenccies
pip install -r requirements.txt

### 4. Database Setup 
Apply the migrations to create the database schema:

python manage.py makemigrations
python manage.py migrate
### 5. Create Admin User
-> to access the Django Admin Panel you have to hit : 
python manage.py createsuperuser

### 6. Run the Server
python manage.py runserver

### App 1: users (Authentication)
Purpose: Handles logic for user roles (Admin vs. Customer).
Endpoints:
POST /auth/register/ - Create a new user.
POST /auth/login/ - Login and receive token/session.
GET /users/me/ - View own profile and role.

### App 2: cinema (Movies & Scheduling)
Purpose: Manages the inventory (movies) and schedule (showtimes).
Endpoints:
GET /movies/ - List all movies (Public).
POST /movies/ - Add a new movie (Admin only).
GET /showtimes/?date=YYYY-MM-DD - Get schedule for a day.
POST /showtimes/ - Create a showtime (Admin only).

### App 3: bookings (Reservations)
Purpose: Handles the complex logic of seats and reservations.
Endpoints:
GET /showtimes/<id>/seats/ - Get seat availability for a specific show.
POST /reservations/ - Book specific seats.
DELETE /reservations/<id>/ - Cancel a booking.
GET /admin/stats/ - View revenue and occupancy reports (Admin only).
### 5. Database Schema (Models)
## Model: User (Custom Model)
username, email, password
role: ChoiceField ('ADMIN', 'CUSTOMER') - defaults to Customer.
## Model: Movie
title: CharField
description: TextField
poster_url: URLField
duration_minutes: IntegerField
## Model: Showtime
movie: ForeignKey (Links to Movie)
start_time: DateTimeField
price: DecimalField
room_name: CharField (e.g., "Screen 1")
## Model: Seat
Note: This can be static (defining the room layout) or dynamic.
room_name: CharField
row: CharField (e.g., "A", "B")
number: IntegerField (e.g., 1, 2, 3)
unique_constraint: (room_name, row, number)
## Model: Reservation
user: ForeignKey (Links to User)
showtime: ForeignKey (Links to Showtime)
seats: ManyToManyField (Links to Seat) or JSONField (to store reserved seat numbers)
status: ChoiceField ('CONFIRMED', 'CANCELLED')
created_at: DateTimeField
