import sys
N, M, K = map(int, sys.stdin.readline().strip().split())

nMax = N // 2  # 여학생 기준으로 만들 수 있는 대회 팀 수
mMax = M       # 남학생 기준으로 만들 수 있는 대회 팀 수
res = 0        # 대회 나가고 남은 사람 수 
_max = 0       # 대회에 나갈 수 있는 최대 팀 수

# ..
# 여학생팀과 남학생 팀 중 작은 팀 수를 선택,
# 남은 학생 수 res 구함.
if nMax <= mMax:
    res = M - nMax + (N % 2)
    _max = nMax
else:
    _max = mMax
    res = N - (mMax * 2)

# ..
# 대회팀 생성 후 남은 학생 수가 K보다 큰 경우 그냥 _max 출력
# 그렇지 않은 경우, K - res 만큼 남은 학생 수를 3명(여2, 남1)으로 나눈 몫(+1)을 뺌
# +1은 나머지 값이 있는 경우에만 더함.
if res > K:
    print _max
else:
    K = K - res
    m, r = divmod(K, 3)
    if r > 0: m += 1
    print _max - m