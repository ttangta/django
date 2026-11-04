from django.urls import path
from . import views

urlpatterns = [
    path('', views.naming_index, name='naming_index'),
    path('move/', views.move, name='move'),
    path('<int:data>/', views.data, name='data'),
]