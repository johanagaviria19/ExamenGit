from django.shortcuts import render

def index(request):
    return render(request, 'hoja_de_vida_johana/index.html')
