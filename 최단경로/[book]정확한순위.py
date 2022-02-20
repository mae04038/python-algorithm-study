INF = int(1e9)

n, m = map(int, input().split())  # n:학생 수, m:비교횟수
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):  # 자기 자신에서 자기 자신으로 가는 비용은 0
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):  # 정보 입력받고 1로 초기화
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
# 각 학생들 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1

print(result)
