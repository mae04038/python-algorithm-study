import sys  # '시간초과' 때문에 추가
input = sys.stdin.readline
n, m = map(int, input().split())  # n:나무의 개수 m:가져가려고하는 나무 길이
tree = list(map(int, input().split()))

start = 0
end = max(tree)
result = 0
while start <= end:
    total = 0
    mid = (start+end)//2  # 절단기 높이
    for x in tree:
        if x > mid:
            total += x-mid  # 얻을 수 있는 나무의 길이
    if total < m:  # 잘려진 길이가 m에 못미쳤을때
        end = mid - 1  # 절단기 높이를 낮춰야함.
    else:  # 잘려진 길이가 m보다 클때, 최대한 덜 잘랐을 때가 정답
        result = mid
        start = mid + 1

print(result)
