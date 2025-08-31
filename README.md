# Healthcare Management System

A Django-based Healthcare Management System with JWT authentication and REST APIs for managing patients, doctors, and users.

**Tech Stack:** Django 5.1.3, Django REST Framework, PostgreSQL, JWT, Python `venv`

---

## Features
- User registration & JWT authentication  
- CRUD operations for patients and doctors  
- REST API endpoints  
- Secure password validation  
- PostgreSQL database integration  

---

## Setup & Installation

1. **Clone repository**
```bash
git clone (https://github.com/Anamika-Singh-23/Healthcare-Backend-Django.git)
cd healthcare
```
2.Create & activate virtual environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```
3.Install dependencies
```bash
pip install -r requirements.txt
```
4.pip install -r requirements.txt
```bash
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```
5.Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
6.Create superuser (optional, for admin panel)
```bash
python manage.py createsuperuser
```
7.Run the server
```bash
python manage.py runserver
```
8.Access:

-Admin panel: http://127.0.0.1:8000/admin/

-API endpoints: http://127.0.0.1:8000/api/


✅ This version uses:
- Proper headings and line breaks  
- Code blocks for commands and `.env`  
- Tables for API endpoints for better readability  
