n, m = map(int, input().split())  # 세로크기, 가로크기
data = []  # 초기 맵 리스트
tmp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵

for _ in range(n):  # 맵 입력
    data.append(list(map(int, input().split())))

# 4가지 이동경로 : 좌 상 우 하
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이우선탐색을 이용해 각 바이러스가 사방으로 퍼지도록 하기.


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상 하 좌 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:  # 맵 크기 내에 있어야하고
            if tmp[nx][ny] == 0:  # 빈칸이어야 가능
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                tmp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서의 안전영역 크기 구하기


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                score += 1
    return score

# 깊이우선탐색을 이용해 울타리를 설치하면서 매번 안전영역크기 계산


def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = data[i][j]

        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)

        # 안전영역최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)
