from . import models
from django.shortcuts import render


def home(request):
    about = models.Home_about.objects.all()
    do = models.Do.objects.all()
    new = models.New.objects.all()
    contex = {
        "about": about,
        "do": do,
        "new": new,
    }
    return render(request, "home.html", contex)


def about(request):
    mission = models.Mission.objects.all()
    about_place = models.Place.objects.all()
    contex = {
        "mission": mission,
        "about_place": about_place,
    }
    return render(request, "about.html", contex)
