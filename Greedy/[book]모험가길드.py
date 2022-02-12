n = int(input())
x = list(map(int, input().split()))

x.sort()
result = 0
cnt = 0  # 현재 그룹에 포함된 모험가의 수
for i in x:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)
