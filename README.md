# bloggers_haven

Bloggers Haven
This guide will help you set up and run the project on your computer.

# Prerequisites

Before starting, make sure your computer has following installed:

1. Python (https://www.python.org/downloads/)
2. During installation, make sure to check the box that says "Add Python to PATH".(Important step)

# Download the project

<!-- Option A -->

1. Open command prompt.
2. Use the `cd` command to enter the folder where you want this project
3. Clone the project repository:
   git clone https://github.com/anushka155/bloggers_haven.git

4. Go inside the project folder:
   cd bloggers_haven

<!-- Option B -->

Option B: Download ZIP

1. Go to the GitHub repository
2. Download ZIP
3. Extract the ZIP file anywhere you like
4. Open Command Prompt or Terminal and navigate to the extracted folder:
   cd path\to\bloggers_haven

# Set Up a Virtual Environment

1. Create a virtual environment:
   py -m venv .venv
2. Activate the virtual environment:
   .venv\Scripts\activate

# Install Dependencies

This will install Django and other necessary packages.
pip install -r requirements.txt

# Apply Database Migrations

Django uses a database to store your data. Run these commands to set it up:
py manage.py makemigrations
py manage.py migrate

# To create Admin Account

This allows you to log in to the admin panel. Follow the prompts to create a username, email, and password.
python manage.py createsuperuser

# Run the Local Server

python manage.py runserver

Open your browser and go to: localhost:8000
To access the admin panel: localhost:8000/admin
