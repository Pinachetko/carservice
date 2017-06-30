"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views as home_views
from django.views.defaults import page_not_found, server_error, bad_request
from django.utils.functional import curry

handler404 = curry(page_not_found, template_name='404.html', exception=Exception("Internal error server"))
handler500 = curry(server_error, template_name='500.html', exception=Exception("Page not Found"))
handler400 = curry(bad_request, template_name='400.html', exception=Exception("Bad request error"))

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^parser/', include('parse.urls')),
    url(r'^$', home_views.home),
]

