from .models import Spot
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin


class SpotList(ListView):
    model = Spot
    ordering = "-id"

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q')

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(contents__icontains=q)
            ).distinct()
        
        return queryset

class SpotDetail(DetailView):
    model = Spot


class SpotWrite(LoginRequiredMixin, CreateView):
    model = Spot
    fields = '__all__'
    success_url=reverse_lazy('spot_list')


class SpotUpdate(LoginRequiredMixin, UpdateView):
    model = Spot
    fields = '__all__'

    def get_success_url(self):
        return reverse('spot_detail', args=[str(self.object.id)])

class SpotDelete(LoginRequiredMixin, DeleteView):
    model = Spot
    success_url = reverse_lazy('spot_list')


spot_list = SpotList.as_view()
spot_detail = SpotDetail.as_view()
spot_write = SpotWrite.as_view()
spot_update = SpotUpdate.as_view()
spot_delete = SpotDelete.as_view()