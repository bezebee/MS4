from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_designs, name="designs"),
    path('<int:design_id>/', views.design_detail, name="design_detail"),
    path('add', views.add_design, name="add_design"),
]
