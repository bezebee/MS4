from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_orders, name='view_orders'),
    path('add/<order_id>/', views.order, name='order'),
]