from turtle import distance

INF = int(1e9)  # 무한
n, m = map(int, input().split())  # n:회사 개수 m:간선 개수

graph = [[INF] * (n+1) for _ in range(n+1)]  # 2차원리스트 무한으로 초기화

for a in range(1, n+1):  # 자기자신으로 가는 비용은 0으로 초기화
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):  # 각 간선에 대한 정보 입력받기
    a, b = map(int, input().split())  # a와 b가 서로에게 가는 비용은 1
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())  # 입력마지막줄 : 거쳐갈 노드 x,도착지 k

for k in range(1, n+1):  # 플로이드워셜 알고리즘
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행 결과 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
