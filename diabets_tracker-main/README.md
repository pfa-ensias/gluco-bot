# **Diabetes Management Tracking System**

The Diabetes Management Tracking System is a web-based application that helps individuals with diabetes to track their blood glucose levels, diet, physical activity, doctor appointment and other health data. The system is designed to provide a simple and intuitive interface for users to manage their diabetes and improve their health outcomes.

## Features

User authentication: Users can create an account and log in to the system to access their personal health data.
Blood glucose tracking: Users can record their blood glucose levels and view their data in a graph or table format.
Medication tracking: Users can log their medication and set reminders for when to take it.
Physical activity tracking: Users can track their exercise and physical activity levels.
Dashboard: Users can view their health data in a personalized dashboard that displays their progress and trends over time.


## To install the Diabetes Management Tracking System locally, follow these steps:

1. Clone the repository to your local machine.
2. Install Python 3.8 or newer.
3. Run `pip install -r requirements.txt` to install required packages.
4. Update `DEBUG = False` to `DEBUG = True` in `/djangoProject/settings.py` file.
5. Migrate the database by running python `python manage.py makemigrations`  `python manage.py migrate` in your terminal. If required tables were not generated, run `python manage.py migrate --run-syncdb` as needed.
6. Load the initial datasets for **Food** and **Exercise** calories lookup tables by running `python dbinitialload.py`. (This is only needed on first run.)
7. Start the server by running `python manage.py runserver` in your terminal.
To install the Diabetes Management Tracking System, follow these steps:

* Clone the repository to your local machine.
* Migrate the database by running python `manage.py migrate` in your terminal.
* Start the server by running `python manage.py runserver` in your terminal.


## Usage

To use the Diabetes Management Tracking System, follow these steps:

* Create an account by clicking on the "Register" button on the login page.
* Log in to the system using your username and password.
* Start tracking your blood glucose levels, doctor appointment, and physical activity by clicking on the relevant buttons in the top nav bar.
* View your records in the dashboard and view list page.
* Get alert if the appointment is approaching within 7 days.
* Access education content regarding diabetes.
