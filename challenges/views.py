from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This works!")

def suhas(request):
    return HttpResponse("1 closer!")