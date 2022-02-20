import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
# 좌 하 우 상
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = int(input())  # 테스트케이스 개수
for tc in range(t):
    n = int(input())  # 노드의 개수

    # 전체 맵 정보 입력받기
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    # 최단 거리 테이블 초기화
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0  # 시작위치는 (0, 0)
    # 시작노드로 가기 위한 비용은 (0, 0)위치의 값->큐에 넣기
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    # 다익스트라
    while q:  # 큐가 빌 때까지 반복
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있으면 무시
        if distance[x][y] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])
