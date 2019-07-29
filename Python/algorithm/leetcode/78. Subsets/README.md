# Subsets

[leetcode](https://leetcode.com/problems/subsets/) (2019.07.29)

![image](https://user-images.githubusercontent.com/40231980/62017666-7a166200-b1f2-11e9-9a04-6d8277169890.png)

### # 문제

중복 없는 숫자 리스트 `nums`를 갖고 만들수 있는 모든 subsets(부분 집합) 반환

### # 해결

- 결과를 담을 `res`배열을 반복문을 돌면서 기존 값에 새로운 숫자를 합친 값을 다시 `res`에 넣어준다.

![image](https://user-images.githubusercontent.com/40231980/62017656-72ef5400-b1f2-11e9-80fd-2d15148ddb14.png)
