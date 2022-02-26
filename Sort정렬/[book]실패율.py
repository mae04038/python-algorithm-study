def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N+1):
        # 해당 스테이지에 머물러 있는 사람 수
        cnt = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = cnt / length

        answer.append((i, fail))
        length -= cnt

    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]  # 스테이지번호만 출력

    return answer
