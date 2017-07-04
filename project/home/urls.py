from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^full-services-list/$', views.full_services_list, name="get-full-services-list"),
    url(r'^undefined', views.undefined),
    url(r'^$', views.home, name="home"),

]
