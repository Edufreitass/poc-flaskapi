# POC (Proof of concept) - Flask API

## Initial Config using Git Bash

```shell
$ mkdir poc-flaskapi
$ cd poc-flaskapi/
$ py -m venv .venv
$ source .venv/Scripts/activate
$ py -m pip install --upgrade pip
$ vim .gitignore
$ git init
$ git add .
$ git commit -m "config: initial commit"
$ pip install Flask Flask-SQLAlchemy Flask-Migrate
$ pip freeze > requirements.txt
$ git add .
$ git commit -m "config: add requirements.txt"
$ code .
# after add a minimal Flask application, execute app
$ py run.py
```

### .gitignore content

```
**/__pycache__
.pytest_cache
.venv
.coverage
.idea
htmlcov
```

## Python packages (commands)

```shell
$ pip install Flask
$ pip install -U Flask-SQLAlchemy
$ pip install Flask-Migrate
```

## Flask-Migrate (commands)

```shell
# Create a migration repository with the following command
$ flask db init
# Generate an initial migration
$ flask db migrate -m "Initial migration."
# The migration script also needs to be added to version control. Then you can apply the changes described by the migration script to your database
$ flask db upgrade
# To see all the commands that are available run this command:
$ flask db --help
```