# Valid Parentheses

[leetcode](https://leetcode.com/problems/merge-intervals/) (2019.07.11)

![image](https://user-images.githubusercontent.com/40231980/61039520-dfeca680-a409-11e9-8cc9-31a9fc674118.png)

### # 문제

주어진 간격 집합에서 겹치는 구간 존재시 병합하기.

### # 해결

- 변수 `list` : 결과를 담는 변수
- 주어진 리스트(intervals)를 정렬한다.
- 반복문을 돌면서 아래 조건에 맞는지 체크한다.
  - **list[-1][-1] >= cur[1]** : 무시 <br/>
    ex) list[-1] = [1, 5] / cur = [2, 3]
  - **list[-1][-1] >= cur[0]**: list의 마지막 요소를 [list[-1][0], cur[-1]]로 변경
    ex) list[-1] = [1, 5] / cur = [2, 8]
  - 그 외: 무조건 추가

![image](https://user-images.githubusercontent.com/40231980/61039506-d82d0200-a409-11e9-81a9-253245324d2f.png)
