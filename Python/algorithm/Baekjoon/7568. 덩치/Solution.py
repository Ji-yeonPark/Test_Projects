import sys

N = int(input())

user = [map(int, sys.stdin.readline().strip().split()) for _ in range(N)]    

rList = []
for u1 in user:
    rank = 1

    for u2 in user:
        if u1 != u2 and u1[0] < u2[0] and u1[1] < u2[1]:
            rank += 1            
    rList.append(str(rank))
print " ".join(rList)
