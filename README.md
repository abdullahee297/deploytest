🚀 Django Deployment on Vercel (Complete Guide)

This project demonstrates how to deploy a Django application on Vercel using:

api/index.py as the entry point
WhiteNoise for static files
SQLite database (default)
📁 Project Structure
project/
│
├── api/
│   └── index.py
│
├── pdfhandling/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── manage.py
├── vercel.json
├── build.sh
├── requirements.txt
⚙️ 1. API Entry Point (api/index.py)

This file is REQUIRED for Vercel to run Django.

import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pdfhandling.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
⚙️ 2. Django Settings (settings.py)
✅ Important Configurations
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ["*"]
📦 Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pdfapp',
]
🧩 Middleware (WhiteNoise MUST be here)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
📁 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
    }
]
🗄️ Database (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
🎨 Static Files (IMPORTANT)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
⚡ 3. Install WhiteNoise
pip install whitenoise
🧪 4. Collect Static Files

Run this before deployment:

python manage.py collectstatic --noinput

👉 This creates:

staticfiles/
🚀 5. Vercel Configuration (vercel.json)
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ]
}
🔧 6. Build Script (build.sh)

Used to install dependencies + collect static files.

#!/bin/bash

pip install -r requirements.txt
python manage.py collectstatic --noinput
📄 7. Requirements (requirements.txt)

Example:

Django>=5.2
whitenoise
gunicorn
🌐 8. Template Usage (IMPORTANT)

Always load static like this:

{% load static %}

<link rel="stylesheet" href="{% static 'style.css' %}">
🚀 9. Deployment Steps
Step 1: Push to GitHub
git add .
git commit -m "deploy setup"
git push origin main
Step 2: Import into Vercel
Go to https://vercel.com
Import GitHub repo
Select project
Step 3: Deploy 🎉
