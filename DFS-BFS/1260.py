from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 노드 연결
    graph[a].append(b)
    graph[b].append(a)

    print("before SORT")  # test
    print(graph)  # test
    print(graph)  # test
    print("after SORT")  # test
    graph[a].sort()  # 1,2,3..노드 순서대로 각각 연결된 노드 확인하기 위해
    graph[b].sort()
    print(graph)  # test
    print(graph)  # test

visited = [False] * (n+1)  # 해당 노드를 방문했는지 확인용


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')  # 방문 노드 출력
    # 현재 노드와 연결된 다른 노드 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:  # not visited[i] = True 여야하므로 vsited[i]가 false
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    visited = [False] * (n+1)
    queue = deque([v])  # 큐 시작
    print("deque([v]) : ", queue)  # 시작 노드출력  확인용 - 나중에 삭제
    visited[v] = True
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력 (꺼내면서 출력)
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들 큐에 삽입.
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited)
print()
bfs(graph, v, visited)
