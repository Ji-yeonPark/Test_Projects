# Word Subsets

[leetcode](https://leetcode.com/problems/coin-change-2/) (2019.08.13)

![image](https://user-images.githubusercontent.com/40231980/62912314-9acde280-bdc2-11e9-8b73-6f96ac264ab5.png)

### # 문제

주어진 코인(`coins`)으로 `amount`를 만들 수 있는 방법 개수 반환.

### # 해결

- [70. Climbing Stairs](https://github.com/Ji-yeonPark/TIL/tree/master/Python/algorithm/leetcode/70.%20Climbing%20Stairs)와 비슷한 문제이다.
- DP (동적계획법)을 이용하면 쉽게 풀 수있다.
- 처음에 dp 리스트를 초기화 한 후 index 0에 1을 입력한다.
- 반복문을 돌면서 특정 코인 일 때, 몇 개가 필요한지 체크한다. <- 코드에 주석 확인

![image](https://user-images.githubusercontent.com/40231980/62912320-a15c5a00-bdc2-11e9-9374-8abb59fdc549.png)
