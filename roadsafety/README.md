# 🛡️ Road Safety Management System
**Built by Aman Pradhan — SOA University, Bhubaneswar**

A web-based Django application to promote road safety awareness, report hazards, and access emergency information.

---

## 🚀 How to Run

### Step 1 — Install Python
Make sure Python 3.10+ is installed. Download from https://python.org

### Step 2 — Install Django
Open terminal/command prompt in this folder and run:
```
pip install django
```

### Step 3 — Setup the Database
```
python manage.py makemigrations
python manage.py migrate
```

### Step 4 — Load Sample Data
```
python manage.py loaddata safety/fixtures/initial_data.json
```

### Step 5 — Create Admin Account
```
python manage.py createsuperuser
```
Enter username, email, and password when prompted.

### Step 6 — Run the Server
```
python manage.py runserver
```

### Step 7 — Open in Browser
Visit: **http://127.0.0.1:8000**

Admin panel: **http://127.0.0.1:8000/admin**

---

## 📋 Features
- User Registration & Secure Login
- Traffic Rules (with category filter)
- Traffic Signs & Symbols Guide
- Road Hazard & Accident Reporting
- Emergency Contact Numbers
- Safety Tips for Drivers, Riders & Pedestrians
- Personal Dashboard to track reports
- Admin panel to manage all content

## 🛠️ Tech Stack
- Python, Django, SQLite
- HTML, CSS, JavaScript
- Django Templates & Admin
