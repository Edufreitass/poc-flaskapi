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