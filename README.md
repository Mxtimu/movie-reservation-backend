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
```bash
git clone <repo here>
cd <Your Folder here>

### 2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate


