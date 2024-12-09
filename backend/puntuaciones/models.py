from django.db import models

class Equipo(models.Model):
    numero = models.IntegerField(default=0, unique=True)
    def __str__(self):
        return f"Equipo {self.numero}"

class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')

    def __str__(self):
        return f"{self.nombre} ({self.equipo.numero})"

class Ejercicio(models.Model):
    numero = models.IntegerField()
    puntaje_maximo = models.FloatField()

    def __str__(self):
        return f"Ejercicio {self.numero}"

class Puntuacion(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    puntaje = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipo.numero} - {self.ejercicio.numero}: {self.puntaje}"
    
