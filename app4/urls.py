from django.urls import path
from app4 import views


urlpatterns = [
    path('index/', views.index, name='indexs'),
    path('message/', views.message, name='messages'),
]
