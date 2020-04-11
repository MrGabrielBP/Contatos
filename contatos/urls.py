from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('busca/', views.busca, name="busca"),
    path('<int:id>/', views.detalhes, name="detalhes"),
]
