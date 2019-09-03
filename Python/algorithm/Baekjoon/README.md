# Baekjoon(백준)

### :point_right: https://www.acmicpc.net/

## # Python2 입력 방법

- 값이 한 줄에 `1개`인 경우

```python
N = int(input())
```
```python
N = raw_input()
```

- 값이 한 줄에 `여러 개(리스트)`인 경우

```python
import sys
A = map(int, sys.stdin.readline().strip().split())
```
