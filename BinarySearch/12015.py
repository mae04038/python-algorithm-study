n = int(input())
A = list(map(int, input().split()))

result = [0]  # 정답을 나타낼 가장 긴 증가하는 부분 수열


def binarySearch(target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if result[mid] < target:  # 중간점 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            start = mid + 1
        else:  # 중간점 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            end = mid - 1
    return start


for i in A:
    if result[-1] < i:
        result.append(i)
    else:
        result[binarySearch(i, 0, len(result)-1)] = i

print(len(result) - 1)
