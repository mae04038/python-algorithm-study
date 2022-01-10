def binarySearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
search = list(map(int, input().split()))
for i in search:
    result = binarySearch(array, i, 0, n-1)
    if result != None:
        print('1')
    else:
        print('0')
