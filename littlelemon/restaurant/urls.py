from django.contrib import admin 
from django.urls import path 
from . import views

  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    
]