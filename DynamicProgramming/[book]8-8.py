n, m = map(int, input().split())  # n:화폐 종류  m:가치의 합 ex)3 4
money = []  # 화폐 단위가 저장될 리스트
for _ in range(n):
    money.append(int(input()))
d = [10001] * (m+1)  # 일단 10001로 초기화. i-k를 만드는 방법이 존재하지 않는 경우
# DP bottom-up 반복문 사용 (여기서 k가 money[i])
d[0] = 0  # 가치의 합0을 만드는 데 사용되는 화폐 개수가 0이라는 의미
for i in range(n):  # 화폐의 종류 별로 ex)2, 3, , ...
    for j in range(money[i], m+1):  # ex) 2~4(화폐가 2원만 있을 때), 3~4(화폐가 3원있을때)
        if d[j - money[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - money[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
