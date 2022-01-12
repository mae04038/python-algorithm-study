k, n = map(int, input().split())  # 오영식이 이미 가지고 있는 랜선의 개수 k, 필요한 랜선 개수 n
array = []
for _ in range(k):
    array.append(int(input()))

start = 1
end = max(array)
result = 0
'''
if k == n:
    print(min(array))  # k와 n의 개수가 같으면 가지고 있는 랜선 중 가장 짧은 길이가 정답
'''
while start <= end:
    total = 0  # 만들 수 있는 랜선 개수
    mid = (start+end) // 2
    for x in array:
        total += x//mid  # 처음에 개수 구해보기
    if total >= n:  # 자른 개수n이 많으면 -> 더 크게 잘라야 함.
        start = mid + 1
    else:
        end = mid - 1
print(end)
