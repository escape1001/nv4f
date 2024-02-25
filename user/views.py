from django.shortcuts import render

def report(request):
    context = {}
    return render(request, "user/report.html", context)
