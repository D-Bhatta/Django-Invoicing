# App checklist

Logs you in. Saves data in a PostgreSQL DB. Displays a dashboard. Enables setting up default values for the various fields. Shows a form that can be filled in. saves as html. prints to pdf. invoices page where invoices are shown.

## Main tasks

- Create checklists
- Setup project with PostgreSQL
- Deploy project
- Create a `Homepage`
- Setup authentication
- Create `Settings` page
- Create `Create Invoice` page
- Create `Print to PDF` Function
- Create `Download` page
- Create `Invoices Dashboard` page

## Create checklists

- Create checklists for each task
- Setup issues

## Setup project with PostgreSQL

- Setup the project
- Add mock fixtures
- Integrate with PostgreSQL

## Deploy project

- Create Heroku account
- Deploy project

## Create a `Homepage`

- Create a `homepage` page
- Add mock links
- Refactor links into real ones

## Setup authentication

- Setup authentication
- Show user stuff in homepage only if logged in

## Create `Settings` page

- Let user specify field names in a form

## Create `Create Invoice` page

- Create form for invoice
- Retrieve defaults unless values are specified
- Allow to select if stuff will be printed to invoice or just stored
- Show invoice as HTML

## Create `Print to PDF` Function

- Create a Print to PDF button
- Convert html to pdf if no pdf exists

## Create `Invoices Dashboard` page

- Create an invoices page with index of all invoices

## Future enhancements

### Change username

- Create a change username form in settings

### Change email

- Create a change email form in settings

### Move away from travis CI to GitHub Actions

- Change CI to GitHub Actions
