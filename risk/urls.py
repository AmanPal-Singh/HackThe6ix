from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
   path('', views.index, name='index'),
   path('about', views.about, name= 'about')
]