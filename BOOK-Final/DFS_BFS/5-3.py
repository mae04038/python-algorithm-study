'''
0 : 구멍 뚫려 있는 부분
1 : 칸막이
'''
N, M = map(int, input().split()) # N: 세로, M: 가로
ice = [list(input()) for _ in range(N)]

ans = 0
visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0] # 세로
dy = [0, 0, -1, 1] # 가로


def dfs(x, y):
    ice[x][y] = 1 # 칸막이로 바꿔주기
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if ice[nx][ny] == '0': # 얼음일 때만 재귀 수행
            dfs(nx, ny)
    return


for i in range(N):
    for j in range(M):
        if ice[i][j] == '0': # 얼음일 때 dfs 수행
            dfs(i, j)
            ans += 1
print(ans)
