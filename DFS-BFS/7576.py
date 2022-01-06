from collections import deque
m, n = map(int, input().split())  # m 가로, n 세로
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0  # 총 몇일 걸리는지 담을 변수

queue = deque([])
# queue에 처음 입력받은 토마토의 위치 좌표 append하기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

dx = [0, 0, 1, -1]  # 세로줄 나타냄 우 좌 하 상
dy = [1, -1, 0, 0]  # 가로줄 나타냄 우 좌 하 상


def bfs():  # 한번 들어가면 다 돌고 나오기 때문에 재귀할 필요X.

    while queue:
        x, y = queue.popleft()  # 처음 토마토 좌표x,y에 꺼내기.
        for i in range(4):  # 토마토 주변에 익힐 토마토 찾기.
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 토마토를 익히고 횟수 세기
                # 여기서 나온 제일 큰 값이 정답.
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])


bfs()
for i in graph:
    for j in i:
        # 다 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result-1)  # 처음 시작이 1이기 때문에 1 빼주기
