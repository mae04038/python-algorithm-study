n, m = map(int, input().split())  # 볼링공 개수, 공의 최대 무게
balls = list(map(int, input().split()))  # 공 정보

# 볼리공 무게 별로 몇개 있는지 담을 리스트
array = [0] * 11

for x in balls:
    # 각 무게에 해당하는 볼링공 개수 세기
    array[x] += 1

result = 0
for i in range(1, m+1):  # A가 선택하는 무게에 따라
    n -= array[i]  # B가 고를 수 있는 볼링공은 A가 선택한 공 제외.
    result += array[i] * n

print(result)
