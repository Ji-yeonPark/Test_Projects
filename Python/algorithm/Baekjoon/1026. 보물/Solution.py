# -*- coding: utf8 -+-
import sys

N = int(input())
A = map(int, sys.stdin.readline().strip().split())
B = map(int, sys.stdin.readline().strip().split())

answer = 0
while A:
    minA = A.pop(A.index(min(A))) # A에서 가장 작은 값
    maxB = B.pop(B.index(max(B))) # B에서 가장 큰 값

    answer += (minA * maxB)
print answer
