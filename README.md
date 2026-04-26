# 🚀 Django QR Generator (Vercel Deployment)

![Django](https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A Django-based QR Generator web app deployed on Vercel using WhiteNoise for static files.

---

# 🌐 Live Demo
https://your-project-link.vercel.app

---

# 📸 Preview

## Home Page
![Home Page](https://via.placeholder.com/1000x500.png?text=Home+Page+Screenshot)

## QR Generator UI
![QR Generator](https://via.placeholder.com/1000x500.png?text=QR+Generator+UI)

---

# 📁 Project Structure

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
├── pdfapp/
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

---

# ⚙️ Features
- QR code generation from text/links  
- Simple UI  
- Django backend  
- Vercel deployment  
- WhiteNoise static handling  

---

# 🧠 Key Files

## api/index.py
```python
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pdfhandling.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
```

---

## settings.py (important)
```python
DEBUG = False
ALLOWED_HOSTS = ["*"]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

---

## vercel.json
```json
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
```

---

## build.sh
```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
```

---

# 🚀 Deployment Steps
1. Push to GitHub  
2. Import to Vercel  
3. Deploy  

---

# ⚠️ Issues Fix
- Run collectstatic for CSS  
- Ensure WhiteNoise is installed  
- Fix api/index.py entry point  

---

# 👨‍💻 Author
Muhammad Abdullah
