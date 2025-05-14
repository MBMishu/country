<h1 align="center" id="title">🌍 Country Information Dashboard</h1>

<p id="description">A Django-based web application that provides detailed information about countries including capital population region languages timezones and more. It also allows users to explore countries by region and language.</p>

<p align="center"><img src="https://img.shields.io/badge/django-Rest_Api-blue" alt="shields"></p>

<h2>🚀 Demo</h2>

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

<h2>Project Screenshots:</h2>

<img src="https://github.com/MBMishu/country/blob/main/banner.png" alt="project-screenshot">

<h2>🧐 Features</h2>

Here're some of the project's best features:

- View comprehensive details of countries.
- Explore countries by region and language.
- Interactive UI with DataTables and Venobox for enhanced user experience.
- Secure API endpoints with token-based authentication.

<h2>🧰 Prerequisites</h2>

Ensure you have the following installed on your system:

- Python 3.6 or higher: Check with python3 --version.

- Git: Verify with git --version.

- pip: Confirm with pip --version.

- Virtual environment tool: venv comes with Python 3. If using virtualenv, install it via pip install virtualenv.

<h2>🛠️ Installation Steps:</h2>

<p>Clone the Repository</p>

```
git clone https://github.com/MBMishu/country.git
```

```
cd country
```

<h2>Create a Virtual Environment</h2>

- Linux/macOS:

```
python3 -m venv env
```

```
source env/bin/activate
```

- Windows:

```
python -m venv env
```

```
env\Scripts\activate
```

<h2>Install Dependencies</h2>

```
pip install -r requirements.txt
```

<h2>Apply Migrations (Set Up the Database)</h2>

I have used Postgresql Database for this project. All you have to do just open pgAdmin and create new Database called country.

```
python manage.py makemigrations
```

```
python manage.py migrate
```

<h2>Create a Superuser (Optional for admin access)</h2>

```
python manage.py createsuperuser
```

<h2> Run the Server</h2>

```
python manage.py runserver
```

Now open your browser and go to:

```
http://127.0.0.1:8000/
```

<h2>💻 Built with</h2>

Technologies used in the project:

- Django
- Restful Api
- PostgreSQL
- Bootstrap 4

<h2>📘 API Documentation</h2>

[👉 Click To View API Documentation on Postman](https://documenter.getpostman.com/view/16581078/2sB2qUnjZS)

This documentation includes:

- Fetching Data and store them
- List of All countries
- Create new Country entry
- Update Exiting Country Entry
- Delete Exiting Country Entry
- Retrieve a specific Country Details
- Search By country Name / Partially Also
- Same Region country List
- Same Spoken Language Cuntry List
