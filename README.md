# Django Project

This is a basic template for a Django project.

## Getting Started

### Prerequisites
- Python 3.x
- Django

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ofullard/DjangoApp.git
   ```
2. Navigate into the project directory:
   ```bash
   cd DjangoApp
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```
5. Install the required packages:
   ```bash
   pip install django
   ```

### Running the Project
1. Start the development server:
   ```bash
   python manage.py runserver
   ```
2. Visit `http://127.0.0.1:8000/` in your browser.

## Structure
```
DjangoApp/
├── manage.py
├── app_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```