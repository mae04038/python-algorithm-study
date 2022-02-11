import heapq
import sys
from turtle import distance
input = sys.stdin.readline
INF = int(1e9)
# N:도시의 개수, M: 통로의 개수,  start:메시지를 보내고자 하는 도시
n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 있는 정보를 담는 리스트

distance = [INF] * (n+1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):  # 모든 간선 정보 입력받기
    x, y, z = map(int, input().split())  # x에서 y로 가는 비용이 z
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작노드로 가기 위한 최단경로는 0으로 설정
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]  # i[1]은 비용 (z값)
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # i[0]은 y값 (도시), 최단거리리스트 갱신
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

cnt = 0  # 도달할 수 있는 도시의 개수
max_distance = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt-1, max_distance)  # 시작노드제외 -> cnt -1
