from django.urls import path
from app5 import views


urlpatterns = [
   path('index/', views.index, name='index'), 
]
