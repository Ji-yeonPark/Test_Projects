N = int(input())
rope = sorted([int(input()) for _ in range(N)])

weight = 0
for i in range(N):
    weight = max(weight, rope[i] * (N-i))
print weight