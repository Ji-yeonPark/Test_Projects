# Rotate Array

[leetcode](https://leetcode.com/problems/rotate-array/) (2019.08.06)

![image](https://user-images.githubusercontent.com/40231980/62505230-b8d19b00-b836-11e9-9ea6-91e04e0c67c8.png)

### # 문제

`NUMS` 뒤에서부터 `k`만큼 `NUMS` 앞으로 옮기기.

### # 해결 1

반복문을 이용한 방법이다.

- `k`만큼 반복하면서 맨 뒤의 요소를 `nums`맨 앞에 추가(insert)해 준다.
- 반복문을 사용했기 때문에 속도가 매우 느리다.

![image](https://user-images.githubusercontent.com/40231980/62505185-7314d280-b836-11e9-9076-aa8bcd331f3a.png)

### # 해결 2

반복문(While, For)을 제거한 풀이 방법이다.

- `nums` 리스트를 전체 복사한 후 `K`만큼 잘라서 변경해준다.

![image](https://user-images.githubusercontent.com/40231980/62505047-0699d380-b836-11e9-86b2-ce4b6582abef.png)
