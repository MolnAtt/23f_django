from django.shortcuts import render
from django.http import HttpResponse

def haliho_view(request):
    return HttpResponse('Halihó!')