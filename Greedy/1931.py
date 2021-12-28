n = int(input())  # n : 회의의 수
time_list = []
cnt = 0  # 최대 회의 개수
for _ in range(n):
    start, finish = map(int, input().split())  # 시작시간, 끝나는시간
    time_list.append([start, finish])

# 빨리 끝나는 회의 순서대로 정렬해야 한다.
time_list = sorted(time_list, key=lambda a: a[0])  # 시작시간 기준 정렬
# print(time_list)  # 확인용
time_list = sorted(time_list, key=lambda a: a[1])  # 끝나는시간 기준 다시 정렬
# print(time_list)  # 확인용

last = 0  # 회의의 마지막 시간을 저장

for i, j in time_list:  # i:시작시간, j:끝나는 시간
    if i >= last:  # 시작시간이 회의의 마지막 시간보다 크거나 같을 때 회의 가능
        cnt += 1
        last = j  # last가 해당 회의의 끝나느 시간으로 바뀜.
print(cnt)
