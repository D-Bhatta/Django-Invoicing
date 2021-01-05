from django.contrib.auth import login
from django.shortcuts import Http404, redirect, render
from django.urls import reverse
from django_apps.utils import get_logger
from users.forms import NewUserCreationForm

lg = get_logger()

# Create your views here.


def register(request):
    lg.debug("Rendering register page")
    if request.method == "GET":
        return render(request, "register.html", {"form": NewUserCreationForm})
    elif request.method == "POST":
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("invoicing:home"))
