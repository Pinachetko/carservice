from django.shortcuts import render
from . import models
from services import models as services_models
import project.additional_scripts as scripts
import os
import re
import random
from weasyprint import HTML, CSS
from django.template.loader import get_template,render_to_string
from django.http import HttpResponse

# Create your views here.


def home(request):
    data = {}
    service_type_objects = services_models.ServiceType.objects.filter(is_active=True)
    logos = [ file for file in os.listdir("./static/images/logos/png") if file[-3:] in ["png", "svg", "jpg"] ]
    random.shuffle(logos)
    data.update({"logos": logos, "service_type_objects": service_type_objects})
    return render(request, "home.html", data)


def full_services_list(request):
    html_template = render_to_string('services-list.html')
    pdf_file = HTML(string=html_template).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="service-list.pdf"'
    return response
