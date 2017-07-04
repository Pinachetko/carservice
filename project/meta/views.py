from django.shortcuts import render_to_response
from . import models
from django.http import HttpResponse

# Create your views here.

def robots(request):
    return render_to_response("robots.txt", content_type="plain/text")

def sitemap(request):
    return render_to_response("sitemap.xml", content_type="application/xhtml+xml")
