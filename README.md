# 🌐 Django Lab 1: Personal Profile Page

This is a simple Django project for **Day 1 Task**: building a personal profile page using function-based views, templates, URL routing, context data, and static files (CSS & JavaScript).

---

## Features

- Function-based view that displays a name, bio, and list of skills.
- HTML template renders profile details using Django template variables.
- Skills are displayed using a `{% for %}` loop.
- A "Say Hello" button triggers a JavaScript alert.
- Styled using an external CSS file.
- Static files are managed with Django’s `{% static %}` tag.

---

## Tech Stack

- Python 3.13
- Django 5.2.4
- HTML5, CSS3, JavaScript
- PyCharm (recommended IDE)

---

## How to Run the Project

### 1. Clone or Download

```bash
git clone <repository-url>
cd Django_Lab1
```

Or just download the ZIP and extract it.

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Django

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. View in Browser

Go to:  
[http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)

---

## Project Structure

```
Django_Lab1/
├── manage.py
├── mysite/
│   └── settings.py, urls.py, ...
├── profile_app/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── profile.html
│   └── static/
│       └── profile_app/
│           ├── style.css
│           └── script.js
```

---

## 👤 Author

# **Tasneem Mohamed**  
