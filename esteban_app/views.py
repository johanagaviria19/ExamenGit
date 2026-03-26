from django.shortcuts import render

# Create your views here.

def hoja_de_vida(request):
    return render(request, 'esteban_app/hoja_de_vida.html')
