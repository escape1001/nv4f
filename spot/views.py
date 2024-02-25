from django.shortcuts import render
from .models import Spot
from django.db.models import Q

def spot_list(request):
    if request.GET.get("q"):
        q = request.GET.get("q")
        spots = Spot.objects.filter(
            Q(title__icontains = q) | Q(contents__icontains = q)
        ).distinct()
    else :
        spots = Spot.objects.all()

    context = {"spot_list":spots}
    return render(request, "spot/spot_list.html", context)

def spot_detail(request, id):
    spot = Spot.objects.get(id=id)
    context = {"spot": spot}
    return render(request, "spot/spot_detail.html", context)