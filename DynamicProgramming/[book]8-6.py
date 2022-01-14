n = int(input())  # 식량창고의 개수
food = list(map(int, input().split()))
d = [0] * 100
# DP bottom-up방식 - 반복문 사용
d[0] = food[0]
d[1] = max(food[0], food[1])  # 한 개를 터는 경우
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+food[i])  # 현재 식량창고를 안 터는 경우 / 터는 경우

print(d[n-1])
