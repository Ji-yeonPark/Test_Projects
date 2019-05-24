# electron-vue-example

[YouTube - Electron with Vue.js](https://www.youtube.com/watch?v=Fl7---SEORQ)

---

- **Language**
  - Electron (Node.js)
  - Vue.js

- **modules**
  - vue-cli-plugin-electron-builder ([install](https://itinerant.tistory.com/106))
  - npm install electron-build
  - npm install axios

- **Configure**
  - Babel
  - Router
  - Vuex
  - Linter


<br/>


:star: **진행하면서 발견된 오류들 해결방법**

1. image.vue 창을 불러오려는데 `require` 를 찾을 수 없다는 오류 발생.
<img width="542" alt="스크린샷 2019-05-24 오후 11 55 29" src="https://user-images.githubusercontent.com/40231980/58338155-269a3780-7e82-11e9-9480-77ce0d8147e8.png">
-> `webPreferences` 에 `nodeIntegration: true`옵션 추가

<br/>
<br/>
<br/>

2. image.vue에 이미지를 불러오지 못하는 오류 발생.<br/>
   redd api 에서 이미지 url 접속시 `403 forbidden`에러 발생.<br/>
   -> URL에 &를 바꿔주면 된다. [[관련 내용](https://stackoverflow.com/questions/11504329/cannot-open-http-status-was-403-forbidden-the-sensor-parameter-specified)]
   <img width="330" alt="스크린샷 2019-05-25 오전 12 42 16" src="https://user-images.githubusercontent.com/40231980/58340128-184e1a80-7e86-11e9-8eac-aae02377943b.png">

   
<br/>

:good: **결과물**

<img width="800" alt="스크린샷 2019-05-25 오전 12 54 51" src="https://user-images.githubusercontent.com/40231980/58340841-c1e1db80-7e87-11e9-8e55-69cfa902f594.png">


<br/>
<br/>
<br/>

---

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn run serve
```

### Compiles and minifies for production
```
yarn run build
```

### Run your tests
```
yarn run test
```

### Lints and fixes files
```
yarn run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
