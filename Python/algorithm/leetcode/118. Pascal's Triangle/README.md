# Pascal's Triangle

[leetcode](https://leetcode.com/problems/pascals-triangle/) (2019.07.25)

![image](https://user-images.githubusercontent.com/40231980/61839309-10cbe180-aec8-11e9-94d0-6c47caebc93e.png)

### # 문제

자연수 `numRows`가 주어졌을 때, 파스칼의 삼각형 구하기<br/>
![PascalTriangleAnimated2](https://user-images.githubusercontent.com/40231980/61839437-7cae4a00-aec8-11e9-96f2-19ebcb9fdc35.gif)

### # 해결

- Solution에 동적계획법을 이용하라고 했다.<br/>
- `numRows`만큼 반복문을 돌면서
  - tmp라는 임시 리스트 생성. (행 넘버만큼 0을 채운 리스트)
  - 리스트의 첫번째와 마지막 요소를 1로 설정한다.
  - 리스트에 0이 없을 때까지 반복문을 돌면서 합을 계산한다.

![image](https://user-images.githubusercontent.com/40231980/61839279-f42fa980-aec7-11e9-9991-52b0127bcea9.png)
