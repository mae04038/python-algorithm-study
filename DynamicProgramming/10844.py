n = int(input())  # n은 자릿수를 의미
MOD = 1000000000
# dp[자리수][앞에 오는 숫자]
dp = [[0]*10 for _ in range(n+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    for j in range(10):
        # 끝의 자리가 0
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:  # 끝의 자리가 9
            dp[i][j] = dp[i-1][8]
        else:  # 끝의 자리가 1~8
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[n]) % MOD)
