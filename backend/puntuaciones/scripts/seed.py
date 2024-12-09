import os
import django
import random
from django.utils.timezone import now
from puntuaciones.models import Equipo, Jugador, Ejercicio, Puntuacion


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()


def run():
    print("Seeding data...")

    # Limpiar datos previos
    Puntuacion.objects.all().delete()
    Jugador.objects.all().delete()
    Ejercicio.objects.all().delete()
    Equipo.objects.all().delete()

    # Crear equipos
    equipos = []
    for i in range(1, 6):  # 5 equipos
        equipo = Equipo.objects.create(numero=i)
        equipos.append(equipo)

    # Crear jugadores
    nombres = ["Juan", "María", "Luis", "Ana", "Pedro", "Sofía", "Carlos", "Lucía", "Miguel", "Elena"]
    for equipo in equipos:
        for _ in range(2):  # 3 jugadores por equipo
            if nombres == []:
                break
            nombre = random.choice(nombres)
            nombres.remove(nombre)  # Evitar nombres repetidos
            Jugador.objects.create(nombre=nombre, equipo=equipo)

    # Crear ejercicios
    ejercicios = []
    for i in range(1, 6):  # 5 ejercicios
        ejercicio = Ejercicio.objects.create(numero=i, puntaje_maximo=random.uniform(5.0, 10.0))
        ejercicios.append(ejercicio)

    # Crear puntuaciones
    for equipo in equipos:
        for ejercicio in ejercicios:
            Puntuacion.objects.create(
                equipo=equipo,
                ejercicio=ejercicio,
                puntaje=random.uniform(0.0, ejercicio.puntaje_maximo),
                created_at=now()
            )

    print("Seeding complete.")
