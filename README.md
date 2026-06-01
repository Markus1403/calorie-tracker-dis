# calorie-tracker-dis
Group project for the course Databases and Information Systems (DIS) at UCPH

This project utilizes Python, Flask with a postgreSQL databse.

### Prerequirements:
It is expected that you already have postgreSQL installed on your device.

# Setup virtual environment 

### Start by installing your virtual environment:
``$ python -m venv .venv``


### Nextup enter your virtual environment:

#### For windows in CMD:
``$ .venv\Scripts\activate``

#### macOS and Linux (the surperior choice):
``$ source .venv/bin/activate``

### Download relevant libraries: 

``$ pip install -r requirements.txt``

### Setup your database

You need to setup a databse for the website to connect to. This assumes youre using linux (Again the surperior choice.)
Start by creating a login role:

``$ sudo -u postgres psql -c "CREATE ROLE calorie_user WITH LOGIN PASSWORD 'YOURPASSWORD HERE';"``

After you've set up your user, create database owned by that user:

``$ sudo -u postgres psql -c "CREATE DATABASE calorie_tracker OWNER calorie_user;"
``

