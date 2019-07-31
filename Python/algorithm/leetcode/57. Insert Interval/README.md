# Insert Interval

[leetcode](https://leetcode.com/problems/insert-interval/) (2019.07.31)

![image](https://user-images.githubusercontent.com/40231980/62177835-63524580-b381-11e9-8857-eabe5718c73f.png)

### # 문제

newInterval 값을 추가하여 주어진 간격 집합에서 겹치는 구간 존재시 병합하기.

( 처음 시작할 때 intervals값은 정렬되어 있다. )

### # 해결

- [LEETCODE 56. Merge Intervals](https://github.com/Ji-yeonPark/TIL/tree/master/Python/algorithm/leetcode/56.%20Merge%20Intervals) 문제와 비슷하다.
- `newInterval`값을 `intervals`에 추가 한 후 정렬한다.
- 반복문을 돌면서 아래 조건에 맞는지 체크한다.
  - **list[-1][-1] >= cur[1]** : 무시 <br/>
    ex) list[-1] = [1, 5] / cur = [2, 3]
  - **list[-1][-1] >= cur[0]**: list의 마지막 요소를 [list[-1][0], cur[-1]]로 변경
    ex) list[-1] = [1, 5] / cur = [2, 8]
  - 그 외: 무조건 추가

![image](https://user-images.githubusercontent.com/40231980/62177847-6e0cda80-b381-11e9-8b16-491ed5007e7d.png)
