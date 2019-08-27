import sys

T = int(input())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().strip().split())
    mok, remain = divmod(N-1, H)

    XX = str(mok+1).zfill(2)
    YY = remain + 1

    print ("{}{}".format(YY, XX))