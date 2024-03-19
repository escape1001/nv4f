from .models import Post
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import PostSerializer


@api_view(['GET'])
def spot_list(request):
    if request.method == 'GET' :
        spotlist = Post.objects.all()
        serializer = PostSerializer(spotlist, many=True)
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def spot_detail(request, pk):
    if request.method == 'GET' :
        spotlist = Post.objects.get(pk=pk)
        serializer = PostSerializer(spotlist)
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SpotList(ListView):
#     model = Spot
#     ordering = "-id"

#     def get_queryset(self):
#         queryset = super().get_queryset()

#         q = self.request.GET.get('q')

#         if q:
#             queryset = queryset.filter(
#                 Q(title__icontains=q) | Q(contents__icontains=q)
#             ).distinct()
        
#         return queryset

# class SpotDetail(DetailView):
#     model = Spot


# class SpotWrite(LoginRequiredMixin, CreateView):
#     model = Spot
#     fields = '__all__'
#     success_url=reverse_lazy('spot_list')


# class SpotUpdate(LoginRequiredMixin, UpdateView):
#     model = Spot
#     fields = '__all__'

#     def get_success_url(self):
#         return reverse('spot_detail', args=[str(self.object.id)])

# class SpotDelete(LoginRequiredMixin, DeleteView):
#     model = Spot
#     success_url = reverse_lazy('spot_list')


# spot_list = SpotList.as_view()
# spot_detail = SpotDetail.as_view()
# spot_write = SpotWrite.as_view()
# spot_update = SpotUpdate.as_view()
# spot_delete = SpotDelete.as_view()