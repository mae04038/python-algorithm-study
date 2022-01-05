n = int(input())  # 컴퓨터의 수
m = int(input())  # 직접 연결된 컴퓨터 쌍의 수 (간선 수)
graph = [[] for _ in range(n+1)]
cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False] * (n+1)

cnt = 0


def dfs(graph, v, visited):
    global cnt
    visited[v] = True  # 현재 노드 방문 처리
    #print(v, end=' ')
    # 현재 노드와 연결되어 있는 노드들 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1


dfs(graph, 1, visited)
print(cnt)
