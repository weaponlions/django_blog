from django.urls import path
from app1 import views


urlpatterns = [
    path('', views.index, name='app1'),
    path('modelForm/', views.indexTwo, name='modelForm'),
]
