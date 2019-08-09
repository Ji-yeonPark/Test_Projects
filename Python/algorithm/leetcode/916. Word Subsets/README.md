# Word Subsets

[leetcode](https://leetcode.com/problems/word-subsets/) (2019.08.09)

![image](https://user-images.githubusercontent.com/40231980/62751290-1ae00980-ba9e-11e9-944c-19a9faeb4547.png)

### # 문제

`A`리스트 안에 문자열들 중 `B`리스트의 단어를 포함하는 문자열 반환.

> ### Test Code 1
>
> ```python
> A = ["amazon","apple","facebook","google","leetcode"]
> B = ["lo","eo"]
> ```
>
> 결과 : ["google","leetcode"]
>
> ### Test Code 2
>
> ```python
> A = ["amazon","apple","facebook","google","leetcode"]
> B = ["e","oo"]
> ```
>
> 결과 : ["facebook","google"]

### # 해결

- `B` 리스트에서 사용되는 알파벳 개수를 체크한다.
  - `B` 의 문자열들이 중복제거.
    - 예) "A", "A", "AB" 는 A가 중복되기 떄문에 "AB"만 검사해도 상관 없다.
- `A`를 검사하면서 `B` 알파벳이 모두 존재하는지 체크한다.

![image](https://user-images.githubusercontent.com/40231980/62672176-94abc080-b9d4-11e9-93db-27bb384aea6f.png)
