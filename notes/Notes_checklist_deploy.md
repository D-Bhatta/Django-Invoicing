# Deploy project

- Create Heroku account
- Deploy project

## Main tasks

- Create Heroku account
- Follow tutorial [here](https://devcenter.heroku.com/articles/getting-started-with-python) and [here](https://devcenter.heroku.com/categories/python-support)

## Create heroku account

- Create account
- Perform setup on local machine
- Create plan to setup heroku

## Setup Heroku for project

- Create a `requirements.txt`
- Create a `Procfile`
- Create a `runtime.txt`
- Install `django-heroku`, `whitenoise` and `gunicorn`
- Install `heroku plugins:install heroku-repo` for resetting repos
- Install `heroku plugins:install heroku-config` for setting env vars
- Create the static files directory in the base directory with an empty file.
- Add them to requirements files
- Add middleware and call `django_heroku.settings(locals())` in settings
- Create heroku app with `heroku create django_invoicing`
- Update `wsgi.py` file
- Confirm that a remote named heroku has been set with `git remote -v`
- Create the static files directory
- Set Env vars
- Set `heroku config:set DEBUG_COLLECTSTATIC=1`
- Push code with `git push heroku setup:master`
