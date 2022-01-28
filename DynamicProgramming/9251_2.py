commonStr = []
commonStr.append(list(input()))
commonStr.append(list(input()))

l1, l2 = len(commonStr[0]), len(commonStr[1])

dp = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):  # ex)commonStr[1][0~5]랑 commonStr[0][0] , ..랑 비교
        if cnt < dp[j]:  # 누적 변수 값이 해당 위치의 dp값보다 작을 때
            cnt = dp[j]
        elif commonStr[0][i] == commonStr[1][j]:  # 알파벳이 같을 때
            dp[j] = cnt + 1
print(max(dp))

'''
h, w = len(commonStr[1]), len(commonStr[0])
dp = [[0] * (w+1) for _ in range(h+1)]
print(commonStr[0])
print(commonStr[0][1])

for i in range(1, h+1):
    for j in range(1, w+1):
        if commonStr[0][i-1] == commonStr[1][j-1]:  # 알파벳이 같을 때
            dp[i][j] = dp[i-1][j]+1
        else:  # 알파벳이 다를 때
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
'''
