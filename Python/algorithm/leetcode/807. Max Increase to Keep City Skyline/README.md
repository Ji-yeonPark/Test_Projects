# Max Increase to Keep City Skyline

[leetcode](https://leetcode.com/problems/max-increase-to-keep-city-skyline/) (2019.07.08)

![image](https://user-images.githubusercontent.com/40231980/60785247-30a39b80-a18d-11e9-8cf7-10969aeddcf7.png)

### # 문제

건물의 높이를 올릴 수 있는 최대 총 합은 얼마인가?

### # 해결

> The skyline viewed from top or bottom is: [9, 4, 8, 7] -> 각 열에서 가장 큰 값 = A<br/>
> The skyline viewed from left or right is: [8, 7, 9, 3] -> 각 행에서 가장 큰 값 = B<br/> > <br/> > `gridNew[i][j] = A[j]와 B[i]중 작은 값`<br/>
> SUM(girdNew) - SUM(gird) 값을 구하면 된다.
