n, k = map(int, input().split())  # n은 동전종류, k는 가치의 합
coin_type = []
for i in range(n):
    coin_type.append(int(input()))
cnt = 0
for coin in coin_type[::-1]:  # 역순으로 꺼내기
    if k >= coin:
        cnt += k//coin
        k %= coin
    else:
        continue
print(cnt)
