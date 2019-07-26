# Find the Duplicate Number

[leetcode](https://leetcode.com/problems/find-the-duplicate-number/) (2019.07.26)

![image](https://user-images.githubusercontent.com/40231980/61840873-a9b12b80-aecd-11e9-9f6e-0de44dadd433.png)

### # 문제

주어진 배열에서 반복된 숫자가 존재하는 경우 반환.

### # 해결

- `nums`정렬한다.
- 반복문 돌면서 현재 값과 다음 값이 일치하는 경우 => 중복되었으므로 값을 반환한다.

![image](https://user-images.githubusercontent.com/40231980/61840963-f268e480-aecd-11e9-95fb-7b6734549e99.png)
