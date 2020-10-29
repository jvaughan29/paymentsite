from django.urls import path

from . import views

urlpatterns = [
    path('paymententry', views.index, name='index'),
    path('results', views.results, name='results'),
    path('exportall', views.exportall, name='exportall'),
    path('exportyesterday', views.exportyesterday, name='exportyesterday'),
    path('complete', views.complete, name='complete'),
    path('receipt', views.receipt, name='receipt'),
    path('summaries', views.summaries, name='summaries'),
]