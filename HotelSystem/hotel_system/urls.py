from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('db', views.dbupdate, name='dbupdate'),
    path('values', views.values, name='values'),
    path('month', views.month, name='month'),
    path('cont', views.content, name = 'cont')
]