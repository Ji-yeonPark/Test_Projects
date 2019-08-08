# Sort Array By Parity II

[leetcode](https://leetcode.com/problems/sort-array-by-parity-ii/) (2019.08.08)

![image](https://user-images.githubusercontent.com/40231980/62669222-cec39500-b9c9-11e9-90a4-dcc176cb718c.png)

### # 문제

주어진 리스트 `A`를 짝수는 짝수번 인덱스에, 홀수는 홀수번 인덱스에 넣어 정렬.

### # 해결

- 결과를 담을 빈 리스트 `B` 생성
- 짝수 인덱스 `even`, 홀수 인덱스 `odd`생성
- 반복분을 실행하면서,
  - 값이 짝수이면 B의 짝수 인덱스에 값을 추가하고 `even += 2`
  - 값이 홀수이면 B의 홀수 인덱스에 값을 추가하고 `odd += 2`

![image](https://user-images.githubusercontent.com/40231980/62669226-d5eaa300-b9c9-11e9-819f-037ea14ca8fd.png)
