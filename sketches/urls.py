from django.urls import path
from . import views

urlpatterns = [
    path('', views.sketches, name='sketches'),
    path('<int:sketch_id>/', views.sketch_detail, name='sketch_detail'),
    path('add/', views.add_sketch, name='add_sketch'),
]
