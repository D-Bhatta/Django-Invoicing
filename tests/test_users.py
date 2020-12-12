""" Tests for 'users' app """
from os import environ

import pytest
from django.urls import reverse
from django_apps.utils import get_logger
from pytest_django.asserts import assertRedirects

from tests.fixtures import create_user, logged_in

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


@pytest.mark.django_db
def test_users_logout(client, create_user):
    USERNAME = environ["USERS_LOGIN_USERNAME"]
    PASSWORD = environ["USERS_LOGIN_PASSWORD"]

    # Log client in and check login
    client.login(username=USERNAME, password=PASSWORD)
    url = reverse("invoicing:home")
    response = client.post(url)
    login_status = response.context["user"].is_authenticated

    assert login_status == True, "Failed to login to app"

    # Check logout
    url = reverse("logout")
    response = client.get(url)
    with pytest.raises(TypeError):
        response.context["user"].is_authenticated

    # Check redirect
    assertRedirects(
        response=response,
        expected_url=reverse("invoicing:home"),
        status_code=302,
        msg_prefix="Failed to redirect to homepage aftre logout",
    )


@pytest.mark.django_db
def test_view_users_password_change_status(client, create_user, logged_in):
    url = reverse("password_change")
    response = client.get(url)
    assert response.status_code == 200, "Cant reach passowrd change page"


@pytest.mark.django_db
def test_view_users_password_change_done_status(
    client, create_user, logged_in
):
    url = reverse("password_change_done")
    response = client.get(url)
    assert response.status_code == 200, "Cant reach passowrd change done page"


def test_view_users_password_reset_status(client):
    url = reverse("password_reset")
    response = client.get(url)
    assert response.status_code == 200, "Cant reach passowrd reset page"


def test_view_users_password_reset_done_status(client):
    url = reverse("password_reset_done")
    response = client.get(url)
    assert response.status_code == 200, "Cant reach passowrd reset done page"
