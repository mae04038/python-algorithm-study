n = int(input())
array = []
for _ in range(n):
    word = str(input())
    word_cnt = len(word)
    array.append((word, word_cnt))
# 중복 삭제
array = list(set(array))
# 단어 길이 정렬 -> 알파벳 정렬
array.sort(key=lambda array: (array[1], array[0]))

for i in array:
    print(i[0])
