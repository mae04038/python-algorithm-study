from collections import deque
import copy

n = int(input())  # 강의의 개수
indegree = [0] * (n+1)  # 모든 노드에 대한 진입차수는 0
graph = [[] for i in range(n+1)]
time = [0] * (n+1)  # 각 강의 시간 0으로 초기화

for i in range(1, n+1):  # 입력정보
    data = list(map(int, input().split()))
    time[i] = data[0]  # 첫번째 수는 시간 정보
    for x in data[1:-1]:  # 선수과목들
        indegree[i] += 1
        graph[x].append(i)

# 위상정렬 함수


def topology_sort():
    result = copy.deepcopy(time)  # 결과를 담을 리스트
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])  # now :큐에서 꺼낸것
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])


topology_sort()
