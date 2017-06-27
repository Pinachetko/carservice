from django.shortcuts import render
from . import models
import project.additional_scripts as scripts
from django.http import HttpResponse
from services import models as services_models
# Create your views here.


def about(request):
    data = {"service_type_objects": services_models.ServiceType.objects.filter(is_active=True)}
    return render(request, "about.html", data)
