from os import environ

import pytest
from django.contrib.auth.models import User


@pytest.fixture
def create_user(db) -> User:
    USERNAME = environ["USERS_LOGIN_USERNAME"]
    PASSWORD = environ["USERS_LOGIN_PASSWORD"]
    return User.objects.create_user(username=USERNAME, password=PASSWORD)


@pytest.fixture
def logged_in(db, client, create_user):
    USERNAME = environ["USERS_LOGIN_USERNAME"]
    PASSWORD = environ["USERS_LOGIN_PASSWORD"]

    # Log client in and check login
    client.login(username=USERNAME, password=PASSWORD)

    return client
