from django.shortcuts import render

# Create your views here.

def helloworld(request, nev, szam):
    template = 'index.html'
    context = {
        'nev': nev,
        'dupla': 2*szam,
        'szamok': [1, 2, 3, 4, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    }
    print(nev)
    print(szam)
    return render(request, template, context)