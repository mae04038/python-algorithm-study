n = int(input())
array = list(map(int, input().split()))

dp = [0] * len(array)  # 연속된 수의합 저장
dp[0] = array[0]

for i in range(1, n):
    dp[i] = max(array[i], dp[i-1]+array[i])
print(max(dp))

'''for i in range(1, n):
    tmp = dp[i-1]+array[i]
    if tmp > dp[i-1]:
        dp[i] = tmp
    else:  # 안 커지면 0으로 바꿔주기
        dp[i] = array[i]
print(max(dp))'''
