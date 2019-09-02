import sys
N, K = map(int, sys.stdin.readline().strip().split())
coins = sorted([int(input()) for _ in range(N)], reverse=True)

cnt = 0
for coin in coins:
    if K % coin >= 0:
        cnt += K // coin
        K -= (K // coin) * coin
    if K == 0:
        break
print cnt