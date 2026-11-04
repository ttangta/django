"""
URL configuration for template_urls project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('dinner/',views.dinner),
    path('template_inheritance/', views.inheritance),
    path('html_form/', views.form),
    path('fake/', views.fack),
    # HTML Form 화용 예제 
    path('throw/', views.throw), # 서버로 데이터 전송
    path('catch/', views.catch), # 서버로 넘어온 데이터 처리 
    # URLs 의 Variable Routing 학습 부분
    path('num/<int:num>', views.num),
    path('str/<str:content>', views.content),
    # App URL 학습 부분
    path('appurls/', include('appurls.urls')),
    # Naming URL Patterns 학습 부분
    path('namingurls/', include('namingurls.urls')),
    # Naming URL Patterns 학습 부분
    path('namingurlpatterns/', include('urlnamings.urls')),
    # Namespace 학습 부분
    path('centers/', include('centers.urls')),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
]
