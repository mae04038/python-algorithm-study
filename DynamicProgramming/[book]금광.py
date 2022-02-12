t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    n, m = map(int, input().split())  # 행, 열
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])  # 입력받은 리스트 행별로 나누기
        index += m

    # 다이나믹프로그래밍 진행 - 3가지 경우 다 구한다음 최댓값을 저장
    for j in range(1, m):  # 왼쪽에서 오는경우 3가지로 나눠서 진행해야하므로 세로 기준
        for i in range(n):
            # [왼쪽 위]에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # [왼쪽 아래]에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # [왼쪽]에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])  # 해당 행에서 가장 큰 값이랑 이전행에서 가장 큰값 비교.
    print(result)
