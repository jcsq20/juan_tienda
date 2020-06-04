from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def validate(request):
    return JsonResponse({
        "Nombre": "Juan",
        "trabajo": "codigoFacilito",
        "courses":[
            {"titulo": "python"},
            {"titulo": "HTML"},
            {"titulo": "Base de datos"},
        ]
    })