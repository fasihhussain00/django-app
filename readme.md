# Sample Django App

### Dependecies:
1. ```python```
2. ```pip```

### Steps:
1. ```pip install virtualenv``` Execute this command to install virtual environment
2. ```python -m venv environment``` Execute this command and It must be execute in project directory.
3. ```.\environment\Scripts\activate``` Execute this command to activate Virtual Enviroment.
4. ```pip install -r requirements.txt``` Execute this command to install all project dependencies
5. ```python manage.py runserver``` Execute this command to run app

### DB:

- go to ```{project_directory}/{project_folder}/settings.py``` and change ```DATABASES``` config to your own configuration

### Migrate:
- ```python manage.py makemigrations``` To make migration of new changes
- ```python manage.py migrate``` To apply latest migration on DB
