# Longest Palindromic Substring
[leetcode](https://leetcode.com/problems/longest-palindromic-substring/) (2019.06.25)

![스크린샷 2019-06-26 오전 12 14 21](https://user-images.githubusercontent.com/40231980/60110708-77fe5500-97a7-11e9-82ae-6e7237a12839.png)

### # 문제
주어진 문자열 s 에 부분 문자열 중 가장 긴 펠린드롬(뒤짚었을 때랑 같은 문자열)을 구하기.

### # 해결
* for 로 문자열 인덱스를 돌면서 문자열 비교함.<br/>
* `완전 탐색 알고리즘`방식으로 해결한 것 같음.
  * 모든 요소 전부 검사했기 때문에.
* `Time Limit Exceeded` 오류 해결을 위해 상단에 if 조건을 추가하여 아래와 같은 경우에는 바로 값을 리턴할 수 있도록 함.
  * 빈 문자열인 경우.
  * 1 글자인 경우.
  * 전체 문자열을 뒤짚었을 때 같은 경우.