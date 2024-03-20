from django.urls import path
from . import views

urlpatterns = [
    # path('posts/', archive_views.post_list, name='post_list'), # 루트 urls.py에 지정됨
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('update/<int:pk>/', views.post_update, name='post_update'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
]