from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_designs, name="designs"),
    path('<int:design_id>/', views.design_detail, name="design_detail"),
    path('add', views.add_design, name="add_design"),
    path('edit/<int:design_id>/', views.edit_design, name="edit_design"),
    path('delete/<int:design_id>/', views.delete_design, name="delete_design"),
]
