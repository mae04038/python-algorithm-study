from itertools import permutations


def isSosu(number):

    # 소수인지 확인
    if number == 1 or number == 0:
        return False
    for i in range(2, number//2+1):
        if number % i == 0:
            return False
    return True


def makeNumber(numList):
    finalNum = ''
    for i in range(len(numList)):
        finalNum += numList[i]
    return finalNum


def solution(numbers):
    answer = 0
    numbersList = list(numbers)  # 문자로 저장
    # numbersList = list(map(int, numbers))  # int형으로 저장
    finalList = []  # 숫사 조합을 저장하는 변수
    done = []  # 소수인지 확인한 숫자들 저장하는 변수

    for i in range(len(numbers)):
        finalList.append(list(permutations(numbersList, i+1)))

    # print(list(permutations(numbersList, 1)))
    # print(list(permutations(numbersList, 2)))
    # print(list(permutations(numbersList, 3)))
    # print(finalList)  # 튜플형태로 보임 -> 나중에 리스트로 바꿔줘야 함.

    for i in range(len(numbers)):
        for j in finalList[i]:
            # list(j)
            # print(list(j))  # 확인용
            finalNum = makeNumber(list(j))
            if int(finalNum) not in done:
                done.append(int(finalNum))
            # print("done리스트 ", done) # 확인용

    for num in done:
        # print(num) # 확인용
        if isSosu(num) == True:
            # print('T') # 확인용
            answer += 1

    return answer


numbers = "011"
print(solution(numbers))
