## django notes

### create new project
`django-admin startproject my-app`

### start server on localhost
* `python3 manage.py runserver`
* `$HOME/env/bin/python3 manage.py runserver`

### create virtual environment (optional but recommended)
Used to create and manage separate environments for projects. Allows use of different python versions for each project.

To install:

* `pip3 install virtualenv`
* `$HOME/env/bin/pip3 install virtualenv`

To create venv folder in project directory:\
`virtualenv venv`

To activate environment:\
`source venv/bin/activate`

To deactivate:\
`deactivate`

### create new app
Used to break functionality into smaller apps; small library representing one part of project.

`python3 manage.py startapp <plural app name>`

### make migrations
1. `python3 manage.py makemigrations` (create migration)
2. `python3 manage.py migrate` (push changes to db)

### django admin site (optional)
Reads metadata from your models and trusted users can manage content on site.

Create superuser:\
`python3 manage.py createsuperuser`

