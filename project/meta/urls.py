from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sitemap.xml$', views.sitemap, name="sitemap"),
    url(r'^robots.txt$', views.robots, name="robots"),
]
