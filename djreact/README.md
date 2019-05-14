## Django-React Tutorial ##


### Chapter 01. Creating a Fullstack Application

- [YouTube](https://www.youtube.com/watch?v=uZgRbnIsgrA)
- [blog - django projects in visual studio code](https://automationpanda.com/2018/02/08/)
- [create-react-app](https://github.com/facebook/create-react-app)
> npm init react-app gui
- [ant design](https://ant.design/)
> npm install antd --save

> npm install axios --save

- [django-cors-headers](https://github.com/ottoyiu/django-cors-headers)

- > npm install react-router-dom --save

- **django-rest-framwork**
  - ListAPIView : read-only. Get만 사용 가능 즉, <form> POST사용 불가 collection of model instances.
  - RetrieveAPIView : read-only. GET만 사용 가능. 단일 값(Single model Instance)만 출력


<br/>

### Chapter 02. Handling Post Requests

- [YouTube](https://www.youtube.com/watch?v=w-QJiQwlZzU)
- [projectCode](https://github.com/justdjango/DjReact)


- **django-rest-framwork**
  - ListCreateAPIView : read-write. GET, POST 둘 다 지원. collection of model instances.
  - CreateAPIView : create-only. POST 방식
  - UpdateAPIView
  - DeleteAPIView

<br/>
1.

`ViewSet`을 이용하면 ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView 한번에 정의 가능하다.<br/>
또한 ListAPIView경로로 접속 시 바로 데이터 추가(CreateAPIView)가 가능하며, <br/>
RetrieveAPIView 방식으로 특정 PK 갖는 요소로 접근할 경우 해당 요소를 수정(UpdateAPIView), 삭제(DestroyAPIView) 가능하다.

<br/>
2.

React에서 Create/Update/Delete 기능 구현.