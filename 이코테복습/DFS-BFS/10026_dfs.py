'''
적록색약이 아닌 사람이 봤을 때의 구역의 개수랑
적록색약인 사람이 봤을 때의 구역의 개수 출력
'''


def dfs(x, y, type):  # type:적록색맹인지 정상인지
    done.append((x, y))  # 방문 완료 위치 넣어주기.

    # 4가지 방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n) and (0 <= ny < n) and ((nx, ny) not in done):
            # 아직 방문하지 않은 곳일 경우
            if type == 0 and paint[nx][ny] == paint[x][y]:  # 같은 색일 경우
                dfs(nx, ny, 0)
            elif type == 1 and paint[nx][ny] == paint[x][y]:
                dfs(nx, ny, 1)


n = int(input())
paint = []
for _ in range(n):
    paint.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 정상인의 경우, 각각의 위치 다 확인
done = []
cnt1 = 0
for i in range(n):
    for j in range(n):
        # 방문하지 않은 곳일 때
        if (i, j) not in done:
            dfs(i, j, 0)
            cnt1 += 1

# 적록색맹의 경우
done = []
cnt2 = 0
for i in range(n):
    for j in range(n):
        # 방문하지 않은 곳일 때
        if (i, j) not in done:
            dfs(i, j, 1)
            cnt2 += 1

print(cnt1, cnt2)
