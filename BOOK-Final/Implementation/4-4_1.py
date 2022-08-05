N, M = map(int, input().split()) # N세로 M가로
now_x, now_y, now_d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 1
cnt = 0 # 네 방향 확인
# 상 좌 하 우 -> 북 동 남 서
dx = [-1, 0, 1, 0] # 세로
dy = [0, 1, 0, -1] # 가로

def find_left():
    global now_d
    if now_d == 0:
        now_d = 3
    elif now_d == 1:
        now_d -= 1
    elif now_d == 2:
        now_d -= 1
    else:
        now_d -= 1

def can_visited(x, y):
    global data
    if data[x][y] == 0:
        return True
    else:
        return False
def can_back(dir):
    global now_x, now_y
    if dir == 0:
        now_x += dx[2]
        now_y += dy[2]
    elif dir == 1:
        now_x += dx[3]
        now_y += dy[3]
    elif dir == 2:
        now_x += dx[0]
        now_y += dy[0]
    else:
        now_x += dx[1]
        now_y += dy[1]

    if data[now_x][now_y] != 1:
        return True
    else:
        return False

while True:
    find_left()  # 입력받은 위치의 왼쪽방향
    if cnt == 4: # 한칸 뒤로 다시 반복문 but 뒤가 바다이면 break
        if can_back(now_d):
            continue
        else:
            break
    # print("왼쪽방향 확인 : ", now_d)
    next_x = now_x + dx[now_d]
    next_y = now_y + dy[now_d]
    # print("왼쪽 위치: ", next_x, next_y)

    if can_visited(next_x, next_y):
        now_x, now_y = next_x, next_y #왼쪽으로 한 칸 전진
        ans += 1
        data[now_x][now_y] = -1 # 이동한 위치 방문처리
        cnt = 0
    else:
        cnt += 1
        continue

print(ans)