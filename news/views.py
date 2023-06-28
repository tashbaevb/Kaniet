from . import models
from django.shortcuts import render, get_object_or_404


def services_all(request):
    serv = models.Service.objects.all()
    return render(request, "service.html", {"serv": serv})


def services_more(request, id):
    more = get_object_or_404(models.Service, id=id)
    return render(request, "service_more.html", {"more": more})


def data(request):
    contact = models.Contact.objects.all()
    return render(request, "contact.html", {"contact": contact})


def novelty(request):
    news = models.New.objects.all()
    return render(request, "news.html", {"news": news})
