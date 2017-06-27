from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^price-catalog/$', views.price_catalog, name="price-catalog"),
    url(r'^price-catalog/(?P<service_type>[^\/]*)/$', views.all_prices, name="all-prices"),
    url(r'^price-catalog/(?P<service_type>[^\/]*)/(?P<page>\d+)/$', views.all_prices, name="all-prices-on-pages"),
    url(r'^price-catalog/(?P<service_type>[^\/]*)/(?P<car_type>[^\/]*)/$', views.prices_by_type_of_car, name="prices-by-type-of-car"),
    url(r'^price-catalog/(?P<service_type>[^\/]*)/(?P<car_type>[^\/]*)/(?P<page>\d+)/$', views.prices_by_type_of_car, name="prices-by-type-of-car-on-pages"),

    # url(r'^price-catalog/(?P<service_type>[^\/]*)/(?P<page>\d+)/$', views.prices, name="prices-post"),
    # url(r'^price-catalog/(?P<service_type>[^\/]*)/(?P<car_type>.+)/$', views.prices, name="prices_by_type_of_cars"),
]
