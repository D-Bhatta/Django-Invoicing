from django.urls import include, path
from users import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
]
