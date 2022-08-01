# 원하는 행을 고르고 그 행에서 가장 작은 숫자를 뽑았을 때 그 작은 숫자에서 가장 큰 숫자를 뽑은 사람이 이기는 게임
N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

arr = []
for card in cards:
    arr.append(min(card))
print(max(arr))