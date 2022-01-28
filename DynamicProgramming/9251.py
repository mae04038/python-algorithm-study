commonStr = []
commonStr.append(list(input()))
commonStr.append(list(input()))

h, w = len(commonStr[1]), len(commonStr[0])
dp = [[0] * (w+1) for _ in range(h+1)]
'''print(commonStr[0])
print(commonStr[0][1])'''

for i in range(1, h+1):
    for j in range(1, w+1):
        if commonStr[0][i-1] == commonStr[1][j-1]:  # 알파벳이 같을 때
            dp[i][j] = dp[i-1][j]+1
        else:  # 알파벳이 다를 때
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
