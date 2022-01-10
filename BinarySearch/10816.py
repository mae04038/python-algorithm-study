n = int(input())  # 가지고 있는 카드의 개수
cards = list(map(int, input().split()))
cards.sort()
cardsDic = {}  # 키-밸류
for c in cards:
    if c not in cardsDic:
        cardsDic[c] = 1  # 초기엔 1
    else:
        cardsDic[c] += 1  # 딕셔너리에 존재하는 키일 경우 1씩 더해주기

m = int(input())
search = list(map(int, input().split()))

for i in search:
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end)//2
        if cards[mid] == i:
            break
        if cards[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    if cards[mid] == i:
        print(cardsDic[i], end=' ')
    else:
        print(0, end=' ')


'''
def binarySearch(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return array[start:end+1].count(target)
    elif array[mid] > target:
        return binarySearch(array, target, start, mid-1)
    else:
        return binarySearch(array, target, mid+1, end)


for i in range(m):
    result = binarySearch(search, i, 0, n-1)
    if result != None:
        print(result, end=' ')
    else:
        print(0, end=' ')
'''
