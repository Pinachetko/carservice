from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^scan/', views.scan, name="scan"),
    url(r'^show/', views.show, name="show_products"),
     url(r'^drop_db/', views.dropdb, name="dropdb")
]
