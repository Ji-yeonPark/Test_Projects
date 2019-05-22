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

