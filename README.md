# Road Safety Management System

A web-based application built with **Django, HTML, CSS, JavaScript, and SQLite** that promotes
road safety by giving users traffic rules, road sign explanations, safety tips, emergency contact
numbers, and a way to report road hazards or accidents.

## Features

- **User registration & secure login** — Django's built-in auth system, extended with a custom
  `Profile` (phone number, role: driver/rider/pedestrian/cyclist, city).
- **Traffic rules section** — searchable list of rules with typical penalties.
- **Traffic signs & symbols guide** — mandatory, cautionary, and informatory signs, filterable by category.
- **Safety tips** — targeted advice for drivers, riders, pedestrians, cyclists, or everyone, filterable by audience.
- **Hazard / accident reporting** — logged-in users can submit reports with location, type, severity,
  description, and an optional photo. Full CRUD: users can edit or delete their own reports.
  All reports are also manageable from the Django admin (status workflow: pending → verified →
  in progress → resolved/rejected).
- **Emergency contact directory** — police, ambulance, fire, highway helpline, women's helpline, etc.
- **User dashboard** — update your profile and see/manage all reports you've submitted.
- **Responsive design** — works on desktop, tablet, and mobile.

## Tech Stack

| Layer      | Technology              |
|------------|--------------------------|
| Backend    | Python 3.10+, Django 5.0 |
| Database   | SQLite (default — zero setup) |
| Frontend   | HTML5, CSS3 (custom, no framework), vanilla JavaScript |
| Image handling | Pillow (for uploaded hazard photos / sign images) |

> Want MySQL instead of SQLite? See the commented-out config block in `road_safety/settings.py`
> under `DATABASES` — swap it in and run `pip install mysqlclient`.

## Project Structure

```
road_safety_system/
├── requirements.txt
└── road_safety/
    ├── manage.py
    ├── db.sqlite3                  (created after first migrate)
    ├── road_safety/                # project config
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    └── core/                       # main app
        ├── models.py                # Profile, TrafficRule, TrafficSign, SafetyTip,
        │                            # EmergencyContact, HazardReport
        ├── forms.py                  # SignUpForm, HazardReportForm, ProfileUpdateForm...
        ├── views.py                  # all page logic (function + class-based views)
        ├── urls.py                   # app routes
        ├── admin.py                  # admin panel registration
        ├── signals.py                 # auto-creates Profile on user creation
        ├── management/commands/seed_data.py   # loads sample rules/signs/tips/contacts
        ├── templates/core/...         # all page templates
        ├── templates/registration/... # login & signup templates
        └── static/core/{css,js}/      # stylesheet & JS
```

## Setup Instructions

1. **Clone/unzip the project**, then move into it:
   ```bash
   cd road_safety_system/road_safety
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r ../requirements.txt
   ```

4. **Run migrations** to create the database:
   ```bash
   python manage.py migrate
   ```

5. **Load sample content** (traffic rules, signs, tips, emergency contacts) so the site isn't empty:
   ```bash
   python manage.py seed_data
   ```

6. **Create an admin account**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. Open your browser at **http://127.0.0.1:8000/**
   Admin panel is at **http://127.0.0.1:8000/admin/**

## Using the Admin Panel

Log in at `/admin/` with your superuser account to:
- Add/edit traffic rules, signs, safety tips, and emergency contacts (the seed command gives you
  a starting set — edit or add to them freely).
- Review hazard reports submitted by users and update their status (e.g. mark as Verified or Resolved).
- Manage user profiles and roles.

## Notes & Possible Extensions

- Photo uploads for hazard reports and traffic sign images are stored under `media/` — this folder
  is git-ignored by default; in production you'd serve media via a proper file/object store.
- `DEBUG = True` and `SECRET_KEY` in `settings.py` are fine for local development only — change
  both before deploying anywhere public.
- Natural next features: email notifications when a report's status changes, a map view for hazard
  locations (e.g. via Leaflet/Google Maps), and a public REST API (Django REST Framework) for a
  future mobile app.

## License

Free to use and modify for academic, portfolio, or learning purposes.
