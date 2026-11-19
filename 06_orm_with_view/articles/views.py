from django.shortcuts import render
from .models import Article # 현재 앱에서 작성한 Model Class import
# Create your views here.

# 전체글 조회 view 함수
def index(request):
    # QuerySet API all 메서드를 통해 데이터베이스 내(SQLite) articles_article 테이블에 존재하는 모든 데이터 조회
    articles = Article.objects.all()

    # template에서 사용할 데이터 객체 생성
    context = {
        'articles': articles
    }

    # template 렌더링
    return render(request, 'articles/index.html', context)

# 단일 데이터를 조회하는 view 함수
# - articles/urls.py 에서 Variable Routing을 통해 추출한 pk 값을 전달받음
# - request(:HTTP 요청 객체) 다음에 pk를 매개변수로 선언
# - 전달받은 pk를 이용해 ORM으로 단일 데이터 조회
def detail(request, pk):
    # QuerySet API get() 메서드 호출 
    # - 데이터베이스 articles_article 테이블 내 pk 속성값이 pk인 데이터 조회
    # - ORM을 통해 조회된 데이터를 Model Instance로 반환
    article = Article.objects.get(pk=pk)

    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)


