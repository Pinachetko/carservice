from django import template
from project import additional_scripts as scripts
from services import models
import os
from project.settings.base import PROJECT_ROOT
import re
import random
register = template.Library()

@register.filter(name='translite')
def translite(value, lang):
    return scripts.Translite(value).translite(lang).get_link()

@register.filter(name="get_object_by_name")
def get_object_by_name(model, name):
    if model == "ServiceType":
        return models.ServiceType.objects.get(type_name=name)
    elif model == "Service":
        return models.Service.objects.get(service_name=name)
    elif model == "ServicedCar":
        return models.ServicedCar.objects.get(car_type=name)

def get_attr(model, args):
    args = args.split(",")
    name = args[0]
    attr = args[1]
    if model == "ServiceType":
        obj = models.ServiceType.objects.get(type_name=name)
    elif model == "Service":
        obj = models.Service.objects.get(service_name=name)
    elif model == "ServicedCar":
        obj = models.ServicedCar.objects.get(car_type=name)
    return obj.__getattribute(attr)

@register.filter(name='path_without_page_number')
def get_path_without_page_number(path):
    return re.sub(r"\d+\/$", "", path)

@register.filter(name='dir_by_position')
def get_dir_by_position(path, pos):
    dirs = [dir_ for dir_ in path.split("/") if dir_!='']
    if len(dirs)  <=  int(pos):
        return 'DoesNotExist'
    else:
        return scripts.Translite(dirs[int(pos)]).translite("ru").normalize() if len(dirs[int(pos)]) > 3 else scripts.Translite(dirs[int(pos)]).translite("ru").normalize().upper()

@register.filter(name='inc')
def inc(count):
    return count + 1

@register.filter(name='dec')
def inc(count):
    return count - 1

@register.filter(name='truncatechars_right')
def  truncatechars_right(string, count):
    return string[:-int(count)]

@register.filter(name='get_string')
def  get_string(objects, arg):
    return arg + " "+ ", ".join([str(obj) for obj in objects])

@register.filter(name='contains')
def  contains(objects, obj):
    return True if obj in objects else False

@register.filter(name='relpath')
def  get_relpath(path):
    return os.path.relpath(path, PROJECT_ROOT)


@register.filter(name='selected')
def  selected(path, app_name):
    dirs = [dir_ for dir_ in path.split("/") if dir_!='']
    if len(dirs) > 0:
        return True if dirs[0] == app_name else False
    else:
        return True if app_name == "home" else False


@register.filter(name='random_slice')
def  random_slice(iterator, count):
    res = list(iterator)
    random.shuffle(res)
    return res[:int(count)]

