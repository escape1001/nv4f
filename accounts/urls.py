from django.urls import path, include
from . import views

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path("signup/", include("dj_rest_auth.registration.urls")),
    path("", include("dj_rest_auth.urls")),
    path('my_info/', views.my_info, name='my_info'),
    path('my_favorite/', views.my_favorite, name='my_favorite'),
]