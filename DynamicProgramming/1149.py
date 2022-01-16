n = int(input())  # 집의 개수
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))
result = 0  # 최종 비용

dp = [0] * 1001
dp[1] = min(cost[0])
print(dp[1])
