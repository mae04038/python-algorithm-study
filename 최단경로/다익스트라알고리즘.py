from dis import dis
import sys
from turtle import distance
input = sys.stdin.readline
INF = int(1e9)

# n: 노드의 개수 , m:간선의 개수
n, m = map(int, input().split())
start = int(input())  # 시작노드 번호

graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 잇는 노드에 대한 정보
visited = [False] * (n+1)  # 방문한적있는지 체크
distance = [INF] * (n+1)  # 최단 거리 테이블 무한으로 초기화

# 모든 간선정보 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환


def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:  # 해당 노드에 연결되어있는 노드들j
        distance[j[0]] = j[1]  # (b,c)가 각각 j[0] j[1] -> b까지의 거리가 c

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()  # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
        visited[now] = True

        for j in graph[now]:  # 현재 노드와 연결된 다른 노드 확인
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("Infinity")
    else:
        print(distance[i])
