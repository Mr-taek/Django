[장고 특징](#장고-특징)

[장고 용어 및 핵심 기능](#장고-용어)

[장고 프로젝트 만들기 및 APP구축](#장고-프로젝트-및-명령어와-mvt-만들기)

[만약오류|동작이 이상하다면](#오류-강령)
# 장고 특징

1. Elegant URL : 바로이동[Django의 URL](#중요개념-urlconf)
    - URL을 직관적이고 쉽게 표현할 수 있음. 그리고 URL 자체를 파이썬 함수와 연결시키기 때문에 개발이 편리
2. 다국어 지원

3. `테스트용 웹 서버를 실행(runserver) 상태에서 소스 파일 수정시 즉시 반영`

# 장고 용어

### MVT

- Django workflow : URLconf - > View - > Model - > Template - > View -> client

- Django 코딩순서 (책에서 추천 + 나의 견해 추가) : Model - > Template - > View  - > URLconf

- MVC
    - M : Model, 데이터 , 개발자 역할
    - V : View, UI. UI 디자이너는 U만 신경쓰면 됨
    - C : Controller, LOGIC개발, 데이터 처리 , 개발자 역할
- M : Model , 데이터베이스에 access하는 역할, 데이터베이스에 저장되는 데이터
    - Django에서 알아서 DB를 만들어줌
    - 그래서 "파이썬 함수"로 DB를 만들고 접근함
    - ORM 이라고 하는 것임. Object-Relational Mapping : 즉 객체-관계 맵핑인데 객체는 인스턴스 또는 클래스|함수 이고 관계가 DBMS를 의미, 파이선 함수|클래스를 사용해서 DBMS와 같은 기능을 한다는 것.
    - 물론 직접 SQL을 사용해서 데이터 베이스 데이터를 가져올 수 있음

    - 따라서
        - TABLE - > Django의 CLASS
            - CREATE -> Django의 CLASS의 함수
            - READ - > Django의 CLASS의 함수
            - UPDATE - > Django의 CLASS의 함수
            - DELETE - > Django의 CLASS의 함수
- V : View , Client의 요청을 받고  요청을 돌려주는 역할, 실질적으로 LOGIC이 동작해서 데이터를 MODEL에서 가져오고 적절하게 처리해서 TEMPLATE에 전달시켜 UI를 띄우게 함
    - 함수 또는 클래스로 작성됨 , 웹 요청을 받고 DB접속 또는 Application Logic에 맞게 처리. 결과 데이터를 HTML로 변환|템플릿 처리 후 CLIENT에 반환
    - views.py 파일에 작성됨, 아무튼 settings.py 에서 경로에 명시되어야 함.
- T : Template , View로부터 데이터들을 받아 결과를 사용자에게 보여주는 UI역할
    - Django가 클라이언트에게 반환하는 최종응답은 HTML이고 이 HTML을 반환시켜줌
    - ".html로 작성이 됨"
    - setting.py 파일에 tempate들이 모여있는 경로를 명시해줘야 함.
- ? 그럼 M과 T의 차이는 무엇 ?

### <중요개념> URLconf
- URL은 클라이언트의 요청에 맞는 내용을 출력시켜주기 위한 통로이다, Django는 수정에 용이하도록 설계되어 있다

### <중요개념> Templates의 경로설정
- URLconf와 views를 작성할 때 자동으로 따라오는 것이 templates의 작성이다
- veiws에서 render 함수를 통해 호출할 .html 템플릿 파일을 불러오기 위해선 settings.py에 정의된 TEMPLATES의 위치가 필수이다. (103page)


- Django의 URL 분석방법
    0. url 요청이 들어옴
    1. setting.py 파일의 ROOT_URLCONF 항목을 읽어 모든 url이 모여있는 URLCconf 파일(urls.py)을 설정
    2. URLconf를 로딩해서 urlpattenrs 리스트에 있는 url들과 요청 url을 비교, 매치되는 패턴이 있을 시 그대로 매칭 url의 함수(view함수 또는 view class의 함수?)를 호출
    3. view에 요청할 때 넘어온 인자들을 다 넘겨버림
    4. 매칭되는 것이 없으면 에러를 처리하는 view를 호출


- 사용방법
    - Django에서 실행을 담당하는 곳 : urls.py

    - path(URL,실행할 함수(View의 함수)) : path함수가 url 패턴이 맞으면 함수를 실행시킨다.
        - URL패턴
            1. path("imhome/kbs/123/",view) : 정직한 패턴
            2. path("imghome<str:target>,view) : str 타입의 view함수의 target parameter의 str값을 넘겨줌
                - 장고의 url 패턴, <> :path converter
                    - 가능한타입
                        1. str: Default타입, "/"를 제외한 모든 문자(열)과 매칭. 
                        2. int: 0과 양의 정수랑만 매칭.
                        3. slug: ASCII, 숫자, 하이픈, 밑줄 과 매칭
                        4. uuid: UUID? 랑만 매칭한대
                        5. path: "/"를 포함한 걍 모든 문자열과 매칭함
            3. re_path(r"^imhome/(?P<year>\d{4})/(?P<time>\d+[-/]\d+([/-]\d+)?)",view함수) : 보통은 path()함수가 자주쓰이고 정교하게 정의할 때 사용함



### Application
- 순수의미 : 여러 프로그램이 뭉쳐져 기능을 하는 것
- 장고 : Application이 모여 Project가 되는 것
    - Project : 웹사이트에 관한 모든 프로그램
    - Application : Module화된 (특정 기능을 하게된 unit) 특정 기능을 하는 것
        - 하나의 Application은 여러 프로젝트에 포함될 수 있음



# 장고 프로젝트 및 명령어와 MVT 만들기

### 프로젝트 만들기
- 단계
    1. django-admin startpoject _name_ : name에는 프로젝트와 관련된 모든 파일들이 있음
        - name 생성시 name의 이름의 root 폴더와 name과 같은 이름의 자식 폴더가 있음. root폴더는 이름을 바꿔도 ㄱㅊ
        - 생성폴더 구조
            - `_name_`
                - `_name_`
                    - `__init__.py` : 이 파일이 있어야 파이썬 패키지로 인식한다고 함
                    - `asgi.py` : 
                    - `settings.py` : 프로젝트 설정 파일
                    - `urls.py` : URLconf, 모든 url을 모으는 장소
                    - `wsgi.py` : Web server gate interface , 아파치 등의 웹서버와 WSGI 규격을 연동하기 위한 파일
                - `manage.py` : Django의 명령어를 실행시켜주는 파일
    2. python manage.py startapp `_appname_` : Application을 만드는 명렁어, Django는 프로젝트 하나에 여러 특정 기능을 담당하는 Application이 있다
        - 생성폴더 구조
            - `_name_`
            - `appname_`
                - `migration` : DB (MODEL) 변경사항을 관리 DIR, CRUD 이 발생하면 변경 내역을 기록한 파일이 생김
                - `__init__.py` : 이 파일이 있어야 파이썬 패키지로 인식
                - `admin.py` : Django가 제공하는 Amin 사이트에 Model로 생성한 Model class를 등록해주는 파일
                - `apps.py` : 
                - `models.py` : Model calss를 정의하는 파일
                - `tests.py` : 모름
                - `views.py` : URLconf를 따로 정의가능하고, view 함수 , view class를 정의하는 파일
    - App을 만들었으면 URLconf를 지정해줘야함
        - 특징
            1. 접속경로는 appname/을 root로 한다
    3. URLconf
        
    3. App folder에 template 폴더 만들기 : App기능을 따로 하는 template을 만들어서 settings.py에 포함시키기가 가능하다
    - 생성 폴더의 용도
        - 
### 명령어

0. python manage.py makemigration

1. python manage.py migrate : DB에 변경사항(MODEL 의 추가 삭제 등..)이 있을 때 반영하기 위해 사용
    - ERROR 발생 사항, 0번 안 할 시
    ```
    Your models in app(s): 'vote' have changes that are not yet reflected in a migration, and so won't be applied. 
    Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
    ```
    
2. python manage.py createsuperuser : admin 진입시 사용할 id/비번

3. python manage.py runserver 0.0.0.0:8000 : admin 진입하기위한

### MVT 만들기

1. Model : DB 만들기
    - App 폴더의 models.py를 수정한다


# 오류 강령

1. settings.py 에 INSTALLED_APPS 변수에 추가된 Application 주소를 다시 체크한다