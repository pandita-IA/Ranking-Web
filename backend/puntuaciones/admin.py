from django.contrib import admin
from .models import Equipo, Jugador, Ejercicio, Puntuacion

admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Ejercicio)
admin.site.register(Puntuacion)
