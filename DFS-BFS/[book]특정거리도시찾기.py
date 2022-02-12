from collections import deque

city, road, shortest, start = map(int, input().split())
graph = [[] for _ in range(city+1)]

# 모든 도로 정보 입력받기
for _ in range(road):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (city+1)
distance[start] = 0  # 출발도시까지의 거리는 0으로 초기화

# BFS 수행
q = deque([start])  # 큐 시작, 시작노드가 q
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)  # 큐에 넣기

# 최단 거리가 shortest인 모든 도시의 번호를 출력
check = False
for i in range(1, city+1):
    if distance[i] == shortest:
        print(i)
        check = True
# 최단 거리가 shortest인 도시가 없다면 -1출력
if check == False:
    print(-1)
