# ReactJS Foundmentals 노트 정리
---

[Nomad Coders - ReactJS로 웹 서비스 만들기](https://academy.nomadcoders.co/courses/enrolled/216871)

---

## props

- 부모가 자식에게 데이터를 전송.
- 자식은 부모의 데이터를 **props**를 이용하여 사용 가능.
- **PropTypes.타입**을 통해 부모로 부터 전달받은 데이터가 해당 `타입`이 아니면 에러가 발생하도록 할 수 있다.
```
$ yarn add prop-types
```
- **PropTypes.타입.isRequired**라고 작성할 경우 필수적으로 해당 prop이 있어야 한다. 

## map

- Array를 맵핑
- [MDN - map](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

## key error

![스크린샷 2019-05-22 오후 10 44 20](https://user-images.githubusercontent.com/40231980/58185589-57e1fe80-7cee-11e9-86fb-bf6615a8b152.png)
> Array에 있는 각 자식들은 반드시 고유한 `key prop`을 가져야 한다.

- 리액트는 엘리먼트가 많을 경우 **Key**를 줘야 한다.
- **Key**는 고유값이어야 한다.

## 리엑트 라이프 사이클 Lifecycle

- 컴포넌트는 여러 기능들을 정해진 순서대로 실행한다.
- render할 때, 즉 컴포넌트를 띄울 때, 이 순서대로 원하든 원치않든 자동으로 실행한다.
> componentWillMount() -> render() -> componentDidMount()

- update할 때는 다음과 같다.
> componentWillReceiveProps() -> shouldComponentUpdate() -> componentWillUpdate() -> render() -> componentDidUpdate()
```
ex) 
componentWillUpdate() : spinner 생성
componentDidUpdate() : spinner 제거
```


## state

- `state`가 바뀔 때마다 컴포넌트는 재 랜더 한다. (다시 render()호출)
- 아래와 같이 `state`값을 직접적으로 바꾸면 안된다.
```javascript
this.state.키 = "값"

// 결과
// Warrning.  Do not mutate state directly.
```
- 직접적으로 변경하면 render 설정들이 작동을 안한다.
- <b>this.setState({})</b>를 이용해야 한다.


## functional component

- **class component** 와 다른점
  - `state`를 사용할 수 없다.
  - `render()`함수도 사용할 수 없기 때문에 `라이프사이클`이 없다.
  - 오직 `return`만 있다.

아래 두 개는 같은 기능을 하는 컴포넌트이다.
```javascript
// class component ( smart component )
class MoviePoster extends Component {

    static propTypes = {
        poster: propTypes.string.isRequired
    }
    render () {
        return (
            <img src={this.props.poster} alt="Movie Poster"></img>
        )
    }
}
```
```javascript
// functional component ( dumb component )
function MoviePoster({poster}) {
    return (
        <img src={poster} alt="Movie Poster"></img>
    )
}

MoviePoster.propTypes = {
    poster: PropTypes.string.isRequired
}
```

## FETCH

- URL의 데이터를 불러옴
- ajax는 url을 자바스크립트로 asynchronous비동기화 방법으로 불러옴.
- AJAX를 쓰는 이유? 뭔가를 불러올 떼 새로고침을 하지 않고서 자바스크립트와 같이 데이터를 다룰 수 있다. 
- `fetch` 작업이 (성공하든말든) 끝나면 `then`을 실행헤라. <br/>
   만약, 에러가 발생하면 `catch`를 실행한다.
```javascript
fetch('')
.then(
    response => console.log(response)
)
.catch(err => console.log(err))
```
- `fetch`의 결과인 `then` 함수는 항상 Object형식의 1개의 attribute만 준다.
- 참고로 `화살표 표시(=>, arrow function)`는 return이 내장되어 있기 떄문에 return을 따로 작성할 필요가 없다.

## Promise

- 최신 자바스크립트 컨셉임
- asynchronous programming 동기
- 앞선 작업이 끝나든 말든 다음 작업을 진행.
- `fetch ... then ... catch`


## Await / Async

- `async`은 이전 라인의 작업이 끝날떄까지 기다리지 않고 순서와 상관없이 진행된다.
- `await`는 이전 작업이 기능이 끝나는 것을 기다린다.(성공 여부와 상관없이)
- id를 사용하는 이유는 컴포넌트의 key는 인덱스를 사용하면 느리기 때문이다.
- `componentDidMount`에 많은 코드를 가지고 있는 것은 좋지 않기 때문에(콜백지옥에 빠질수도 있음) 함수별로 정리한 후 넣는 것이 기능별로 넣을 수 있고 수정도 용이하다.

## lines-ellipsis

```
$ yarn add react-lines-ellipsis
```

## gh-pages

- 깃허브에 프로젝트로 올린 프론트엔드 파일들을 무료로 호스팅해줌. (백엔드X)
- 깃허브는 코드를 보여줄 뿐 실행하진 않기 때문.
- 단, 브랜치가 있어야하며, 해당 브랜치 이름은 `gh-pages`이야만 한다.
- 프로젝트명, 유저명과 함께 웹사이트에 보여짐

방법
1. 아래 셋 중 한가지 명령어 이용해서 css 압축하여 `build`폴더에 넣음.
- `build`하면 좀 더 최적화되고, 압축, 더 향상된다.
```
$ yarn run start
$ yarn build
$ npm start 
```

2. `package.json`에 `key`추가
> 형식 : http://[깃허브유저명].github.io/[프로젝트명] <br/>
> "homepage" : "http://myname.github.io/myapp",


3. 파일을 수정했으므로 다시 `build`.

4. 브랜치 추가
```
$ yarn add --dev gh-pages
```

5. `package.json`에 스크립트(`scripts`) 추가
```
// ...
"scripts": {
    // ...
    "predeploy": "yarn build",
    "deploy": "gh-pages -d build"
}
```


6. `deploy` 실행
```
$ yarn run deploy
```