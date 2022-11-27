from .models import Place
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json


def PlaceList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id', 'name', 'measurements'))
    return JsonResponse(context, safe=False)


def PlaceCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        place = Place()
        place.variable = data_json['variable']
        place.value = data_json['value']
        place.unit = data_json['unit']
        place.place = data_json['place']
        place.save()
        return HttpResponse("successfully created place")


def PlacesCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        place_list = []
        for place in data_json:
            db_place = Place()
            db_place.variable = place['variable']
            db_place.value = place['value']
            db_place.unit = place['unit']
            db_place.place = place['place']
            place_list.append(db_place)

        Place.objects.bulk_create(place_list)
        return HttpResponse("successfully created places")
