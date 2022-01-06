from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

case = int(input())  # 테스트 케이스의 개수

for _ in range(case):
    l = int(input())  # 테스판의 한 변의 길이
    cx, cy = map(int, input().split())  # 나이트가 현재 있는 칸
    fx, fy = map(int, input().split())  # 나이트가 이동하려고 하는 칸

    graph = [([0]*l) for i in range(l)]  # l x l 크기의 그래프(체스판) 만들기

    queue = deque()
    queue.append((cx, cy))
    graph[cx][cy] = 0  # 현재위치에서는 이동횟수가 0

    while queue:
        x, y = queue.popleft()
        if x == fx and y == fy:  # 나이트가 이동하려고 하는 칸이라면 종료
            break
        for i in range(8):  # 이동 가능 방향이 8가지임
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if graph[nx][ny] == 0:  # 이동가능
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    print(graph[fx][fy])
