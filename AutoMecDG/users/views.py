from django.shortcuts import render, HttpResponse


# Create your views here.

def pagina_inicial(request):
    return render(request, "users/index.html")
