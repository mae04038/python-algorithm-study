def sol1(answers):
    cnt = 0
    one1 = []
    for _ in range(2000):
        one1 += [1, 2, 3, 4, 5]
    for i in range(len(answers)):
        if answers[i] == one1[i]:
            cnt += 1
    return cnt


def sol2(answers):
    cnt = 0
    two = []
    for _ in range(1250):
        two += [2, 1, 2, 3, 2, 4, 2, 5]
    for i in range(len(answers)):
        if answers[i] == two[i]:
            cnt += 1
    return cnt


def sol3(answers):
    cnt = 0
    three = []
    for _ in range(1000):
        three += [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == three[i]:
            cnt += 1
    return cnt


def solution(answers):
    answer = []  # 리스트 형태로 리턴해야 함.

    answer.append(sol1(answers))
    answer.append(sol2(answers))
    answer.append(sol3(answers))

    result = list(
        filter(lambda x: answer[x] == max(answer), range(len(answer))))

    for i in range(len(result)):
        result[i] += 1

    return result
