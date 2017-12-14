from django.http import HttpResponse
from django.shortcuts import render
import json

from .models import Point

def index(request):
    return render(request, 'webpoints/index.html', {})

def points(request):
    points = Point.objects.all()

    points_json = [ p.to_json() for p in points ]
    return HttpResponse(json.dumps(points_json))
