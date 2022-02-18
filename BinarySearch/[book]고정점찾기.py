# 이진탐색
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)


n = int(input())
array = list(map(int, input().split()))

index = binary_search(array, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)
