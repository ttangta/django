from django.urls import path
from .import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # Path Parameter(경로 매개변수) : URL 경로 자체에 포함된 변수
    # <자료형: 변수명> 형식으로 Variable Routing 
    path('<int:pk>/', views.detail, name='detail'),
]