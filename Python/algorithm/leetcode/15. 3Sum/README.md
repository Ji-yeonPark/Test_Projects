# 3Sum
[leetcode](https://leetcode.com/problems/3sum/) (2019.06.26)

![스크린샷 2019-06-27 오전 1 11 28](https://user-images.githubusercontent.com/40231980/60196630-8cf6e900-9878-11e9-99d6-f7c79b577de6.png)


### # 문제
nums 리스트에서 3 요소를 합해서 0(a + b + c = 0)이 되는 유니크한 리스트 구하기.

### # 해결
* 주요 변수 설명.
  * 첫 번째 요소 인덱스 i, 두 번째 요소 인덱스 j , 세 번째 요소 인덱스 k 
  1) `i` 는 for 를 돌면서 순차적으로 증가한다.( 범위 : 0 ~ len(nums) - 1)<br/>
  2) `j` 는 `i + 1`부터 시작한다.<br/>
  3) `k` 는 `len(nums) - 1` 부터 시작한다.<br/>
  4) `target` 은 첫 번쨰 요소를 0으로 만들기 위해 필요한 값이다.
  5) `arr` 은 합이 0이 되는 리스트를 담는 리스트이다. (결과 값)
* 먼저 nums를 정렬해준다.
* i 가 증가하면서, j 와 k의 범위를 줄여가며 검사한다.
  * nums[j] + nums[k]  < -nums[i] 이면 j 인덱스 증가
  * nums[j] + nums[k]  > -nums[i] 이면 k 인덱스 감소
  * nums[j] + nums[k]  == -nums[i] 이면
    * 합이 0 이되는 경우이므로 결과 리스트에 추가한다.
    * j 인덱스 증가, k 인덱스 감소한다.


### # 오류
처음엔 [solution.1.py](https://github.com/Ji-yeonPark/TestProjects/blob/master/Python/algorithm/leetcode/15.%203Sum/solution.1.py) 처럼 풀었을 때, `Time Limit Exceeded`오류 발생했다.<br/>
15~16번 라인의 `if .. not in .. ` 부분이 `순차검색`이라 `O(n)`이 추가로 걸려 시간이 초과된 듯 하다.<br/>
