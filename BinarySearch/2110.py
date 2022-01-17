n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

start = 1  # 최소거리
end = house[-1] - house[0]  # 최대거리

result = 0
while start <= end:
    mid = (start+end) // 2  # 해당 gap
    old = house[0]  # 리스트의 가장 낮은 좌표
    count = 1  # 거리를 mid로 했을 때 가능한 집의 개수

    for i in range(1, len(house)):
        if house[i] >= old+mid:  # gap이상
            count += 1
            old = house[i]
    if count >= c:
        start = mid + 1
        result = mid  # 최대거리
    else:
        end = mid - 1
print(result)
