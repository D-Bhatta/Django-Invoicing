# Setup project with PostgreSQL

- Setup the project
- Add mock fixtures
- Integrate with PostgreSQL

## Main tasks

- Create templates: `base.html`, `dummy.html`, `homepage.html`
- Create static assets
- Create `homepage` view
- Delete all tables in `test_main`
- Delete all tables in `elephantsql1` db
- Integrate local PostgreSQL in settings
- Integrate remote PostgreSQL in settings

## Create templates: `base.html`, `dummy.html`, `homepage.html`

- Create basic templates : `base.html`, `dummy.html`, `homepage.html`
- Change structure according to app requirements

## Create static assets

- Create `static` folders and store assets
- Create a logo and store it in images
- Modify `base.html` to use logo in header

## Create `homepage` view

- Create `homepage` view
- Create urls
- Run and refactor
- Write tests
- Run and refactor

## Delete all tables in `test_main`

- Delete all tables in `test_main` db
- Prep db for use
- Run and refactor

## Delete all tables in `elephantsql1` db

- Delete all tables in db
- Prep db for use
- Run and refactor

## Integrate local PostgreSQL in settings

- Change settings to use PostgreSQL instead of SQLite
- Add local PostgreSQL in settings to `.env`
- Run and refactor

## Integrate remote PostgreSQL in settings

- Add remote PostgreSQL in settings to `.env`
- Add the DB information to `.travis.yml`
- Run and refactor
