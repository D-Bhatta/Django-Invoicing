""" Tests for 'users' app """
from os import environ

import pytest
from django.urls import reverse
from django_apps.utils import get_logger
from pytest_django.asserts import SimpleTestCase

from tests.fixtures import create_user

lg = get_logger()

# This is supposed to fail
def test_helloworld():
    assert True == True, "Basic tests failing"


def test_view_users_login_status(client):
    url = "/users/accounts/login/"
    response = client.get(url)
    assert response.status_code == 200, "Cant reach login page"


@pytest.mark.django_db
def test_users_login(client, create_user):
    USERNAME = environ["USERS_LOGIN_USERNAME"]
    PASSWORD = environ["USERS_LOGIN_PASSWORD"]
    response = client.login(username=USERNAME, password=PASSWORD)
    assert response == True, "Failed to login to app"

    url = reverse("invoicing:home")
    response = client.post(url)

    assert (
        response.context["user"].is_authenticated == True
    ), "Failed to verify authenticated status of user"
