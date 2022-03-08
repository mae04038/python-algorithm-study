n = int(input())  # 전체 사람의 수
info = []
for _ in range(n):
    kg, cm = map(int, input().split())
    info.append((kg, cm))

result = []  # 등수 담는 리스트 변수

for i in range(n):
    cnt = 0  # 몇 명인지 세기
    for j in range(n):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            cnt += 1
    result.append(cnt+1)

for k in result:
    print(k, end=" ")
