# Word Subsets

[leetcode](https://leetcode.com/problems/word-subsets/) (2019.08.12)

![image](https://user-images.githubusercontent.com/40231980/62843028-c03eeb80-bcf1-11e9-853f-1067d4ae5ae7.png)

### # 문제

두 문자열 `S` 와 `T`가 주어졌을 때, 두 문자열이 같은지 체크.

- `#`은 이전 문자를 하나 지움.

### # 해결

- 각 문자열의 문자 하나씩 체크한다. (반복문)
  - 조건 1, `#` 인 경우 이전 문자열 제거
  - 조건 2, 그 외 문자인 경우 리스트에 추가
- `O(M+N)`

![image](https://user-images.githubusercontent.com/40231980/62843023-b61ced00-bcf1-11e9-8c6a-ffaa7bcccfde.png)
