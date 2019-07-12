# Spiral Matrix II

[leetcode](https://leetcode.com/problems/spiral-matrix-ii/) (2019.07.12)

> [54. Spiral Matrix](https://github.com/Ji-yeonPark/TIL/tree/master/Python/algorithm/leetcode/54.%20Spiral%20Matrix)와 비슷한 문제.

![image](https://user-images.githubusercontent.com/40231980/61099238-9600d080-a49c-11e9-9a02-9e6309102639.png)

### # 문제

2차원 배열(matrix)를 달팽이 모양으로 숫자 넣기.<br/>

### # 해결 1

- [오른쪽, 아래, 왼쪽, 위] 순서대로 방문하게 된다. <br/>
  direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] <br/>
- 모든 값을 False를 갖는 2차원 배열을 만든 후 방문한 곳은 True로 변경 한다.

![image](https://user-images.githubusercontent.com/40231980/61099208-83869700-a49c-11e9-9796-884d2f7669f2.png)
