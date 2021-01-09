""" Tests for 'invoicing' app """
import pytest
from django.urls import reverse
from django_apps.utils import get_logger

from tests.fixtures import create_user, logged_in

lg = get_logger()

# This is supposed to fail
def test_helloworld():
    assert True == True


def test_view_homepage(client):
    url = reverse("invoicing:home")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_reach_authenticated_only_content_home(client, create_user, logged_in):
    url = reverse("invoicing:home")
    response = client.get(url)
    assert (
        "Your Dashboard" in response.content.decode()
    ), "Cannot reach authenticated content"


def test_dont_reach_authenticated_only_content_home(client):
    url = reverse("invoicing:home")
    response = client.get(url)
    assert (
        "Your Dashboard" not in response.content.decode()
    ), "Authenticated content is reachable without authentication"
