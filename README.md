# Python - Django Rest Framework boilerplate

This is boilerplate for starting fresh new DRF projects. It's built using [cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest).

## Highlights

- Modern Python development with Python 3.8+
- Bleeding edge Django 3.1+
- Fully dockerized, local development via docker-compose.
- PostgreSQL
- Full test coverage, continuous integration, and continuous deployment.
- Celery tasks

### Features built-in

- JSON Web Token authentication using [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- Social (FB + G+) signup/sigin
- API Throttling enabled
- Password reset endpoints
- User model with profile picture field using Easy Thumbnails
- Files management (thumbnails generated automatically for images)
- Sentry setup
- Swagger API docs out-of-the-box
- CodeLinter (flake8) and CodeFormatter (yapf)
- Tests (with mocking and factories) with code-coverage support

## API Docs

API documentation is automatically generated using Swagger. You can view documention by visiting this [link](http://localhost:8000/swagger).

## Prerequisites

If you are familiar with Docker, then you just need [Docker](https://docs.docker.com/docker-for-mac/install/). If you don't want to use Docker, then you just need Python3 and Postgres installed.

## Local Development with Docker

Start the dev server for local development:

```bash
cp .env.dist .env
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

## Local Development without Docker

### Install

```bash
python3 -m venv env && source env/bin/activate                # activate venv
cp .env.dist .env                                             # create .env file and fill-in DB info
pip install -r requirements.txt                               # install py requirements
./manage.py migrate                                           # run migrations
./manage.py collectstatic --noinput                           # collect static files
redis-server                                                  # run redis locally for celery
celery -A src.config worker --beat --loglevel=debug
  --pidfile="./celerybeat.pid"
  --scheduler django_celery_beat.schedulers:DatabaseScheduler # run celery beat and worker
```

### Run dev server

This will run server on [http://localhost:8000](http://localhost:8000)

```bash
./manage.py runserver
```

### Create superuser

If you want, you can create initial super-user with next commad:

```bash
./manage.py createsuperuser
```

### Running Tests

To run all tests with code-coverate report, simple run:

```bash
./manage.py test
```


You're now ready to ROCK! ✨ 💅 🛳
