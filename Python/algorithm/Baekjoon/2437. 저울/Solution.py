import sys
 
N = int(input())
weights = sorted(map(int, sys.stdin.readline().strip().split()))

cnt = 0
memo = weights[:]

for i in range(N):
    if (weights[i] > cnt + 1):
        break
    cnt += weights[i]

print cnt + 1