# Letter Case Permutation

[leetcode](https://leetcode.com/problems/letter-case-permutation/) (2019.07.30)

![image](https://user-images.githubusercontent.com/40231980/62018214-afbc4a80-b1f4-11e9-9707-4d622c7315cc.png)

### # 문제

주어진 문자열 `S`의 모든 문자를 대문자/소문자로 치환하여 만들 수 있는 모든 문자열 반환.

### # 해결

- 맨 처음에 모든 문자를 소문자로 바꾼 값을 결과에 넣어준다.
- 문자열을 돌면서 해당 인덱스 값이 문자인 경우 대문자로 치환해준 후 결과에 넣어준다.
  - 결과를 돌면서 모든 결과에 현재 인덱스를 대문자로 바꾼 값을 추가해 준다.

![image](https://user-images.githubusercontent.com/40231980/62018196-a0d59800-b1f4-11e9-8f41-fae6c3101edd.png)
