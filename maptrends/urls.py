from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('result/', views.result,name='result'),
    path('home/', views.home,name='home'),
    path('final_product/', views.final_product,name='final_product'),
]