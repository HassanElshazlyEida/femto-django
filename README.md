# Personal Finance Web App

This is a personal finance web application built using Django, Django REST Framework. The app allows users to set saving goals and calculates the monthly deposit needed to reach those goals.

## Features

- User Registration and Authentication: Users can register and login to their accounts to access the app's features.
- Saving Goal Management: Users can create, view, and manage their saving goals.
- Monthly Deposit Calculation: The app calculates the monthly deposit amount required to reach the saving goals based on the total amount and the goal date.
- User-Friendly Interface: The app provides an intuitive and user-friendly interface for a smooth user experience.

## Installation

1. Clone the repository: `git clone <repository-url>`
2. Create and activate a virtual environment: `python3 -m venv env` and `source env/bin/activate`
3. Install the dependencies: `pip install -r requirements.txt`
4. Set up the database: Update the database settings in the `settings.py` file and run migrations using `python manage.py migrate`

## Usage

1. Start the development server: `python manage.py runserver`
2. Access the web app in your browser at `http://localhost:8000`
3. Register a new account or login with an existing account.
4. Create saving goals by specifying the total amount to be saved and the goal date.
5. View and manage your saving goals on the home page.



## Technologies Used

- Django: Web framework for building the backend of the application.
- Django REST Framework: Enables building RESTful APIs in Django.
- SQL Lite: Database system for storing user and goal data.

## Credits

This project is developed by [Hassan Elshazly Eida](http://linkedin.com/in/hassanelshazlyeida). Feel free to contribute and make improvements.

