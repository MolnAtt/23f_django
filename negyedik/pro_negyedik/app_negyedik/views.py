from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def view_negyedik(request):
#     return HttpResponse('asdflkjahdf')


def view_negyedik(request):
    return render(request, 'index.html')