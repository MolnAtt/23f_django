from django.shortcuts import render

# Create your views here.

def kilencedik_view(request,i):
    template = 'index.html'
    lista = ['alma', 'körte', 'grapefruit', 'szőlő', "maracuja", 'guava', 'mangó', 'sárkánygyümölcs', 'szilva', 'barack', 'málna']
    context = {
        'gyumi': lista[i],
        
    }
    
    return render(request, template, context)

def kilencedik_view_szoveges(request,szoveg):
    template = 'index2.html'
    szotar = {
        'egy': 1,
        'ketto': 2,
        'harom': 3,
    }
    context = {
        'szam': szotar[szoveg],
        
    }

    return render(request, template, context)