# 1120
import sys
A, B = map(str, sys.stdin.readline().strip().split())

res = 50
for i in range(0, len(B)- len(A) + 1):
    cnt = 0
    for j in range(0, len(A)):
        if A[j] != B[j+i]:
            cnt += 1
    res = min(res, cnt)
print res