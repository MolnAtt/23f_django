from django.shortcuts import render

# Create your views here.

def otodik_view(request):
    return render(request, 'index.html')

