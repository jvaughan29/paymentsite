from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.results, name='results'),
    path('complete', views.complete, name='complete'),
    path('receipt', views.receipt, name='receipt'),
]