from django.urls import path
from . import views

urlpatterns = [
    path('', views.spot_list, name="spot_list"),
    path('<int:id>', views.spot_detail, name="spot_detail")
]