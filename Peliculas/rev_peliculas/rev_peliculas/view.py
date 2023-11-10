from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from app_peli.models import Peliculas
#def prueba_con_html(request):
    #contexto = {}
    #http_response = render(
        #request=request,
       # template_name='base.html',
       # context=contexto,
   # )
 #   return http_response

#def crear_peli(request):
  # http_response = render(
    #   request=request,
    #   template_name='base.html',
    #)
   #return http_response

def crear_peli(request):
   if request.method == "POST":
       data = request.POST
       peli = Peliculas(nombre=data['nombre'], puntaje=data['puntaje'])
       peli.save()
       url_exitosa = reverse('lista_peli')
       return redirect(url_exitosa)
   else:  
       return render(
           request=request,
           template_name='base.html',
       )

def lista_peli(request):
   contexto = {
       "pelicula": Peliculas.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='base.html',
       context=contexto,
   )
   return http_response