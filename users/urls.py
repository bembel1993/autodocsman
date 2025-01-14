from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('docsread/', views.readDocx, name='readDocx'),
    path('showform/', views.showform, name='showform'),
    path('users/', views.users, name='users'),
]