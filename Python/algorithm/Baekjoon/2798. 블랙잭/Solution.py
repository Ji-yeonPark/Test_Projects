import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))

arr = []
for i, comb in enumerate(combinations(cards, 3)):
    _sum = sum(comb)
    if _sum <= M:
        arr.append(_sum)

print sorted(arr)[-1]
