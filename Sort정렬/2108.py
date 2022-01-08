import sys
from collections import Counter
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

# 산술평균 - 다 더해서 / n
print(round(sum(array)/n))

# 중앙값 - 오름차순 -> 중간값
array.sort()
print(array[n//2])

# 최빈값 - 빈출
cnt_array = Counter(array).most_common()
# print("최빈값:", cnt_array)  # test
#최빈값: [(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)]
if len(cnt_array) > 1 and cnt_array[0][1] == cnt_array[1][1]:  # 최빈값 2개 이상
    print(cnt_array[1][0])
else:
    print(cnt_array[0][0])

# 범위 - 최댓값-최솟값
print(max(array)-min(array))
