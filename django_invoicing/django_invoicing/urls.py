from django.urls import path

from django_invoicing import views

app_name = "invoicing"

urlpatterns = [path("home/", views.homepage, name="home")]
