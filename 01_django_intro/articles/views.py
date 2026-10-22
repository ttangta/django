from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "articles/index.html")

def none_template(request):
    return HttpResponse("템플릿을 사용하지 않은 요청 처리")