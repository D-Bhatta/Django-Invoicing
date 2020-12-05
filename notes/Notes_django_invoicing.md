# Notes on Django-Invoicing

Notes and code about Django-Invoicing.

## Sections

- [Notes on Django-Invoicing](#notes-on-django-invoicing)
  - [Sections](#sections)
  - [Notes](#notes)
  - [Setup the project](#setup-the-project)
    - [Create `homepage` view](#create-homepage-view)
      - [Create templates: `base.html`, `dummy.html`, `homepage.html`](#create-templates-basehtml-dummyhtml-homepagehtml)
      - [Create static assets](#create-static-assets)
      - [Create `homepage` view](#create-homepage-view-1)
    - [Configure tests](#configure-tests)
    - [Create tests](#create-tests)
    - [Prep remote and local databases](#prep-remote-and-local-databases)
    - [Integrate PostgreSQL in settings](#integrate-postgresql-in-settings)
  - [Add remote DB info to TravisCI config](#add-remote-db-info-to-travisci-config)
  - [Deploy Project](#deploy-project)
  - [Additional Information](#additional-information)
    - [Screenshots](#screenshots)
    - [Links](#links)
  - [Notes template](#notes-template)

## Notes

<!-- markdownlint-disable MD024 -->

## Setup the project

### Create `homepage` view

#### Create templates: `base.html`, `dummy.html`, `homepage.html`

- Create basic templates : `base.html`, `dummy.html`, `homepage.html`

```html
{% block header_content %} {% load static %}
<html>
  <meta charset="utf-8" />
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0, user-scalable=yes"
  />
  <link rel="stylesheet" href="{% static 'css/ridge.css' %}" />
  <link rel="stylesheet" href="{% static 'css/ridge-light.css' %}" />
  <head>
    <title>Welcome to Invoicing!</title>
  </head>
  {% endblock header_content %}
</html>

```

```html
{% extends "base.html" %} {% load static %} {% block header_content %}
{{block.super }}
<body>
  <main>
    <vstack spacing="m">
      <vstack spacing="s" stretch="" align-x="center" align-y="center">
        <hstack responsive="" spacing="xl">
          <img
            src="{% static 'img/logo.png' %}"
            alt="logo"
            height="150"
            width="150"
          />
          <h1>Welcome to Invoicing!</h1>
        </hstack>
        <p><i>Your personal Invoicing app!</i></p>
        <p>
          Created by
          <a href="https://d-bhatta.github.io/Portfolio-Main/"
            >Debabrata Bhattacharya</a
          >
        </p>
      </vstack>
      <spacer></spacer>
      <vstack spacing="l">
        <vstack spacing="xs">
          <aside class="pa-s">
            <vstack> </vstack>
          </aside>
        </vstack>
      </vstack>
    </vstack>
  </main>
</body>
{% endblock header_content %}

```

```html
{% extends "base.html" %} {% load static %} {% block header_content %}
{{block.super }}
<head>
  <title>Welcome to Invoicing!</title>
</head>
<body>
  <main>
    <vstack spacing="s" stretch="" align-x="center" align-y="center">
      <h1>Welcome to Invoicing!</h1>
      <p>This is a dummy test page. It will have content shortly</p>
    </vstack>
  </main>
</body>
{% endblock header_content %}

```

#### Create static assets

- Create `static` folders and store assets
- We will be using light theme for this app
- Create a logo and store it in images

#### Create `homepage` view

- Create `homepage` view and render `homepage.html`

```python
def homepage(request):
    return render(request, "homepage.html", {})
```

- Create urls in `django_invoicing.urls`

```python
from django.urls import path

from django_invoicing import views

app_name = "invoicing"

urlpatterns = [path("home/", views.homepage, name="home")]
```

- Include in `django_apps.urls`

```python
"""django_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("invoicing/", include("django_invoicing.urls", namespace="invoicing")),
]
```

### Configure tests

- Create a `conftest.py` file
- Copy `base.html` to each `templates/` directory temporarily

```python
from os import remove
from shutil import copy, rmtree


def pytest_configure():
    copy(
        "django_invoicing/django_apps/templates/base.html",
        "django_invoicing/django_invoicing/templates/",
    )


def pytest_unconfigure():
    remove("django_invoicing/django_invoicing/templates/base.html")
```

### Create tests

- Create tests for the `home` view

```python
""" Tests for 'invoicing' app """
import pytest
from django.urls import reverse
from django_apps.utils import get_logger

lg = get_logger()

# This is supposed to fail
def test_helloworld():
    assert True == True


def test_view_homepage(client):
    url = reverse("invoicing:home")
    response = client.get(url)
    assert response.status_code == 200
```

### Prep remote and local databases

- Sign into pgAdmin for local and create a database
- Create a new role with access to the db
- Sign into local server with psql
- Create a new schema
- Create a table to test it out
- Sign into remote server with psql
- Create a new schema
- Create a table to test it out

### Integrate PostgreSQL in settings

- Add settings for connecting to a PostgreSQL backend in `settings.py`
- Test with ``env`` vars for local and remote DB servers

```python
try:
    DJANGO_ENVIRONMENT = os.environ["DJANGO_ENVIRONMENT"]
    DJANGO_HOST_NAME = os.environ["DJANGO_HOST_NAME"]
    DBNAME = os.environ["DBNAME"]
    DBUSER = os.environ["DBUSER"]
    DBPASSWORD = os.environ["DBPASSWORD"]
    DBHOST = os.environ["DBHOST"]
    DBPORT = os.environ["DBPORT"]

except KeyError:
    path_env = os.path.join(BASE_DIR.parent, ".env")
    dotenv.read_dotenv(path_env)
    DJANGO_ENVIRONMENT = os.environ["DJANGO_ENVIRONMENT"]
    DJANGO_HOST_NAME = os.environ["DJANGO_HOST_NAME"]
    DBNAME = os.environ["DBNAME"]
    DBUSER = os.environ["DBUSER"]
    DBPASSWORD = os.environ["DBPASSWORD"]
    DBHOST = os.environ["DBHOST"]
    DBPORT = os.environ["DBPORT"]
```

```python
#
# Settings for PostgreSQL
#
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DBNAME,
        "USER": DBUSER,
        "PASSWORD": DBPASSWORD,
        "HOST": DBHOST,
        "PORT": DBPORT,
    }
}
```

## Add remote DB info to TravisCI config

- Install `travis` gem using    ```❯ gem install travis```
- Log into travis with ```❯ travis login --pro --github-token  token```
- Add the DB information using

    ```bash
    travis encrypt --pro DBNAME="name"  --add

    travis encrypt --pro DBUSER="user"  --add

    travis encrypt --pro DBPASSWORD="password"  --add

    travis encrypt --pro DBHOST="host"  --add

    travis encrypt --pro DBPORT="port"  --add

    ```

- There should be no space between the var name and the = and the value
- Push to TravisCI

## Deploy Project

- Create a `requirements.txt`. Heroku will use this file to install python dependencies, and recognise the project as a python project.

```requirements.txt
black==20.8b1
coveralls==2.1.2
cryptography==3.1.1
Django==3.1.2
django-dotenv==1.4.2
django-heroku==0.3.1
django-upload-validator==1.1.5
djangorestframework==3.12.1
Flask==1.1.2
grip==4.5.2
gunicorn==20.0.4
opencv-python==4.4.0.44
pip==20.2.4
pre-commit==2.7.1
psycopg2==2.8.6
pytest==6.1.1
pytest-cov==2.10.1
pytest-django==4.1.0
pytest-pythonpath==0.7.3
setuptools==50.3.2
social-auth-app-django==4.0.0
tox==3.20.1
twine==3.2.0
wheel==0.35.1
```

- Create a `Procfile` to deploy to Heroku. It will call the `gunicorn` server to start a worker for the app.
- Gunicorn requires a `pythopath` if the project files aren't in the same directory.

```Procfile
web: gunicorn --pythonpath django_invoicing django_apps.wsgi --log-file -

```

- Create a `runtime.txt`. It will tell Heroku what python runtime to use.

```txt
python-3.8.6
```

- Install `django-heroku`, `whitenoise` and `gunicorn`
- Install `heroku plugins:install heroku-repo` for resetting repos
- Install `heroku plugins:install heroku-config` for setting env vars
- Create the `static` files directory in the `BASE` directory with an `emptyfile.txt` file.
- Add them to requirements files in `requirements_dev.txt` and `requirements.txt`
- Add middleware and call `django_heroku.settings(locals())` in `settings.py`

```python
try:
    path_env = os.path.join(BASE_DIR.parent, ".env")
    dotenv.read_dotenv(path_env)
except (EnvironmentError, FileNotFoundError):  # Catch FileNotFoundError
    print("Couldn't retrieve the environment variables")

try:
    path_env = os.path.join(BASE_DIR.parent, ".env")
    dotenv.read_dotenv(path_env)  # Catch FileNotFoundError
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
except (KeyError, FileNotFoundError):
    path_env = os.path.join(BASE_DIR.parent, ".env")
    utils.generate_secret_key(path_env)
    dotenv.read_dotenv(path_env)
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
```

```python
if DJANGO_ENVIRONMENT == "PRODUCTION":
    ALLOWED_HOSTS = [DJANGO_HOST_NAME]
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "django_apps/static/django_apps"),
        # os.path.join(BASE_DIR, "django_invoicing/static/django_invoicing"),
    ]
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
elif DJANGO_ENVIRONMENT == "DEVELOPMENT":
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "django_apps\\static\\django_apps"),
        # os.path.join(BASE_DIR, "django_invoicing\\static\\django_invoicing"),
    ]
    ALLOWED_HOSTS = []
else:
    pass
```

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Add whitenoise middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "django_apps/templates/")
        ],  ## Add base templates directory
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]
```

```python
# Keep this at the end

if DJANGO_ENVIRONMENT == "PRODUCTION":
    django_heroku.settings(locals())
```

- Create heroku app with `heroku create d-djangoapps-1`
- Confirm that a remote named heroku has been set with `git remote -v`
- Set Env vars with `heroku config:push --file=env\r.env`
- Set `heroku config:set DEBUG_COLLECTSTATIC=1`
- Push code with `git push heroku setup:master`
- Check logs with `heroku logs --tail`

## Additional Information

### Screenshots

### Links

## Notes template

```python
```

```html

```
