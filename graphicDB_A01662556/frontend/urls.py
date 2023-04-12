from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('chart', views.chart, name="chart"),
    path('log', views.log, name="log"),
    path('hola', views.hola, name="hola")
]
