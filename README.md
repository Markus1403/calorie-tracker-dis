# calorie-tracker-dis
Group project for the course Databases and Information Systems (DIS) at UCPH

This project utilizes Python, Flask with a postgreSQL databse.

### E/R-Model:
<img width="2400" height="1792" alt="image" src="https://github.com/user-attachments/assets/ccc031f3-be83-41fc-ba62-01c88c0bae8c" />

### Prerequirements:
It is expected that you already have postgreSQL installed on your device.

# Setup virtual environment 

### Start by installing your virtual environment:
``$ python -m venv .venv``


### Nextup enter your virtual environment:

#### For windows in CMD:
``$ .venv\Scripts\activate``

#### macOS and Linux (the superior choice):
``$ source .venv/bin/activate``

### Download relevant libraries: 

``$ pip install -r requirements.txt``

### Setup your database

You need to setup a databse for the website to connect to. This assumes youre using linux (Again the superior choice.)
Start by creating a login role:

``$ sudo -u postgres psql -c "CREATE ROLE calorie_user WITH LOGIN PASSWORD 'YOURPASSWORDHERE';"``

After you've set up your user, create database owned by that user:

``$ sudo -u postgres psql -c "CREATE DATABASE calorie_tracker OWNER calorie_user;"
"
``

After youve done this, you can now add your postgress link to your .env file. See .env.example for formatting. If youve named your user calorie_user you should only need to update the YOURPASSWORDHERE part of the username. 

### Create the database tables

The steps above only create an *empty* database. You still need to build the tables from the migrations, otherwise the app crashes with an Internal Server Error on the very first request (`relation "users" does not exist`). Run:

``$ flask db upgrade``

This applies the existing migrations and creates all the tables. You only need to do this once (and again whenever new migrations are added). After that you can start the server:

``$ python run.py``


# TODO

- Add more standardfoods to init.py
- Add calorie profiles
- Add food log to html page
- Finish the TODO list






