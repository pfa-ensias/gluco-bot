## To install the Diabetes Management Tracking System locally, follow these steps:

1. Clone the repository to your local machine.
2. Install Python 3.8 or newer.
3. Run `pip install -r requirements.txt` to install required packages.
4. Update `DEBUG = False` to `DEBUG = True` in `/djangoProject/settings.py` file.
5. Migrate the database by running python `python manage.py makemigrations`  `python manage.py migrate` in your terminal. If required tables were not generated, run `python manage.py migrate --run-syncdb` as needed.
6. Load the initial datasets for **Food** and **Exercise** calories lookup tables by running `python dbinitialload.py`. (This is only needed on first run.)
7. Start the server by running `python manage.py runserver` in your terminal.

## To use the Diabetes Management Tracking System, follow these steps:

1. Create an account by clicking on the "Register" button on the login page.
2. Log in to the system using your username and password.
3. Start tracking your blood glucose levels, doctor appointment, and physical activity by clicking on the relevant buttons in the top nav bar.
4. View your records in the dashboard and view list page.
5. Get alert if the appointment is approaching within 7 days.
6. Access education content regarding diabetes.


### For application production depolyment online, please refer to the [Startup and Configuration Files.md](./Startup%20and%20Configuration%20Files.md).