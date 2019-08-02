# Find Minimum in Rotated Sorted Array

[leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (2019.08.02)

![image](https://user-images.githubusercontent.com/40231980/62338515-d12e7680-b513-11e9-94eb-3c7f90bc7296.png)

### # 문제

오름차순으로 정렬된 리스트에서 pivot(회전축)을 찾는 문제.

pivot(회전축)은 오른차순으로 진행되다가 갑자기 감소되다가 다시 증가하는 부분을 말한다.

> ![image](https://user-images.githubusercontent.com/40231980/62338685-5ade4400-b514-11e9-8bf9-da4c27721bff.png)
>
> 위 그림에서 2가 pivot값이 된다

### # 해결

Medium인데 엄청 쉬운 문제였다.

- 리스트를 돌면서 갑자기 감소되는 부분의 값을 반환하면된다.
- 감소되는 부분이 없는 경우 가장 첫번째 요소를 반환하면 된다.

![image](https://user-images.githubusercontent.com/40231980/62338527-dab7de80-b513-11e9-8267-e31750e5c7e9.png)

### # :question:

이 문제의 테스트 코드들이 좀 이상한 것 같다.  
아래와 같이 실행해도 성공하며, 결과값도 더 좋게 나온다.
```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
```
![image](https://user-images.githubusercontent.com/40231980/62339318-8e21d280-b516-11e9-84f3-7bbeb1a17a47.png)

### # 비슷한 문제

- [154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
  - 풀이와 답이 같다.
