from collections import deque

n, k = map(int, input().split())  # N: 크기 ,K: 바이러스종류 수

graph = []  # 전체 보드 정보를 담는 리스트
data = []  # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:  # 바이러스가 존재하면,
            # (바이러스 종류, 시간, 위치x, 위치y)
            data.append((graph[i][j], 0, i, j))

data.sort()  # 바이러스 종류 순대로 오름차순 정렬

q = deque(data)  # 큐 시작

target_s, target_x, target_y = map(int, input().split())  # (S, X, Y)입력받기

dx = [0, 0, -1, 1]  # 상 하 좌 우
dy = [-1, 1, 0, 0]
while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break

    # 현재노드에서 상하좌우 위치로 갈때 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:  # 이동 가능한 경우
            # 아직 바이러스가 없는 곳일때
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))
print(graph[target_x - 1][target_y - 1])
