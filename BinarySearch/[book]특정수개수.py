def count_by_value(array, x):
    n = len(array)  # 데이터의 개수
    a = first(array, x, 0, n-1)
    if a == None:
        return 0
    b = last(array, x, 0, n-1)

    return b-a+1


def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid  # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    elif array[mid] >= target:  # 중간점 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
        return first(array, target, start, mid-1)
    else:  # 중간점 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        return first(array, target, mid+1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid  # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    elif array[mid] >= target:  # 중간점 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
        return first(array, target, start, mid-1)
    else:  # 중간점 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        return first(array, target, mid+1, end)


n, x = map(int, input().split())
array = list(map(int, input().split()))

cnt = count_by_value(array, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)
