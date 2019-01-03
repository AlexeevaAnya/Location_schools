from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Skola


def index(request):
    list = Skola.objects.all()
    template = loader.get_template('map/index.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))
