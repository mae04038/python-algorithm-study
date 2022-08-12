'''
현재위치 (1, 1) -> (0, 0)
출구 (N, M) -> (N-1, M-1)
괴물 있음 : 0
괴물 없음 : 1   괴물 없는 부분으로만 이동 가능
최소 이동칸의 개수 출력 : 이동할 때마다 더해주기, 출구값 출력
'''
from collections import deque

N, M = map(int, input().split()) # N: 세로 , M: 가로
miro = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        miro[i][j] = int(miro[i][j])
visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0] # 세로
dy = [0, 0, -1, 1] # 가로

def bfs(x, y):
    q = deque()
    q.append((x, y)) # 시작위치 넣어주기
    visited[x][y] = True
    while q:
        now_x, now_y = q.popleft()
        if now_x == N-1 and now_y == M-1: # 출구이면 break
            break
        for i in range(4): # 인접 위치 1 이면 큐에 넣어주기
            nx, ny = now_x + dx[i], now_y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or miro[nx][ny] == 0 or miro[nx][ny] != 1: # 범위 벗어나는 경우
                continue
            if miro[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True # 방문 처리
                miro[nx][ny] += miro[now_x][now_y]

    return miro[N-1][M-1]

print(bfs(0, 0))


