K = int(input())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0
total = 1000 - K 

for c in coins:
    if total % c >= 0:
        cnt += (total // c)
        total -= (total // c) * c
    if total == 0:
        break
print cnt
