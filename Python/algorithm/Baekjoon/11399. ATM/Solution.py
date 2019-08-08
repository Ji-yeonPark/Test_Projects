import sys
_ = int(input())
COSTS = map(int, sys.stdin.readline().strip().split())
COSTS.sort()

for i in range(1, len(COSTS)):
    COSTS[i] += COSTS[i-1]
print sum(COSTS)