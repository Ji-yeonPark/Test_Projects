# 1026 보물

[백준](https://www.acmicpc.net/problem/1026) (2019.08.01)

![image](https://user-images.githubusercontent.com/40231980/62258710-6feca180-b446-11e9-9ea5-f5cb4b21b78f.png)

### # 문제

길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

`S = A[0]*B[0] + ... + A[N-1]*B[N-1]`

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. **단, B에 있는 수는 재배열하면 안 된다.**

**S의 최솟값**을 출력하는 프로그램을 작성하시오.

### # 해결

- B는 정렬하면 안된다는 조건이 명시되어 있기 때문에 `sort`는 사용할 수 없다.
- A를 반복문을 돌면서 A의 최솟값과 B의 최댓값을 `pop`하여 계산한다.

![image](https://user-images.githubusercontent.com/40231980/62258708-66fbd000-b446-11e9-9bee-a41e3419a76b.png)
