INF = int(1e9)

# 도시개수랑 버스노선입력받기
city = int(input())
bus = int(input())

graph = [[INF]*(city+1) for _ in range(city+1)]  # 초기화

for a in range(1, city+1):  # 자기자신으로 가는 비용은 0
    for b in range(1, city+1):
        if a == b:
            graph[a][b] = 0

# 각 노선 정보 입력받고 초기화
for _ in range(bus):
    a, b, cost = map(int, input().split())
    if cost < graph[a][b]:  # 가장 적은 비용을 저장
        graph[a][b] = cost

# 플로이드워셜알고리즘 수행
for k in range(1, city+1):
    for a in range(1, city+1):
        for b in range(1, city+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, city+1):
    for b in range(1, city+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
