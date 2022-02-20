def find_parent(parent, x):
    if parent[x] != x:  # 루트 노드가 아니면 루트 찾을 때까지 재귀적 호출
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):  # 두 원소가 속한 집합 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


gate = int(input())  # 탑승구의 수
plane = int(input())  # 비행기의 수

parent = [0] * (gate+1)  # 부모테이블 초기화

for i in range(1, gate+1):
    parent[i] = i

result = 0
for _ in range(plane):
    data = find_parent(parent, int(input()))  # 입력받은 비행기의 탑승구 루트 확인
    if data == 0:  # 루트가 0이면 도킹 불가 -> 종료
        break
    union_parent(parent, data, data-1)  # 왼쪽 집합(작은 수들)하고 합치기
    result += 1
print(result)
