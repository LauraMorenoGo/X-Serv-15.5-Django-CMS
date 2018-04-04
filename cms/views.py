from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages
# Create your views here.

def listar(request):
    respuesta = "Direcciones: "
    lista = Pages.objects.all()
    for pag in lista:
        respuesta += "<br>/" + pag.name + " = " + pag.page
    return HttpResponse(respuesta)


def buscar(request, ident):
    try:
        pag = Pages.objects.get(name=ident)
        respuesta = "Página " + pag.name + " = " + pag.page
    except Pages.DoesNotExist:  #Error no encuentra la página
        respuesta = "Página no disponible en la base de datos"
    return HttpResponse(respuesta)
