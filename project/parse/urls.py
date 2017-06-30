from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^scan/$', views.scan, name="scan"),
url(r'^drop_db/$', views.drop_db, name="dropdb"),
url(r'^check/$', views.check, name="check"),
]
