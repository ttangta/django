from django.urls import path
from . import views

urlpatterns = [
    path('', views.naming),
    path('goto/', views.goto),
]
