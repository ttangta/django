## 0. Django Framework

**Django란?**

Django는 Python 프로그래밍 언어를 기반으로 웹 애플리케이션을 효율적으로 개발할 수 있도록 다양한 기능을 제공하는 웹 프레임워크(Web Framework)

**Django의 주요 특징**

- Python 기반 : Python 언어를 사용하여 웹 애플리케이션 개발
- MTV 패턴 : Model, View, Template으로 역할을 분리
- ORM 지원 : Python 코드를 사용하여 데이터베이스 조작
- 기본 기능 제공 : URL Routing, 사용자 인증, 관리자 페이지, 보안 기능 등
- Project와 App 구조 : 하나의 프로젝트 안에서 기능별로 여러 앱을 구성할 수 있음

**Django의 MTV 패턴**

|구성 요소|역할|
|:---:|---|
|Model|데이터베이스와 관련된 데이터 구조 및 처리|
|View|클라이언트의 요청 처리 및 응답 생성|
|Template|사용자에게 보여줄 HTML 화면 구성|

**Django의 기본 동작 흐름**

1. Client -> Django 서버에 HTTP 요청
2. URL Dispatcher -> 요청 URL에 해당하는 View 연결
3. View -> 요청 처리 및 필요시 Model을 통해 데이터 조회
4. Template -> 전달받은 데이터를 활용하여 HTML 생성
5. Response -> 클라이언트에 HTTP 응답

| Model과 Template은 필요한 경우에 사용된다.

**Django Project 와 App**

- Project : Django 웹 애플리케이션의 전체 설정과 구성을 관리하는 단위
- App : 게시글, 회원 관리 등 특정 기능을 담당하는 단위

## 1. 가상환경 설치 및 활성화/비활성화

```bash
# 1. 가상환경 설치
python -m venv venv₩
# macOS 가상환경 설치
python3 -m venv venv

# 2. 가상환경 활성화
source venv/Scripts/activate
# macOS 가상환경 활성화
source venv/bin/activate
echo $VIRTUAL_ENV # 경로 출력 = 활성화, 경로 미출력 = 비활성화

# 3. 가상환경 비활성화
deactivate
```

## 2. 가상환경에 django install

```bash
# 가상환경이 활성화 된 상태 기준
# 1. django 설치
pip install django

# 2. 가상환경에 설치된 의존성 패키지 확인
pip list

# 3. 의존성 기록
pip freeze > requirements.txt

# 4. 의존성 가져오기
pip install -r requirements.txt
```

![django 설치 성공](./images/django_success_install.png)

![가상환경에 설치된 패키지 확인](./images/django_dependencyPackages.png)

![의존성 기록 결과](./images/의존성기록텍스트파일.png)

## 3. Django 프로젝트 생성 및 서버 실행

```bash
# 프로젝트 생성
django-admin startproject firstpjt .

# 서버 실행
python manage.py runserver
```

![django 프로젝트 생성](./images/django프로젝트%20생성.png)

![django 서버 실행](./images/django%20서버실행.png)

![django 서버 실행결과](./images/django%20서버실행%20결과.png)