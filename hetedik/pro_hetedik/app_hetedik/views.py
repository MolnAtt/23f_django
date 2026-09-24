from django.shortcuts import render

# Create your views here.

from .models import *


def view_hetedik(request):

    darabok = Darab.objects.all()

    template = 'app_hetedik/hetedik.html'
    context = {
        'darabok': darabok
    }

    return render(request, template, context)