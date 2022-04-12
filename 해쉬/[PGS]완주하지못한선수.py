'''
참가자 중에 동명이인이 있을 수 있음
-> value가 2 이상이면 동명이인이 value만큼 있다는 것.
-> 완주자 명단인 completion의 선수들 이름을 하나씩 돌면서
   value가 1이면 해당 key, value 삭제. 동명이인이 있어서 value가 
   2이상이면, 완주자 이름이 나올 때마다 -1 해주는 방식.
'''


def solution(participant, completion):
    hash = {}  # 딕셔너리 이용
    for i in participant:  # 해시 만들어주기- 이름을 key로 사용.
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    for i in completion:
        if hash[i] == 1:
            del hash[i]
        else:
            hash[i] -= 1

    answer = list(hash.keys())[0]  # 딕셔너리를 리스트로 바꾸고 가장 첫번째요소 리턴.(어차피 하나)

    return answer


participants = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participants, completion))
