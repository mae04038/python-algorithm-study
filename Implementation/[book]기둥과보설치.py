def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥을 설치하는 경우
            # '바닥 위', '보의 한쪽 끝부분 위', '다른 기둥 위'일 때 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False  # 아니라면 거짓 반환
        elif stuff == 1:  # 보를 설치하는 경우
            # '한쪽 끝부분이 기둥 위', '양쪽 끝부분이 다른 보와 동시에 연결'일 때 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
        return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:  # 삭제하는 경우
            answer.remove([x, y, stuff])  # 일단 삭제한 뒤
            if not possible(answer):  # 가능한 구조물인지 확인 (ex.보가 중간에 혼자 떠있는건 불가능)
                answer.append([x, y, stuff])  # 가능한 구조물이 아니면 다시 설치
        if operate == 1:  # 설치하는 경우
            answer.append([x, y, stuff])
            if not possible(answer):  # 가능한 구조물인지 확인
                answer.remove([x, y, stuff])  # 가능한 구조물이 아니라면 다시 제거

    return sorted(answer)
