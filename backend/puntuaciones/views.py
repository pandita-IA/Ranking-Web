from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Equipo, Puntuacion, Ejercicio, Jugador
from django.db.models import Sum , Max

@api_view(['GET'])
def ranking(request):
    # Sumar los puntajes por equipo y ejercicio
    ranking = (
        Puntuacion.objects.values('equipo__numero', 'ejercicio__numero')
        .annotate(total=Sum('puntaje'), ultima_solucion=Max('created_at'))
        .order_by('equipo__numero', '-total')
    )

    # Obtener jugadores por equipo
    equipos = Equipo.objects.prefetch_related('jugadores').all()
    equipos_con_integrantes = {
        equipo.numero: [jugador.nombre for jugador in equipo.jugadores.all()]
        for equipo in equipos
    }

    # Crear un diccionario de ejercicios resueltos por equipo
    ejercicios_resueltos_por_equipo = {}
    for item in ranking:
        equipo_numero = item['equipo__numero']
        ejercicio_numero = item['ejercicio__numero']
        if equipo_numero not in ejercicios_resueltos_por_equipo:
            ejercicios_resueltos_por_equipo[equipo_numero] = []
        ejercicios_resueltos_por_equipo[equipo_numero].append({
            "ejercicio": ejercicio_numero,
            "puntaje_total": item['total'],
            "ultima_solucion": item['ultima_solucion'],
        })

    # Construir el resultado final enriquecido
    resultado = []
    for equipo_numero, ejercicios in ejercicios_resueltos_por_equipo.items():
        resultado.append({
            "equipo_numero": equipo_numero,
            "puntaje_total": sum(ejercicio['puntaje_total'] for ejercicio in ejercicios),
            "ejercicios_resueltos": ejercicios,
            "integrantes": equipos_con_integrantes.get(equipo_numero, [])
        })

    # Ordenar el resultado final por puntaje total y última solución
    resultado.sort(key=lambda x: (-x["puntaje_total"], max(ej["ultima_solucion"] for ej in x["ejercicios_resueltos"])))

    return Response(resultado)


@api_view(['GET'])
def usuarios(request):
    jugadores = Jugador.objects.select_related('equipo').all()

    data = [
        {
            "nombre": jugador.nombre,
            "equipo": {
                "numero": jugador.equipo.numero,
            }
        }
        for jugador in jugadores
    ]
    return Response(data)