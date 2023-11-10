from django.shortcuts import render

# Create your views here.
def crear_peli(request):
   http_response = render(
       request=request,
       template_name='rev_peliculas/formulario_peli_a_mano.html',
    )
   return http_response