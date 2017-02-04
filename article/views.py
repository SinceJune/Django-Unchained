from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    message = "Hello World!"
    return render(request, 'index.html', locals())
