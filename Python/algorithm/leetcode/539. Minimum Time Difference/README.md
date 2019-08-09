# Minimum Time Difference

[leetcode](https://leetcode.com/problems/minimum-time-difference/) (2019.08.09)

![image](https://user-images.githubusercontent.com/40231980/62670438-324fc180-b9ce-11e9-917d-94c2d34d3463.png)

### # 문제

"Hour:Minutes" 포멧으로 된 24시간 timePoints 리스트가 주어짐.  
리스에서 두 개의 최소 시간 차이를 분 단위로 반환.

### # 해결

- `timePoints`를 분 단위`시간 * 60 + 분`로 모두 변경하여 리스트에 넣는다.
  - 이때, 12시간 미만의 시간들은 24시간을 더한 값도 같이 넣어준다.
  - ["23:49", "22:01", "00:01"]이 존재하는 경우 "23:49"와 "00:01"의 차이가 가장 작기 때문이다.
- 반복문을 실행하면서 가장 큰 값 두개씩 비교해서 `min`최소값을 비교한다.
  - min 이 0 이 되면 이보다 작은 차이 값은 없기 때문에 바로 반환해준다.

![image](https://user-images.githubusercontent.com/40231980/62672176-94abc080-b9d4-11e9-93db-27bb384aea6f.png)
