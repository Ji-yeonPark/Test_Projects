# 11399 ATM

[백준](https://www.acmicpc.net/problem/11399) (2019.08.08)

![image](https://user-images.githubusercontent.com/40231980/62609539-ee60ac00-b93c-11e9-9cd2-8cf061a35ce7.png)

### # 문제

돈을 인출하는데 필요한 시간의 찹의 최솟값을 구하시오.

사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 `Pi`분이다.

`[3, 1, 4, 3, 2]`은 `P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2`이 된다.

### # 해결

- `P`리스트를 오름차순으로 정렬한 후 누적 값 다시 P에 넣어 사람이 ATM에서 인출하는데 걸린 시간을 구한다.
- 리스트 각 인자들의 총 합을 출력한다.

![image](https://user-images.githubusercontent.com/40231980/62258708-66fbd000-b446-11e9-9bee-a41e3419a76b.png)
