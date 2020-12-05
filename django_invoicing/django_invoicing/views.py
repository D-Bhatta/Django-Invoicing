from django.shortcuts import render
from django_apps.utils import get_logger

lg = get_logger()

# Create your views here.


def homepage(request):
    lg.debug("Rendering homepage")
    return render(request, "homepage.html", {})


def dummy(request):
    lg.debug("Rendering dummypage")
    return render(request, "dummy.html", {})
