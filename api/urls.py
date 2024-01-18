from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_routes, name='routes'),
  path('notes/', views.get_all_notes, name='notes'),
  path('notes/<str:pk>/', views.get_single_note, name='note'),
]