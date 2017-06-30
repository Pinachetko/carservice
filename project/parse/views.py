from django.shortcuts import render
from django.http import HttpResponse
from . import models
from services import models as services_models
import os
from . import tasks




# Create your views here.


def scan(request):
    tasks.GrabTask.delay()
    return HttpResponse("ok")

def drop_db(request):
    try:
        services_models.ServiceType.objects.all().delete()
        services_models.Service.objects.all().delete()
        services_models.ServicedCar.objects.all().delete()
        return HttpResponse("All databases are cleaned!" )
    except Exception as e:
        return HttpResponse("Error!" + str(e) )


def check(request):
    return HttpResponse("is checked")
