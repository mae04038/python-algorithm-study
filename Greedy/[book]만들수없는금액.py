n = int(input())  # 동전의 개수
won = list(map(int, input().split()))  # 화폐 단위 입력받기 N개.
won.sort()  # 오름차순으로 정렬

target = 1  # 특정금액
for x in won:
    if target < x:
        break
    target += x
print(target)
