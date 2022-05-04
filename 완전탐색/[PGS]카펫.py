def solution(brown, yellow):
    answer = []
    y_sero, y_garo = 0, 0
    b_sero, b_garo = 0, 0

    if yellow == 1:
        answer = [3, 3]
        return answer

    if yellow % 2 != 0:  # yellow가 홀수인 경우
        for j in range(1, yellow//2 + 1, 2):
            if yellow % j == 0:
                y_sero = j
                y_garo = yellow / j

                if (y_garo+2+y_sero)*2 == brown:
                    b_sero = y_sero+2
                    b_garo = y_garo+2

        answer.append(b_garo)
        answer.append(b_sero)

        answer.sort(reverse=True)

        return answer

    for i in range(1, yellow//2 + 1):
        if yellow % i == 0:
            y_sero = i
            y_garo = yellow / i

            if (y_garo+2+y_sero)*2 == brown:
                b_sero = y_sero+2
                b_garo = y_garo+2

    answer.append(b_garo)
    answer.append(b_sero)

    answer.sort(reverse=True)

    return answer
