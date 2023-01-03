[장고 특징](#장고-특징)

[장고 용어 및 핵심 기능](#장고-용어)

[장고 프로젝트 만들기 및 APP구축](#장고-프로젝트-및-명령어와-mvt-만들기)

[장고 templates사용법](#template사용법)

[GET|POST 이론](#GET-POST-이론)

[model활용방법](#model사용법)

[HTML_CSS 적용강령](#HTML_CSSwithDjango)

[Login기능구현](#Login)

[만약오류|동작이 이상하다면](#오류-강령)


# 장고 특징

1. Elegant URL : 바로이동[Django의 URL](#중요개념-urlconf)
    - URL을 직관적이고 쉽게 표현할 수 있음. 그리고 URL 자체를 파이썬 함수와 연결시키기 때문에 개발이 편리
2. 다국어 지원

3. `테스트용 웹 서버를 실행(runserver) 상태에서 소스 파일 수정시 즉시 반영`



# template사용법
    1. base 템플릿 생성시
        1. project 폴더의 바로 하위에 template 폴더를 넣는다. 이 때 폴더이름은 반드시 settings.py 의 템플릿 DIRS에 명시된 이름이어야 한다
            - E.G : base template 폴더이름 : basetemplate, TEMPLATES=[{~~, "DIRS" :["basetemplate"]}]
    2. application 폴더안에 템플릿 생성시
        1. 반드시 template폴더 - app이름과동일한폴더 - .html 파일들 , 구성으로 생성되어야 한다
            1. template 폴더는 반드시 settings.py template에 명시된 이름이어야 한다
            2. app이름과 동일한 폴더가 아니면 오류가 난다




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

- 템플릿 시스템
    - templates 시스템은 장고의 templates 문법 으로 작성된 템플릿 코드를 해석해서 템플릿  파일을 결과로 낸다
    - rendering : 장고의 템플릿 코드를 템플릿 파일로 해석하는 과정을 의미한다
    
    - **템플릿 변수**
        - 사용법 : {{ 변수 }} : 템플릿 시스템에서 변수를 평가, dot 표현도 가능한데 파이썬과 조금 다름. variable.var 이면 variable이 dictionary인지 체크해서 맞다면 variable['var']로 해석후 바로 value값 찾음. 아니면 리스트인지 체크해서 varianle[var]로 해석. 만약 정의가 안 되어있다면 빈 문자열 '' 로 채움.
    - **템플릿 필터**
        - 사용법 : {{ variable|템플릿필터용어|템플릿필터용어:인자|... }}
            - 템플릿 필터 용어 
        - 필터 종류
            1. length : 대부분의 필터가 string을 반환해서 산술연산이 불능, 그러나 이것은 예외적으로 가능
                - e.g : {%if nameleng|lengh >10 %}, 이름길이가 10보다 크면을 의미한다
    - **템플릿 태그**
        - 설명 : 태그는 좀 복잡하다, 어떤 거는 시작태그만 있어도 되나 어떤 거는 시작과 끝맺음을 하는 태그가 있어야한다

        - 태그 사용법 : {% tag명 %}

        - 대표 태그
            1. {% for %}
                - e.g
                    ```
                    {% for names in athlete%} <li>{{names.name}}{%endfor%}
                    ```
                - for tag 사용시 사용가능한 변수 179 page
                    1. forloop.couter
            2. {%if _ %} {%elif _ %} {%else%} {%endif%}
                - 추가 사용가능 예
                    1. {% if names|length > 1 %}
                    2. and ,or ,not ,and not ,== , != , <, > , <= , >= , in , not in 등을 사용할 수 있다
            3. {%csrf_token%} : Cross Site Request Forgery 라는 공격을 방지하기 위해 사용하는 태그. Post를 진행하는 <form> 태그를 사용하는 탬플릿 코드에 사용한다, <form> 태그에는 악의적인 스크립트 문장이 있을 수 있기 때문이다. 절대 외부 URL로 보내는 <form> 태그에는 사용하면 안된다, 토큰값이 유출되면 무의미하다
                - CRSF 공격 : 특정 웹사이트에서 이미 인증을 받은 사용자를 통하여 공격하는 방법, 인증된 사용자임으로 들어오는 코드를 그대로 수용하게 되는 약점을 노린 것
                - 사용법 : <form>태그 바로 다음에 넣어주면 된다.
            4. {%url%} : 
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

0. python manage.py makemigrations : models.py에 만든 내용을 DB와 직접적으로 연동시킬 PYTHON FILE(생성한 app 파일 안에 migrations.py)에 수정/생성 부분 작성

1. python manage.py migrate : DB에 변경사항(MODEL 의 추가 삭제 등..)이 있을 때 반영하기 위해 사용
    - ERROR 발생 사항, makemigrations 안 할 시
    ```
    Your models in app(s): 'vote' have changes that are not yet reflected in a migration, and so won't be applied. 
    Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
    ```
    
2. python manage.py createsuperuser : admin 진입시 사용할 id/비번

3. python manage.py runserver 0.0.0.0:8000 : admin 진입하기위한

### MVT 만들기

1. Model : DB 만들기
    - App 폴더의 models.py를 수정한다

# GET POST 이론

1. GET : DB에 있는 속성, PARAMETER 접근. 주소 안에다 "/?파라미터이름=값" 의 형태로 URL 진입
    - 최초 url 진입시엔 GET으로 진입하게 된다
2. POST : CREATE , UPDATE 방식. 서버 내 어떤 정보를 수정|생성할 때 사용함. 
    - 사용법 : HTML 에 form 태그를 사용한다
    - form 태그 : 어떤 파일, 많은 데이터 등이 POST의 BODY에 담기는데 이것을 모두 담는 태그.
        - action 속성 : form 태그가 활성화 되면 이동할 위치, 반드시 URL에 "/~/" 처럼 /으로 시작해서 끝나야함. 오류남!
        
# model사용법
- 설명 : 모든 저장되는 내용은 db.sqlite3 에 저장된다

- view함수에서 model 클래스를 불러와서 변수에 저장하고 해당 변수.save() 하면 ㅇㅋ


# HTML_CSSwithDjango

- 사전 요건 및 지식
    1. settings.py에 보면 STATIC_URL 이 있다, 이것은 APP마다 STATIC을 적용시 STATIC파일 명을 사전에 알려주는 것이다
        - e.g : url진입시 urls.py에 정의된 최초 진입로(page app일 때 진입을 "pages/"로 하면 pages)/static/~ 을 찾는다.
    2. 특정 app안에 구속되지 않은 base static 을 만들어야만 한다면 settings.py에 STATICFILES_DIRS=[경로]를 지정한다.
        - e.g : STATICFILES_DIRS=[BASE_DIR+"/"+"basestatic"]
    3. BASE html작성시 css등 static 파일이 필요하면 2번을 만족을 시켜야만한다
        - e.g
            1. base.html에서 .css 불러오기 
                ```
                <link rel="stylesheet" href="{% static 'css/style.css' %}"> # css폴더 안에 있는 style.css를 불러온다. 경로가 사전에 정의되어 있어서 찾을 수 있다
                ```
            2. style.css에서 img 불러오기
                ```
                .home-hero{
                    background : url("../images/this.jpg") # 같은 static폴더 안에 있는 images 폴더에서 사진을 가져온다
                }
                ```


# Login
- views.py : login 기능을 구현
    - 진입 형태
        ```
        def login(requs):
            ~~
        ```
    설명 : view함수는 기본적으로 html에서부터 변수를 가져온다. 따라서 모든 함수에는 requst 변수가 있고 이 안에 html에서 넘어온 모든 정보가 담겨 있다
    - 변수 설명 
        0. requs : html에서 넘어왔을 때 
        - 속성
            1. user : django가 기본적으로 제공하는 변수. views를 통해 html 생성시 모든 html에서 user.로 변수 접근 가능. view에선 req.user 으로 html에선 그냥 user. 으로
                - Attribute
                    1. req.user.id : user의 DB에 있는 id를 출력
                        - 로그인 안 되어 있을 때 :None
                    2. req.user.is_active : 활성화 되어 있는 지
                        - 로그인 안 되어 있을 때 : False

                    3. req.user.is_anonymois : 현재 접속한 사용자가 회원인지(False) 아닌지(True)

                    4. req.user.is_authenticated : 현재 접속한 사용자가 회원인지(True) 아닌지(False)

                    5. req.user.pk
                        - 로그인 안 되어 있을 때 :None

                    6. req.user.user_permissions : 
                        - 로그인 안 되어 있을 때 : auth.Permission.None
             2. POST / GET : dict 비슷한 형태로 값들이 넘어옴. form 태그 안에 있는 모든 값들이 name:value 형태로 넘어옴
                - Attribute
                    1. requs.POST.get(name) : name 키에 맞는 value가 넘어옴
                    2. 이외 다양한 함수들이 있는데 사실상 dict형태로 특정 값을 가져오는 거라 1만 잘 써도 ㅇㅋ
             3. get_host() : 현재 사이트에 진입을 허용한 url의 HOST 주소를 가져옴
                - 사용법 requs.get_host() : 127.0.0.1:8000
             4. get_full_path() , get_full_path_info() : HOST 제외 현재 사이트를 보기위한 진입 PATH를 모두 알려줌
                - 사용법 requs.get_full_path() : /account/login/ 
             5. method : GET / POST 중 하나
                - 사용법 : requs.method
                
- models
    
# 오류 강령

1. settings.py 에 INSTALLED_APPS 변수에 추가된 Application 주소를 다시 체크한다
