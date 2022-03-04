from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


array = [[] for _ in range(10001)]  # 모든 단어를 길이마다 나누어서 저장
reversed_array = [[] for _ in range(10001)]  # 모든 단어를 길이마다 나누어서 뒤집어 저장


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)  # 단어를 삽입
        reversed_array[len(word)].append(word[::-1])  # 단어를 뒤집어서 삽입

    for i in range(10001):  # 이진 탐색을 위해 단어리스트 정렬시키기
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:  # 쿼리 하나씩 확인
        if q[0] != '?':  # 접미사에 와일드카드가 있는 경우
            res = count_by_range(array[len(q)], q.replace(
                '?', 'a'), q.replace('?', 'z'))
        else:  # 접두사에 와일드카드가 있는 경우
            res = count_by_range(
                reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-10].replace('?', 'z'))

        answer.append(res)
    return answer
