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


n, m = map(int, input().split())  # n:여행지의 수, m:여행계획에 속한 도시의 수
parent = [0] * (n+1)  # 부모테이블 초기화
edges = []

for i in range(1, n+1):  # 루트를 자기 자신으로 초기화
    parent[i] = i

for i in range(n):  # 연결정보 입력받기 - 한줄씩
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)  # 연결된 경우 합치기 연산

plan = list(map(int, input().split()))  # 여행계획 입력받기

result = True
for i in range(m-1):  # 계획에 속한 도시들의 루트가 모두 같은지 확인 (그래서 m-1)
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print("YES")
else:
    print("NO")
