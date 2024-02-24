from django.shortcuts import render
from django.http import HttpResponse

def report(request):
    return HttpResponse("<h1>제보페이지</h1>")