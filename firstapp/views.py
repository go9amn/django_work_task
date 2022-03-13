
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = request.GET.get('name', '')
    message = request.GET.get('message', '')
    output = '<h2>Hello {0}<h3>{1}</h3></h2>'.format(name, message)
    return HttpResponse(output)
