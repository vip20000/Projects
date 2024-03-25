from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), 
    path('upload/', views.upload, name='upload'),
    path('result/', views.result, name='result'),
]
