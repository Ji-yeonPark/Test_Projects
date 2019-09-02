import sys
N = int(input())
classes = [map(int, sys.stdin.readline().strip().split()) for _ in range(N)]
classes = sorted(classes, key=lambda t: t[0])
classes = sorted(classes, key=lambda t: t[1])

cnt = 0
start = 0
for cl in classes:
    if cl[0] >= start:
        start = cl[1]
        cnt += 1
print cnt
