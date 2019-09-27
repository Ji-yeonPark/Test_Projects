# Max Increase to Keep City Skyline

[leetcode](https://leetcode.com/problems/top-k-frequent-words/) (2019.09.27)

![image](https://user-images.githubusercontent.com/40231980/60785247-30a39b80-a18d-11e9-8cf7-10969aeddcf7.png)

### # 문제

`words`에서 가장 빈도수가 많은 글자 `K`만큼 뽑아내기.
단, 빈도수가 같은 경우, 알파벳 수가 작은 걸 먼저 선택한다.

### # 해결

- collections.Counter로 빈도수 계산 후 정렬
