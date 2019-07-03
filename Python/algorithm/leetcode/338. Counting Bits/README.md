# Counting Bits
[leetcode](https://leetcode.com/problems/counting-bits/) (2019.07.03)

![image](https://user-images.githubusercontent.com/40231980/60407529-21a17400-9bf6-11e9-8924-020c5ae1e804.png)


### # 문제
0 <= i <= num 범위의 모든 10진수를 2진수로 바꾼 후 1 개수 카운트하기

    ex) Input: 5
        Output: [0,1,1,2,1,2]

        풀이:
            0 -> 0000 -> 0
            1 -> 0001 -> 1
            2 -> 0010 -> 1
            3 -> 0011 -> 2
            4 -> 0100 -> 1
            5 -> 0101 -> 2
            -----------------
                    결과 [0, 1, 1, 2, 1, 2]


### # 해결 1 ( solution 1 )
* 반복문을 돌면서 모든 10진수에 대한 2진수 값을 구한 후 1의 개수를 카운팅 한다.

### # 해결 2 ( solution 2 )
* 10진수에서 2진수의  1 개수 구하는 방법은 `10진수 % 2 + (10진수/2)의 1의 개수` 값과 동일하다.
* 그래서 `(10진수/2)의 1의 개수`를 구할 때마다 리스트에 넣어준 후 해당 값을 불러오는 방식으로 해결할 수 있다.
    ex) Input: 3
            Output: [0,1,1]

            풀이:
                0 -> 0 % 2 + ((0/2)의 1 개수)
                1 -> 1 % 2 + ((1/2)의 1 개수)
                2 -> 2 % 2 + ((2/2)의 1 개수)
                3 -> 3 % 2 + ((3/2)의 1 개수)
                -----------------
                        결과 [0, 1, 1]