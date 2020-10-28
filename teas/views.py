from django.shortcuts import render
from django.views.generic import ListView
from .models import Tea


def home(request):
    return render(request, "home.html")


class TeaListView(ListView):

    model = Tea