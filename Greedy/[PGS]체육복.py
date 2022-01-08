def solution(n, lost, reserve):
    '''
    제한사항 
    1.여벌의 체육복을 가져온 학생의 수는 
    1명 이상 n명 이하이고 중복되는 번호는 없습니다.

    2.여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 
    있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 
    가정 하며, 남은 체육복이 하나이기에 다른 학생에게는 
    체육복을 빌려줄 수 없습니다.
    '''
    reserve_uniq = set(reserve) - set(lost)
    lost_uniq = set(lost) - set(reserve)

    for i in reserve_uniq:
        if i-1 in lost_uniq:
            lost_uniq.remove(i-1)
        elif i+1 in lost_uniq:
            lost_uniq.remove(i+1)

    return n - len(lost_uniq)
