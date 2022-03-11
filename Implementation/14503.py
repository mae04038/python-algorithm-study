
n, m = map(int, input().split())  # 가로, 세로
x, y, direction = map(int, input().split())  # (r, c)좌표 , 바라보는방향 d
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))

# 청소기 방문 여부 지도 표시
cleaner_move_map = [[0] * m for _ in range(n)]
cleaner_move_map[x][y] = 1  # 현재 좌표 방문 처리

# 청소기 이동방향 - 북, 동, 남, 서 d: 0 1 2 3순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소기 왼쪽으로 회전


def turn_left():
    global direction  # 0, 1, 2, 3만 가능
    direction -= 1  # 왼쪽으로 이동
    if direction == -1:
        direction = 3


cnt = 1  # 처음 위치를 청소했으므로 1
turn_time = 0  # 왼쪽방향으로 회전하는 횟수 계산, 4번 다 회전한 경우 다른 조건 실행
while True:
    turn_left()  # 왼쪽 방향으로 회전
    # 이동하려는 청소기의 위치
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 청소기가 이동하려는 칸이 청소하지 않았고 빈 칸인 경우, 청소가능(방문가능)
    if cleaner_move_map[nx][ny] == 0 and map_data[nx][ny] == 0:
        # 이동하려는 칸 청소
        cleaner_move_map[nx][ny] = 1
        # 청소한 칸 추가
        cnt += 1
        # 청소기 위치 업데이트(이동했기 때문에)
        x, y = nx, ny
        # 회전 횟수 초기화
        turn_time = 0
        continue
    else:
        # 이외의 경우, 회전 횟수만 증가시키기
        turn_time += 1

    # 4가지 방향 다 돌았는데 청소할 구역이 없는 경우,
    # 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
    else:
        # 그렇지 않을 경우
        break
    turn_time = 0  # 회전횟수 초기화

print(cnt)
