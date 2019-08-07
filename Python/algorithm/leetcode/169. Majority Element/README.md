# Two Sum II - Input array is sorted

[leetcode](https://leetcode.com/problems/majority-element/) (2019.08.07)

![image](https://user-images.githubusercontent.com/40231980/62591334-3fa37800-b90a-11e9-9034-b1de3d5affac.png)

### # 문제

리스트 `nums`애서 가장 많이 반복된 값 반환.

### # 해결 1

collections의 Counter 이용

- Counter의 `most_common`을 이용해서 가장 많이 반복되어 사용된 값 반환한다.
  - https://docs.python.org/2/library/collections.html#collections.Counter.most_common

![image](https://user-images.githubusercontent.com/40231980/62591070-61e8c600-b909-11e9-9352-d55658b33c16.png)

### # 해결 2

collections의 defaultdict 이용.

- for 를 이용하여 값을 `defaultdict`에 누적한 후 `MAX` 값 반환한다.

![image](https://user-images.githubusercontent.com/40231980/62591070-61e8c600-b909-11e9-9352-d55658b33c16.png)
