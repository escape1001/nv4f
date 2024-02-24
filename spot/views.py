from django.shortcuts import render
from django.http import HttpResponse

def spot_list(request):
    return HttpResponse("<h1>spot_list</h1>")

def spot_detail(request, id):
    return HttpResponse(f"<h1>spot_detail {id}</h1>")