# Setup authentication

- Setup authentication
- Show user stuff in homepage only if logged in

## Main tasks

- Create an `users` app
- Add authentication urls
- Add authentication templates
- Refactor homepage to show user stuff only if logged in

## Create an `users` app

- Create a `users` app with `python.exe manage.py startapp users`
- Disable password validators in settings. Just comment them out, leaving an empty list
- Create a superuser with `python manage.py createsuperuser`
- In homepage display the current user's username and set a default with `{{ user.username | default:"Guest" }}`
- Run and refactor, write tests, run and refactor

## Add authentication urls

- Add the URLs provided by the Django authentication system into the app urls
- Move the app to the top of the installed apps list
- Run and refactor, write tests, run and refactor

## Add authentication templates

- Create a login page
- Redirect to `homepage` in settings
- Run and refactor, write tests, run and refactor
- Add logout and login links to `homepage`
- Redirect logout to `homepage` in settings
- Run and refactor, write tests, run and refactor
- Create a Change Passwords Pages
- Add a password change link to the `homepage`
- Run and refactor, write tests, run and refactor
- Add email integration
- Run and refactor, write tests, run and refactor
- Create password reset templates
- Run and refactor, write tests, run and refactor
- Include a link to the password reset form on the login page
- Change Email Templates
- Run and refactor, write tests, run and refactor
- Add the email field by inheriting the `UserCreationForm` into `CustomUserCreationForm`  that extends Django’s `UserCreationForm`
- Run and refactor, write tests, run and refactor
- Create a new view called `register`
- Add `register` url to `urls.py`
- Create a template called `register.html`
- Add registration url to `login.html` template
- Run and refactor, write tests, run and refactor
- Add Login h2 header

## Refactor homepage to show user stuff only if logged in

- Refactor homepage to hide stuff unless logged in
- Run and refactor, write tests, run and refactor

## Fix register

- Fix login button text on `register` page

## Email reset

- Test email reset
- Create template for password reset confirmation `password_reset_confirm.html`
- Create template for password reset complete `password_reset_complete.html`
