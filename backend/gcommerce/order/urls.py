from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_order, name='get_order'),
    #path('new/', views.new, name='porto_new'),
    #path('<int:pk>', views.edit, name='porto_edit'),
    #path('delete/<int:pk>', views.delete, name='porto_delete'),    
]
