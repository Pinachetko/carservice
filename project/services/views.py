from django.shortcuts import render
from . import models
from project import additional_scripts as scripts
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import re




# Create your views here.

def get_default_data_for_services(request, service_type=None, car_type=None, page=1, method="GET", all_data=True):
    data = {}
    current_page= page
    records_on_page = 15

    current_type_name = scripts.Translite(service_type).translite(lang="ru").normalize()
    service_type_objects = models.ServiceType.objects.filter(is_active=True)
    if  car_type:
        car_type_object = models.ServicedCar.objects.get(car_type__iexact=scripts.Translite(car_type).translite(lang="ru").normalize())
        service_objects = models.Service.objects.filter(service_type=service_type_objects.get(type_name=current_type_name)).filter(serviced_cars=car_type_object)
    else:
        service_objects = models.Service.objects.filter(service_type=service_type_objects.get(type_name=current_type_name))

    count_pages = (service_objects.count() // records_on_page) + 1 if service_objects.count() % records_on_page > 0 else service_objects.count() // records_on_page

    if current_page == 1:
        service_objects = service_objects[:records_on_page]
    elif current_page ==  count_pages :
        service_objects = service_objects[records_on_page * (current_page-1) :]
    else:
        service_objects = service_objects[records_on_page * (current_page- 1) : records_on_page * current_page]
    if method == "GET":
        return {"current_type_name":current_type_name,"service_objects":service_objects,\
                "count_pages": count_pages, "current_page": current_page, "service_type_objects":service_type_objects}
    elif method == "POST":
        return {"html": render_to_string("tbody.html", {"service_objects": service_objects, "request": request}), 'count_pages': count_pages, "current_page": current_page, "hrefTextPrefix": re.sub(r"\d+\/$", "", request.path)}


def price_catalog(request):
    data = {"service_type_objects": models.ServiceType.objects.filter(is_active=True)}
    return render(request, "price-catalog.html", data)

@csrf_exempt
def all_prices(request, service_type, page=1):
    if request.method == "GET":
        data = get_default_data_for_services(request, service_type=service_type,page=int(page))
        return render(request, "prices.html", data)
    elif request.method == "POST":
        post_data = get_default_data_for_services(request,service_type=service_type,page=int(page), method="POST")
        return JsonResponse(post_data)

@csrf_exempt
def prices_by_type_of_car(request, service_type, car_type=None, page=1):
    if request.method == "GET":
        data = get_default_data_for_services(request, service_type=service_type, car_type=car_type, page=int(page))
        return render(request, "prices.html", data)
    elif request.method == "POST":
        post_data = get_default_data_for_services(request,service_type=service_type,car_type=car_type,page=int(page), method="POST")
        return JsonResponse(post_data)
