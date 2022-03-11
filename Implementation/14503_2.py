import sys
input = sys.stdin.readline
# 북동남서 순 - 현재방향+3을 4로 나눈 나머지가 왼쪽 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def clean(x, y, d):
    global ans
    if a[x][y] == 0:  # 청소 가능할 때
        a[x][y] = 2
        ans += 1  # 청소한공간 1추가

    for _ in range(4):
        d_Left = (d+3) % 4  # 바라보는 방향의 왼쪽
        nx = x + dx[d_Left]
        ny = y + dy[d_Left]
        if a[nx][ny] == 0:  # 이동할 위치가 청소가능한 경우
            clean(nx, ny, d_Left)  # 방문해서 청소
            return
        d = d_Left  # 바라보는 방향 업데이트 해주기

    # 4방향 모두 이동할 수 없으면 후진할 수 있는지 확인
    d_Left = (d+2) % 4  # 후진 방향
    nx = x + dx[d_Left]
    ny = y + dy[d_Left]
    if a[nx][ny] == 1:  # 후진하려는 위치가 벽이면 종료, 이동할 수 있으면 다음 좌표 방향 입력
        return
    clean(nx, ny, d)


n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
clean(x, y, d)
print(ans)
