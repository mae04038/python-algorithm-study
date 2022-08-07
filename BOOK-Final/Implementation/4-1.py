N = int(input()) # 공간의 크기 - 공간을 벗어나는 움직임은 무시됨
plans = list(input().split())
data = [[1] * (N+1) for _ in range(N+1)] # 지도
now_x, now_y = 1, 1

# L R U D 순
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def beyond_range(nx, ny):
    if nx <= 0 or nx > N or ny <= 0 or ny > N:
        return True
    else:
        return False

for plan in plans:
    if plan == 'L':
        next_x, next_y = now_x + dx[0], now_y + dy[0]
        if beyond_range(next_x, next_y):
            next_x, next_y = now_x, now_y
    elif plan == 'R':
        next_x, next_y = now_x + dx[1], now_y + dy[1]
        if beyond_range(next_x, next_y):
            next_x, next_y = now_x, now_y
    elif plan == 'U':
        next_x, next_y = now_x + dx[2], now_y + dy[2]
        if beyond_range(next_x, next_y):
            next_x, next_y = now_x, now_y
    else:
        next_x, next_y = now_x + dx[3], now_y + dy[3]
        if beyond_range(next_x, next_y):
            next_x, next_y = now_x, now_y

    now_x, now_y = next_x, next_y # 현재 위치 바꿔주기

print(next_x, next_y)

