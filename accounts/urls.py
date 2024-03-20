from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('my_info/', views.my_info, name='my_info'),
    path('my_favorite/', views.my_favorite, name='my_favorite'),
]