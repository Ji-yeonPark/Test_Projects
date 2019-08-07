# Majority Element II

[leetcode](https://leetcode.com/problems/majority-element-ii/) (2019.08.07)

![image](https://user-images.githubusercontent.com/40231980/62591706-7332d200-b90b-11e9-8e52-2b0cb0ddb1cb.png)

### # 문제

리스트 `nums`애서 `n/3`이상 반복된 수 반환. ( n: 리스트의 길이 )

### # 해결

[169. Majority Element](https://github.com/Ji-yeonPark/TIL/tree/master/Python/algorithm/leetcode/169.%20Majority%20Element)와 비슷한 문제이다.

- collections의 defaultdict을 이용해서 얼만큼 반복되었는지 체크한다.
- 반복문을 이용해서 해당 숫자가 `len(nums) / 3` 보다 큰 경우 리스트에 넣는다.

![image](https://user-images.githubusercontent.com/40231980/62591759-a70df780-b90b-11e9-8683-8365e4da17c8.png)
