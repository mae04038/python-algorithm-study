n, k = map(int, input().split())  # n: 물품의 수, k: 버틸 수 있는 무게
info = [[0, 0]]
for _ in range(1, n+1):
    info.append(list(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]  # dp[i][j] - j가 무게를 나타냄

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = info[i][0]
        value = info[i][1]

        if j < weight:  # 무게가 현재물건의 무게보다 작을 때 위의값 그대로 가져오기
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[n][k])


'''
	 가로는 물건, 세로는 무게인 2차원 배열
	 물건을 하나씩 추가하면서 무게가 j일때 넣을 수 있는 물건들의 가치의 합
	 dp[i][j]는 기본적으로 이전 아이템(이전 행)으로 해당 무게를 채울 수 있는 경우를 넣어준다.
	 ->우선 dp[i-1][j] 
	 무게(j)보다 넣어야 하는 물건의 무게가 작거나 같은 경우(다른 물건을 더 넣을 수 있는 경우)
	 -> dp[i][j] = Math.max(dp[i-1][j-tmp_W]+tmp_V, dp[i][j])
	 나머지 무게(j-해당행물건무게)만큼 넣을 수 있는 값을 더한 후, 현재 있는 값과 최대값 비교
     '''
