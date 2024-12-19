# E-commerce Website Project

## Overview
This project is a comprehensive E-commerce Website built using HTML, CSS, and the Django framework, designed to provide seamless shopping, management, and delivery experiences. The platform is role-based, offering distinct functionalities for Users, Admins, and Delivery Personnel, ensuring smooth operations and a user-friendly interface.

---

## Features

### User Functionalities
#### Account Management:
- Signup / Create Account
- Login / Logout

#### Product Browsing:
- View all available products
- Filter products by category

#### Cart Management:
- Add products to the cart
- Update item quantities
- Automatically update the total price

#### Order Management:
- Place orders
- View order status (delivered/pending)

### Admin Functionalities
#### Account Management:
- Login / Logout

#### Product and Category Management:
- Add/remove products
- Add/remove categories
- View the list of available products and categories

#### Order Management:
- View pending and completed orders

### Delivery Personnel Functionalities
#### Account Management:
- Login / Logout

#### Order Tracking:
- View pending and completed orders
- Update the status of products (delivered/pending)

---

## Demo

*(Add demo details or screenshots if available)*

---

## Technologies Used
- **Frontend:** HTML, CSS
- **Backend:** Django
- **Database:** SQLite (Default)

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/ecommerce-website.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd ecommerce-website
   ```

3. **Set Up a Virtual Environment:**
   - On Linux:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     python3 -m venv env
     env\Scripts\activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the Website:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## Directory Structure

```
Ecommerce-Website/
|-- ecommerce/              # Main Django application
|-- store/                  # Files related to the project
|-- static/                 # Static files (CSS, JS, images)
    |-- middelwares/
    |-- models/             # Models for database tables
    |-- templates/          # HTML files
    |-- templatetags/       # Filters used in the project
    |-- views/              
|-- manage.py               # Django management script
|-- requirements.txt        # Dependencies
|-- db.sqlite3              # SQLite database
```

---

## System Requirements
- Download the requirements listed in `requirements.txt`

---

## Suggestions
"Suggestions and project improvement ideas are welcomed!"

---

## Contact
- **Name:** Utsavi Hetukkumar Patel
- **Email:** utsavipatel0905@gmail.com
- **GitHub:** [github.com/utsavi_patel09](https://github.com/your-username)
