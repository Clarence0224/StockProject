from django.urls import path

from . import views

urlpatterns = [
    path('', views.openDashboard, name='dashboard'),
    path('stock-list/', views.ShowAll, name='stock-list'),
    path('stock-details/<int:pk>/', views.viewStock, name='stock-details'),
    path('stock-buy/', views.BuyStock, name='stock-buy'),
    path('stock-sell/<int:pk>/', views.SellStock, name='stock-sell'),
]