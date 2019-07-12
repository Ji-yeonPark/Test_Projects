# Spiral Matrix

[leetcode](https://leetcode.com/problems/spiral-matrix/) (2019.07.12)

![image](https://user-images.githubusercontent.com/40231980/61098924-a06e9a80-a49b-11e9-9e57-cdd4d623537e.png)

### # 문제

2차원 배열(matrix)를 달팽이 모양으로 읽기.

### # 해결 1

- [오른쪽, 아래, 왼쪽, 위] 순서대로 방문하게 된다. <br/>
  direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] <br/>
- 모든 값을 False를 갖는 2차원 배열을 만든 후 방문한 곳은 True로 변경 한다.

![image](https://user-images.githubusercontent.com/40231980/61099108-36a2c080-a49c-11e9-8124-56271b867895.png)
