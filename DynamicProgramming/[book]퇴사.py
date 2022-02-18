n = int(input())
t = []  # 상담을 완료하는데 걸리는 기간
p = []  # 상담을 완료했을 때 받을 수 있는 수익
dp = [0]*(n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 뒤에서부터 확인
# dp[i] : i번째 날부터 마지막 날까지 낼 수 있는 최대 이익.
for i in range(n-1, -1, -1):  # i: 6 5 4 3 2 1 0
    time = t[i] + i
    print(i)

    if time <= n:  # 현재까지의 최고 이익 계산
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
