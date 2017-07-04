from celery.task import Task
from celery.registry import tasks
from . import models
import requests
import re


class sendSMS(Task):

    def run(self, phone, message, name):
        settings_objects = models.smsSendingSetting.objects.filter(is_active=True)
        message_body = "(Автосервис) Новое сообщение! %s, %s, %s"%(name, phone, message)
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1)',
            'Accept-Encoding': ', '.join(('gzip', 'deflate')),
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }
        if len(message_body) >=160:
            message_body = (message_body[:155] + "...")
        for setting_object in settings_objects:
            response = requests.get("http://sms.ru/sms/send?api_id=%s&to=%s&text=%s"%(str(setting_object.app_id).upper(), setting_object.recipient_phone, re.sub(r"\s+", "+",message_body)), headers=headers)
            print(response)
tasks.register(sendSMS)
