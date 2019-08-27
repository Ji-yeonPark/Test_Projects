def check(N):
    A = 0
    while A < N:
        A += 1       
        if sum([int(x) for x in list(str(A))]) + A == N:
            return A
    return 0

print check(int(input()))