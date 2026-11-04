from django.urls import path, include
from . import views

app_name = 'centers'

urlpatterns = [
    path('', views.center, name='center'),
    path('app1/', include('app1.urls'))
]