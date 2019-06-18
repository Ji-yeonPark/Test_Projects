# todo-vue
---

### :star: Electron + Vue 

---

## Part 1. [Vue.js Todo App - Basics - Part 1](https://www.youtube.com/watch?v=A5S23KS_-bU&list=PLEhEHUEU3x5q-xB1On4CsLPts0-rZ9oos)

1) install
  > $ npm i sass-loader node-sass  --save

- TodoList 생성

<br/>

## Part 2. [Vue.js Todo App - Component Communication - Part 2](https://www.youtube.com/watch?v=4WwzOZzoUUg&list=PLEhEHUEU3x5q-xB1On4CsLPts0-rZ9oos&index=2)

- TodoList 에서 TodoItem 분리

<br/>

## Part 3. [Vue.js Todo App - Event Bus - Part 3](https://www.youtube.com/watch?v=7AXiN5mrOgY&list=PLEhEHUEU3x5q-xB1On4CsLPts0-rZ9oos&index=3)

- TodoList 에서 EventBus를 이용해서 TodoCheckAll, TodoClearCompleted, TodoFiltered, TodoItemsRemaining을 분리 후 이벤트 연결

<br/>

## Part 4. [Vue.js Todo App - Vuex - Part 4](https://www.youtube.com/watch?v=yrCGcnn4_RU&list=PLEhEHUEU3x5q-xB1On4CsLPts0-rZ9oos&index=4)

- **Vuex** : 중앙 집중식 저장소 역할

1) install
  > $ npm i vuex --save

<br/>

## Part 5. [Vue.js Todo App - Laravel API - Part 5](https://www.youtube.com/watch?v=Ork8274eqYo)

1) install
  의존성 관리를 위해 **컴포저**를 통해 laravel 설치한다.
  - 컴포저 설치 : https://getcomposer.org
  - laravel 설치 : 
    > $ composer global require laravel/installer

2) 프로젝트 생성
    > $ laravel new todo-laravel<br/>
    > $ cd todo-laravel<br/>
    * controller, model, factory, migration 생성.
    > $ php artisan make:model Todo -a

### Electron + MySql
1) install
  https://www.npmjs.com/package/mysql
  > $ npm install mysql --save




