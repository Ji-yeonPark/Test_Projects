# Sort Colors

[leetcode](https://leetcode.com/problems/sort-colors/) (2019.07.30)

![image](https://user-images.githubusercontent.com/40231980/62094295-93351680-b2b7-11e9-96eb-c80eb115495b.png)

### # 문제

빨간색, 흰색 또는 파란색으로 색상이 지정된 n개의 객체가 있는 배열을 동일한 색상의 객체가 빨간색, 흰색 및 파란색의 순서로 인접하도록 객체를 정렬.

0: 빨간색, 1: 흰색, 2: 파란색을 나타냄.

단, 정렬 라이브러리 사용 불가.

### # 해결 1

- `버블 정렬` 이용함.
  - 인접한 두 요소 비교해서 앞의 요소가 더 클 경우 두 요소 위치 바꿈.
  - O(n^2)으로 느림.

![image](https://user-images.githubusercontent.com/40231980/62094287-887a8180-b2b7-11e9-8ffe-0cedbc88d5db.png)

### # 해결 2

- `선택 정렬` 이용함.
  - 리스트에서 가장 최솟값을 찾은 후
  - 최소값을 맨 앞 요소와 위치 바꾼다.
  - O(n^2)으로 느림.

![image](https://user-images.githubusercontent.com/40231980/62094473-3ede6680-b2b8-11e9-8f7d-767df9d51f3b.png)
