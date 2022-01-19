progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

answer = []
time, count = 0, 0

while len(progresses) > 0:
    if(progresses[0] + time*speeds[0]) >= 100:
        progresses.pop(0)  # 배포하면 리스트에서 빼줌.
        speeds.pop(0)
        count += 1  # 하나 뽑을 때 배포 개수 더해주기
    else:  # 100이 안되었을 때
        if count > 0:
            answer.append(count)
            count = 0  # 다시 세줘야 하기 때문에 0으로 초기화
        time += 1  # 누적계산
answer.append(count)

print(answer)
