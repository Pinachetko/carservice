from django.shortcuts import render
from . import models
from django.template.loader import render_to_string
import project.additional_scripts as scripts
from services import models as services_models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from . import tasks


# Create your views here.
@csrf_exempt
def contacts(request):
    data = {"service_type_objects": services_models.ServiceType.objects.filter(is_active=True)}
    return render(request, "contacts.html", data)

@csrf_exempt
def send_message(request):
    data = {"isOk": True}
    name = request.POST.get("name", '').strip()
    phone = request.POST.get("phone", '').strip()
    email = request.POST.get("email", '').strip()
    message = request.POST.get("message", '').strip()
    if not re.match(r"^([a-z0-9_\.-]+)@([a-z0-9_\.-]+)\.([a-z\.]{2,6})$", email):
        email = "Не указан"
    if not re.match(r"^[а-яА-ЯёЁ a-zA-z\-]{3,100}$", name ):
        data["isOk"] = False
        data["error_name"] = "Указано не корректное имя"
    if not re.match(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", phone ):
        data["isOk"] = False
        data["error_phone"] = "Указан не корректный номер телефона"
    if data["isOk"]:
        models.Message.objects.create(from_name=name, from_email=email, from_phone=phone, from_message=message, from_date_time=timezone.now())
        subject = "Заявка на проведение авторемонтных работ"
        from_email = "webmaster@rybinsk-tech.ru"
        to = "costya.badanin2015@yandex.ru"
        text_content = message
        html_content = render_to_string("email/email.html", {"from_name":name, "from_email":email, "from_phone":phone, "from_message":message})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # tasks.sendSMS.delay(phone, message, name)

        data["submit_message"] = "Сообщение отправлено!"

    else:
        data["submit_message"] = "Сообщение не отправлено!"

    return JsonResponse(data)

