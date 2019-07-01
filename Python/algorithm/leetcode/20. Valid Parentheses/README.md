# Valid Parentheses
[leetcode](https://leetcode.com/problems/valid-parentheses/) (2019.07.01)

![image](https://user-images.githubusercontent.com/40231980/60407529-21a17400-9bf6-11e9-8924-020c5ae1e804.png)


### # 문제
'(', ')', '{', '}', '[', ']' 로  이루어진 주어진 문자열의 유효한 문자열인지 체크하기.

    문자열 유효성 체크
        1. 열려 있는 괄호는 같은 타입의 괄호로 닫아야 한다.
        2. 열려 있는 괄호는 순서대로 닫아야 한다.


### # 해결
* 반복문을 돌며 문자열의 char 하나씩 stack에 쌓는다.
* 만약 닫는 괄호가 나오면 stack을 pop하여, 마지막 요소와 현재 괄호와 비교해서 일치하지 않는 경우 다시 stack에 넣어준다.
* 반복문을 다 실행한 후 stack에 문자가 남아있으면 False가 된다.

![image](https://user-images.githubusercontent.com/40231980/60407806-2286d580-9bf7-11e9-90fa-a635251ae66d.png)