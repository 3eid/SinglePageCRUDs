# DjangoSimpleCRUDs
Simple CRUD operations project using Django Framework

This is a simple CRUD (Create, Read, Update, Delete) application built using Django framework. It allows managing a list of Branches with basic information in one single page with a navigator.

## Live Demo
https://singlepagecruds.pythonanywhere.com/

## Screenshots
Home Page (Make all the CRUDs operations):
![Home Page (List Persons)](Documentation/Home.png)



## Installation:

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/3eid/DjangoSimpleCRUDs

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Apply migrations to create the database schema:
   ```bash
   python manage.py migrate
4. Create a superuser for accessing the admin interface:
   ```bash
   python manage.py createsuperuser
5. Run the development server:
   ```bash
   python manage.py runserver
6. Access the application in your browser at http://localhost:8000




## Admin Interface
You can access the admin interface at http://localhost:8000/admin/ with the superuser credentials (username: *admin* , password: *admin*). This interface allows managing persons directly through a user-friendly interface.