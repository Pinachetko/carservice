from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^send-message/$', views.send_message, name="send-message"),
    url(r'^$', views.contacts, name="contacts"),
]
