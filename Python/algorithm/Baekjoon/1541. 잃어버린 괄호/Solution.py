nums = str(raw_input()).split('-')

res = 0
for i, n in enumerate(nums):
    if i == 0:
        for x in n.split('+'):
            res += int(x) 
    else:
        for x in n.split('+'):
            res -= int(x) 
print res