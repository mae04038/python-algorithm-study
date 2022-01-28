n = int(input())  # 수열A의 크기
A = list(map(int, input().split()))

dp = [1] * n  # 자신을 포함하여 만들 수 있는 부분 수열크기 저장.

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:  # 증가해야하기 때문에0
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
