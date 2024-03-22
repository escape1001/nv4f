from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('post/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/filter_list/', views.post_filter_list, name='post_filter_list'),
    path('post/<int:pk>/like/', views.post_like_toggle, name='post_like_toggle'),
]