from django.shortcuts import render

# Create your views here.

# Template System을 사용한 View 함수
def index(request):
    context = {
        "username": "땅타",
        "age": 25,
    }
    return render(request, "articles/index.html", context)


# DTL(Django Template Language) 사용법 연습 View 함수
import random
def dinner(request):
    menu = ["국밥", "국수", "카레", "탕수육", "빵"]
    alcohol = ["좋은데이", "참이슬", "대선", "진로"]
    picked = random.choice(menu)
    username = "땅타",
    age = 19
    context = {
        "menu":menu,
        "alcohol":alcohol,
        "picked": picked,
        "username":username,
        "age":age
    }
    return render(request, "articles/dinner.html", context)

# 템플릿 상속을 확인하기 위한 View 함수
def inheritance(request):
    return render(request, "articles/inheritance.html")

# HTML Form 확인을 위한 View 함수
def form(request):
    return render(request, "articles/htmlform.html")

# HTML Form의 action을 통해 실제 URL에 데이터를 전달
def fack(request):
    return render(request, "articles/fack.html")

# 서버로 데이터를 전달할 Form 태그를 사용하는 템플릿 연결 View 함수
def throw(request):
    return render(request, "articles/throw.html")

# 서버로 넘어온 데이터 처리
def catch(request):
    # GET 요청을 통해 전달받은 데이터를 가져옴
    message = request.GET.get("message")
    context = {
        "message": message
    }
    return render(request, "articles/catch.html", context)

# URL 패턴의 일부분을 정수 형태의 변수로 전달받아 사용하는 View 함수
def num(request, num):
    context = {
        "num":num
    }
    return render(request, 'articles/num.html', context)

# URL 패턴의 일부분을 문자열 형태의 변수로 전달받아 사용하는 View 함수
def content(request, content):
    context = {
        "content":content
    }
    return render(request, 'articles/content.html', context)


