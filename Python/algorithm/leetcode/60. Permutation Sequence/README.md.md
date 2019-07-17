# 60. Permutation Sequence

[leetcode](https://leetcode.com/problems/permutation-sequence/) (2019.07.17)

![image](https://user-images.githubusercontent.com/40231980/61341466-5877bb00-a881-11e9-9f29-6650c40fd388.png)

### # 문제

리스트 [1,2,3, ... , n] 은 n! 유니크한 순열을 갖음.
순열에서 K 자리 수로 만들 수 있는 모든 값을 나열하고, n번 째 값을 반환.<br/>

### # 해결 1

- factorial 리스트 `fac`을 만든다.
- n 숫자 리스트 `digits`를 만든다.
- n 만큼 반복문을 돌면서 숫자를 하나씩 뽑아낸다.

#### Example 2

    > INPUT: n = 4, k = 9
    > OUTPUT: "2314"

    - FAC = factorial 값 계산하려 리스트에 넣은 후 뒤집은 리스트
    1. 몫, 나머지 = divmod(k-1, FAC[0])
    2. 몫, 나머지 = divmode(1의 나머지값, FAC[1])
    3. 몫, 나머지 = divmode(2의 나머지값, FAC[2])
    4. 몫, 나머지 = divmode(3의 나머지값, FAC[3])

![image](https://user-images.githubusercontent.com/40231980/61341483-734a2f80-a881-11e9-8d6c-4b021bf707da.png)
