def solution(s):
    answer = len(s)

    # 단위: 1개~N/2개
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]  # 앞에서부터 해당step까지 문자 추출
        cnt = 1
        # 단위만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 문자열과 똑같다면 압축횟수 증가시키기
            if prev == s[j:j+step]:
                cnt += 1
            else:  # 압축 못하는 경우
                compressed += str(cnt)+prev if cnt >= 2 else prev
                prev = s[j:j+step]  # 상태 초기화
                cnt = 1  # 상태 초기화
        # 남아있는 문자열 처리
        compressed += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(compressed))

    return answer
