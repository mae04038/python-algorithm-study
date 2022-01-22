priorities = [2, 1, 3, 2]
location = 2
answer = 0  # 몇 번째로 인쇄되는지
m = max(priorities)
while True:
    now = priorities.pop(0)
    if m == now:
        answer += 1
        if location == 0:
            break
        else:
            location -= 1  # 위치 줄이기
        m = max(priorities)
    else:
        priorities.append(now)
        if location == 0:
            location = len(priorities) - 1
        else:
            location -= 1
print(answer)
