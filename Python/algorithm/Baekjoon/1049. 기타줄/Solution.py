import sys
N, M = map(int, sys.stdin.readline().strip().split())

mCost = 1000 * 100
mMix = 1000 * 100
mOne = 1000 * 100
for _ in range(M):
    mix, one = map(int, sys.stdin.readline().strip().split())
    mMix = min(mix, mMix)
    mOne = min(one, mOne)

m, n = divmod(N, 6)
mCost = min(m * mMix + mOne * n, N * mOne, (m+1) * mMix )
print mCost
