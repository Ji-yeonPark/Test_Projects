# Climbing Stairs

[leetcode](https://leetcode.com/problems/climbing-stairs/) (2019.07.24)

![image](https://user-images.githubusercontent.com/40231980/61757944-a51d4200-adfd-11e9-89ff-75988befa162.png)

### # 문제

N층까지 올라갈 수 있는 방법 횟수.<br/>
한 번에 1 또는 2층씩 올라갈 수 있다.<br/>

### # 해결 1 Brute Force

- `재귀호출`을 이용하여 계산한다.<br/>
- O(2^n)<br/>
- Time Limit Exceeded 발생<br/>

### # 해결 2 Recursion with Memoization

- `재귀호출`을 이용하여 계산하는 Brute Force와 방식이 비슷하다.<br/>
- 이전에 검색했던 값을 저장(`memo`)하여 다시 검색하지 않도록 하기 때문에 속도가 빠르다.
- O(n)<br/>

![image](https://user-images.githubusercontent.com/40231980/61758077-4a381a80-adfe-11e9-85da-3b8cc1bbbfda.png)

### # 해결 3 Dynamic Programming(동적계획법)

- `동적 계획법` 사용.<br/>
- O(n)

![image](https://user-images.githubusercontent.com/40231980/61758218-db0ef600-adfe-11e9-9e94-8e023a9adc2d.png)

### # 해결 4 Fibonacci Number

- `피보나치 수열` 사용.<br/>
- O(n) / O(1)

![image](https://user-images.githubusercontent.com/40231980/61758321-507ac680-adff-11e9-872d-ed544f388fae.png)

### # 해결 5 Binets Method

- `비네 방정식` 사용.<br/>
- O(logN) / O(1)
