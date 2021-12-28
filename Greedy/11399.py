n = int(input())  # n은 사람 수
atmTime = list(map(int, input().split()))  # 각 걸리는 시간
atmTime.sort()
# print(atmTime) #확인용
for i in range(1, n):
    atmTime[i] = atmTime[i-1]+atmTime[i]

print(sum(atmTime))
