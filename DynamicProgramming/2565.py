n = int(input())  # 두 전봇대 사이의 전깃줄의 개수
lineList = []
for _ in range(n):
    lineList.append(list(map(int, input().split())))

lineList.sort()

dp = [1] * n  # 가장 긴 증가하는 수열 구하기.
for i in range(n):
    for j in range(i):
        if lineList[i][1] > lineList[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
print(n-max(dp))
