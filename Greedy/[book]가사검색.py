words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

answer = []
result = False  # 검색가능한지 여부

for keyword in queries:  # 키워드 별
    query = list(keyword)
    cnt = 0  # 매칭단어개수
    cntTrue = 0
    cntFalse = 0
    cntResult = 0
    for i in range(len(words)):  # 단어별로 검색가능한지 확인
        word = list(words[i])
        if len(word) != len(query):  # 길이가 다르면 검색불가
            # print(i, "번째 단어 검색 불가")  # 지우기
            continue
        else:  # 단어길이 같을 때
            # print(i, "번째 단어 검색 가능")  # 지우기
            for j in range(len(word)):
                if query[j] != '?':  # ?가 아닐 때, 글자가 같은지 확인
                    if word[j] == query[j]:
                        cntTrue += 1  #
                    else:  # 글자가 다르면 검색 불가
                        continue
                else:  # ?이면 다음 글자가 같은지 확인
                    cntResult += 1  # ?개수
                    continue
            ##print(i, "번째 cntTrue : ", cntTrue, "cntResult: ", cntResult)
            if cntTrue == (len(word)-cntResult):
                cnt += 1
            cntTrue = 0
            cntResult = 0

    answer.append(cnt)

print(answer)
