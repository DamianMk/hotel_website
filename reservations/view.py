from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def homepage(request):
    return HttpResponse('This is going to be hotel homepage.\n'
                        'Work is still in progress...')
