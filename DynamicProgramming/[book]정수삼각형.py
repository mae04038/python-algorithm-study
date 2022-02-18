n = int(input())  # 정삼각형의 크기
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):  # 둘째줄부터 확인
        # 1.왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        # 2.바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        # 최대 합 저장
        dp[i][j] = dp[i][j] + max(up, up_left)

print(max(dp[n-1]))
