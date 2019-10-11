# Flask-RESTful API project structure

This project shows one of the possible ways to structure a Flask RESTful Api App.

## Getting Started

### Setup and Installation:
- Make sure you have [Python2.7+/Python3.x](https://www.python.org/) installed on your system.
- Make sure [pip](https://pypi.org/project/pip/) is installed on your system.
- Make sure [virtualenv](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv) is installed on your system.

### Core packages used in this project:
Packages  | Description
--------- | -------------
[Flask-Migrate](https://flask-restful.readthedocs.io/en/latest/index.html) | Handling all database migrations
[Flask-RESTful]() | RESTful API library
[Flask-Script]() | Provides support for writing external scripts
[Flask-SQLAlchemy]() | Adds support for SQLAlchemy ORM
[Alembic](https://pypi.org/project/alembic/) | Database migrations tool
[Flask-marshmallow](https://pypi.org/project/flask-marshmallow/) | Flask + marshmallow for beautiful APIs
[marshmallow](https://pypi.org/project/marshmallow/) | ORM/ODM/framework-agnostic library for converting complex datatypes
[marshmallow-sqlalchemy](https://pypi.org/project/marshmallow-sqlalchemy/) | SQLAlchemy integration with the marshmallow (de)serialization library
[SQLAlchemy](https://pypi.org/project/SQLAlchemy/) | The Python SQL Toolkit and Object Relational Mapper


### Project structure:
```
├── app
│   ├── __init__.py
│   ├── api      
│   │   ├── __init__.py
│   │   └── ...
│   ├── models
│   │   ├── __init__.py
│   │   └── ...
│   ├── utils
│   │   ├── __init__.py
│   │   └── ...
│   ├── __init__.py
│   ├── app.py
├── migrations
│   └── ...
├── tests
│   └── ...
├── .gitignore
├── config.py
├── manage.py
├── migrate.py
├── README.md
└── requirements.txt
```

- ```app/utils/``` consists of utils classes, helpers and functions that are useful for all the modules.
- ```app/api/``` contains all the controllers/resources for every API endpoints.
- ```app/models/``` contains all the database models.
- ```app/app.py``` is the main entry point of the Flask app.
- ```migrations/``` contains all the migration from running script such as init, migrate and upgrade.
- ```config.py``` will storing all the configuration for different environments (developent, test, staging and prod).
- ```manage.py``` will be used to launch the server locally.
- ```migrate.py``` contains useful scripts (run, initdb, testing, list routes, etc) using Flask-Script.
- ```tests/``` write unit tests for models or integration tests for the different API endpoints.
- ```requirements.txt``` contains all the python dependencies that install using pip.  
  ``` 
  pip install -r requirements.txt 
  ```

## Usage 

1. Clone the repository.
2. ```pip install -r requirements.txt```
3. Run following commands:
    1. ```python manage.py db init```
    2. ```python manage.py db migrate```
    3. ```python manage.py db upgrade```
4. Start server by running ```python manage.py```

