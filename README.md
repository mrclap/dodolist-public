# dodolist
dodolist는 **'나의 할 일'**을 관리할 수 있는 간단한 'todo 웹 어플리케이션 입니다'.

위 프로젝트는 **프로그래머스에서 진행하는 '섬머코딩'의 2차 과제를 목적**으로 작성되었습니다.

## 소감
Django REST Framework와 Draggable기능을 사용해 프로젝트를 진행하였습니다.

1. Django REST Framework는 시간에 쫓겨 제대로 사용하지 못했으나 시간을 갖고 보아야겠습니다.

2. Draggable에 의해 실시간으로 변경되는 DOM의 순서를 DB에 반영하는 것이
    - 프로그램의 복잡도를 엄청나게 증가시키며 (물론 제가 못해서 입니다.)
    - React, Vue와 같은 라이브러리를 왜 사용해야하는지.. 그 필요성을 크게 느꼈습니다.


## website
[dodolist](http://dodolist.tk/)

## 기능 요구 사항 및 구현 상세
| 요구사항 | 구현 상세 |
|------|-------|
|새로운 TODO()(제목과 내용)을 작성할 수 있다.|구현 페이지 상단에 [엔터키] 혹은 버튼을 통해 작성 가능|
|TODO 목록을 볼 수 있다.|TODO의 작성과 확인이 동시에 가능한 Single page application |
|TODO 항목의 제목과 내용을 수정할 수 있다.|각 TODO를 클릭하여 'Modal'에서 수정|
|TODO 항목을 삭제할 수 있다.|삭제하고자 하는 TODO를 클릭하여 'Modal'에서 삭제 버튼을 눌러 삭제|
|사용자의 선택에 의해 TODO에는 마감 기한을 넣을 수 있다.|TODO 추가/수정시 datepicker를 통해 마감기한 입력|
|TODO항목의 우선 순위를 설정 및 조절 할 수 있다.|리스트의 TODO를 **Drag&Drop하는 것으로 우선순위**를 설정|
|TODO항목에 대한 완료처리를 할 수 있다.|TODO 왼편의 **checkbox를 클릭**하여 완료처리/완료취소처리 가능 |
|마감기한이 지난 TODO에 대해 알림을 노출할 수 있다.| 마감기한이 지나면 마감기한이 파란색->**빨간색**으로 변경(1분 마다 체크)|


## 인터페이스 요구사항
직관적이고 의미 전달이 명확한 화면을 사용자에게 제공한다.

| 인터페이스 구분 | 구분 상세 | 구현 상세 |
|------------|---------------|---------|
|TODO 추가| TODO 타이틀 입력|제목 입력 후 [엔터키] 입력 시 자동 추가<br>_(TODO 특성상 제목만 빠르게 입력하는 경우를 고려)_|
|TODO 추가| TODO 마감기한 입력| - Datepicker를 이용하여 달력을 보면서 입력 가능 <br>- *190520 1200*의 형식으로 숙련사용자의 간편입력 고려|
|우선순위 변경| 우선순위 변경 | Drag&Drop을 이용하여 직관적 방법으로 우선순위 변경 |
|완료처리| 완료처리 | Checkbox를 클릭하여 완료처리 (affordance) |
|완료처리|완료취소처리| Checkbox를 재차 클릭하여 완료취소처리가 가능 (affordance) |
|완료처리|완료된TODO| 완료된 TODO를 화면 하단에 취소선과 함께 표기 |

## 성능 요구 사항 
- TODO 이용 시 발생하는 오류 사항을 최소화한다.
- 오류 발생 시 사용자가 이해하기 쉽게 표시한다.
- 다른 사람이 읽기 쉬운 코드를 작성한다.
- HTML/CSS에서 사용할 수 있는 최신 구조와 기술을 사용한다.

## 개발환경
- python 3.5.2 이상
- Django 2.2.1
- mySQL
- AWS


## 주요 사용 library
- [Django REST framework](https://www.django-rest-framework.org/)
- [JQuery 3.4.1](https://jquery.com/)
- [Bootstrap 4.3](https://getbootstrap.com/docs/4.3/getting-started/download/)
- [draggable](https://shopify.github.io/draggable/examples/simple-list.html)
- [Tempus Dominus - datepicker](https://tempusdominus.github.io/bootstrap-4/)

## 시작
```
# 1. 코드 내려받기
git clone https://github.com/mrclap/dodolist.git
cd dodolist

# 2. 가상환경 생성 및 실행
python -m venv venv
source venv/bin/activate

# 3. dependency 설치
pip install -r requirements.txt

# 4. dodolist > dodolist > setting.py의 DB설정(메일 계정 내용 참조-프로그래머스)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dodolist',
        'USER': ##########,
        'PASSWORD': #########,
        'HOST': ############,
        'PORT': '3306',
    }
}

# 5. Django를 이용해 로컬서버 실행
python manage.py runserver

# 6. 로컬서버 접속
```




## trouble shooting
- mysqlclient 설치 오류 시

```
apt-get install python3-dev libmysqlclient-dev gcc
pip install mysqlclient
```
