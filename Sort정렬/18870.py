n = int(input())
array = list(map(int, input().split()))
# print(array)
result_array = list(sorted(set(array)))  # 중복 제거 후 정렬
dic = {result_array[i]: i for i in range(len(result_array))}
# print(dic)  # test
for i in array:  # 처음 입력 순서대로 출력
    print(dic[i], end=' ')
