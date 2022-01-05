n = int(input())  # n x n 정사각형
graph = []
num = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]  # 세로 우 좌 하 상
dy = [1, -1, 0, 0]  # 가로 우 좌 하 상


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:  # 현재 노드가 1이라면
        global cnt
        cnt += 1
        graph[x][y] = 0  # 해당 노드 0으로 바꿔주기
        # 주변 노드 방문 (1인지 보기 위해)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True  # 방문가능
    return False  # 더이상 방문 불가. 단지 만들기 종료


cnt = 0
result = 0
# 탐색 시작 지점을 모르기 때문에 하나씩 돌면서 1인 지점에서 시작
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(cnt)
            result += 1
            cnt = 0  # 초기화 시켜줘야 새로운 단지의 집 개수를 셀 수 있음
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
