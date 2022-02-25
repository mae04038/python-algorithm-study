def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


home, road = map(int, input().split())  # home:집의 수, road: 도로의 수
parent = [0] * (home)  # 부모 테이블 초기화

edges = []  # 모든 도로를 담을 리스트
result = 0  # 최종 비용을 담을 변수

for i in range(home):
    parent[i] = i  # 부모 테이블 상에서, 부모를 자기 자신으로 초기화

# 각 도로의 정보 X Y Z : X번 집과 Y번 집 사이의 길이가 Z라는 의미
for _ in range(road):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 도로를 비용 순으로 정렬
edges.sort()
total = 0
# 도로를 하나씩 확인하며 사이클이 발생하지 않는 경우에만 집합에 포함.
for edge in edges:
    cost, a, b = edge
    total += cost
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total-result)
