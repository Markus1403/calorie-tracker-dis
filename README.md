# calorie-tracker-dis
Group project for the course Databases and Information Systems (DIS) at UCPH

This project utilizes Python, Flask with a postgreSQL databse.

### Prerequirements:
It is expected that you already have postgreSQL installed on your device.

# E/R-Model:
<img width="7013" height="5296" alt="Entity-relationship (ER) Diagram (Community)" src="https://github.com/user-attachments/assets/da18c0e0-99eb-4bd6-a6bc-dce598638ebd" />

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

You need to setup a databse for the website to connect to. This assumes youre using linux (Again the superior choice.) or macOS.

Start by creating a login role:

``$ sudo -u postgres psql -c "CREATE ROLE calorie_user WITH LOGIN PASSWORD 'YOURPASSWORDHERE';"``

After you've set up your user, create database owned by that user:

``$ sudo -u postgres psql -c "CREATE DATABASE calorie_tracker OWNER calorie_user;"``

After youve done this, you can now add your postgress link to your .env file. See .env.example for formatting. If youve named your user calorie_user you should only need to update the YOURPASSWORDHERE part of the username. 

### Create the database tables

The steps above only create an *empty* database. You still need to build the tables from the migrations, otherwise the app crashes with an Internal Server Error on the very first request (`relation "users" does not exist`). Run:

``$ flask db upgrade``

This applies the existing migrations and creates all the tables. You only need to do this once (and again whenever new migrations are added). After that you can start the server:

``$ python run.py``

# Deklaration for anvendelse af generative AI-værktøjer

☒ Jeg/vi har benyttet generativ AI som hjælpemiddel/værktøj

☐ Jeg/vi har IKKE benyttet generativ AI som hjælpemiddel/værktøj

## Oplist, hvilke GAI-værktøjer der er benyttet, inkl. link til platformen

* Claude (Anthropic): https://claude.com/

## Beskriv hvordan generativ AI er anvendt i opgaven

### 1) Formål (hvad har du/I brugt værktøjet til)

* Hjælp til Styling i CSS
* Hjælp til HTML

### 2) Arbejdsfase (hvornår i arbejdsprocessen har du/I brugt GAI)

* Under udviklingen af applikationen.

### 3) Hvad gjorde du/I med outputtet (herunder også, om du/I har redigeret outputtet og arbejdet videre med det)

* Outputtet blev brugt i det endelige produkt.


