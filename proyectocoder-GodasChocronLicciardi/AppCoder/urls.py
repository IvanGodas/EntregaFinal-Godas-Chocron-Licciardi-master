from django.urls import path
from .views import *


urlpatterns = [
   path('arquero/', arquero, name = 'arquero'),
   path('mediocampista/', mediocampista,name='mediocampista' ),
   path('delantero/', delantero, name='delantero'),
   path ('arqueroFormulario/', arqueroFormulario, name='arqueroFormulario'),
   path('', inicio,name='inicio'),
   path('medioFormulario/', medioFormulario,name='medioFormulario'),
   path('delanteroFormulario/', delanteroFormulario,name='delanteroFormulario'),
   path('busquedaFutbolista', busquedaFutbolista, name='busquedaFutbolista'),
   path('buscar/', buscar, name='buscar'),
]

