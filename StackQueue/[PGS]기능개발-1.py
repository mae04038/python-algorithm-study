progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

answer = []
days = [(100 - progresses[i])//speeds[i] for i in range(len(progresses))]

front = 0
for i in range(len(days)):
    if days[i] > days[front]:
        answer.append(i - front)
        front = i
answer.append(len(days) - front)

print(answer)
