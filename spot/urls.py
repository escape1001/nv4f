from django.urls import path
from . import views

urlpatterns = [
    path('', views.spot_list, name="spot_list"),
    path('<int:pk>/', views.spot_detail, name="spot_detail"),
    # path('spot/write/', views.spot_write, name="spot_write"),
    # path('spot/update/<int:pk>/', views.spot_update, name="spot_update"),
    # path('spot/delete/<int:pk>/', views.spot_delete, name="spot_delete"),
]