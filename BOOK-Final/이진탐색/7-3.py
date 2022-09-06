N, M = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
start, end = 0, data[-1]
mid = (start + end) // 2

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in range(len(data)):
        if data[i] > mid:
            result += data[i] - mid
    
    if result >= M: # 기준 높이기
        start = mid + 1
    else: # 기준 낮추기
        end = mid - 1

print(mid)