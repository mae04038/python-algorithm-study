def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        result = array[i-1:j]
        result.sort()
        answer.append(result[k-1])

    return answer
