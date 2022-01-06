from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]  # 세로 우 좌 하 상
dy = [1, -1, 0, 0]  # 가로 우 좌 하 상


def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # 1. 탐색시작 노드를 큐에 삽입->방문처리
    while queue:
        x, y = queue.popleft()  # 2.큐에서 노드 꺼내기 (3. 반복)
        for i in range(4):  # 2-1. 해당 노드의 인접 노드 확인 (상,하,좌,우)
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:  # 이동 가능한 경우
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))  # 2-2. 방문하지 않은 노드 큐에 삽입
    return graph[n-1][m-1]


print(bfs(0, 0))
