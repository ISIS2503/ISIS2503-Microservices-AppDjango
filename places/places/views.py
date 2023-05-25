from .models import Place
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def PlaceList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def PlaceCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        place = Place()
        place.name = data_json["name"]
        place.save()
        return HttpResponse("successfully created place")
    
def PlacesCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        places_list = []
        for place in data_json:
                    if isinstance(place, str) and len(place) > 1:
                        db_place = Place()
                        db_place.name = place
                        places_list.append(db_place)
                    else:
                        return HttpResponse("Place creation failed. Invalid place name")
        
        Place.objects.bulk_create(places_list)
        return HttpResponse("successfully created places")