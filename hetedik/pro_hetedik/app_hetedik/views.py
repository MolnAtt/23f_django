from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import *


def view_hetedik(request):

    darabok = Darab.objects.all()

    template = 'app_hetedik/hetedik.html'
    context = {
        'darabok': darabok
    }

    return render(request, template, context)


def view_uj_darab(request):

    darabok = Darab.objects.all()

    template = 'app_hetedik/hetedik.html'
    context = {
        'darabok': darabok
    }

    return render(request, template, context)



def view_uj_mufaj(request):

    template = 'app_hetedik/uj_mufaj.html'
    context = {}

    return render(request, template, context)


def view_mufaj_import(request):
    return render(request, 'import.html', {})

def view_uj_mufaj_kuld(request):
    if request.method!='POST':
        return HttpResponse('az űrlap kitöltésével szabad csak idejönni!')
    if 'ajdi' not in request.POST:
        return HttpResponse('hogyhogy nincs ajdi kulcsod a post-ban?')
    if 'nev' not in request.POST:
        return HttpResponse('hogyhogy nincs nev kulcsod a post-ban?')

    # LBYL: Look Before You Leap

    szotar = request.POST
    print(szotar)


    try:
        az_ajdi = int(szotar['ajdi'])
    except:
        return HttpResponse('Nem adtál meg számot? ')


    a_nev = szotar['nev']

    uj_mufaj = Mufajka.objects.create(ajdi=az_ajdi, nev=a_nev)



    template = 'app_hetedik/uj_mufaj_kuld.html'
    context = {
        'uj_mufaj': uj_mufaj,
    }


    return render(request, template, context)


