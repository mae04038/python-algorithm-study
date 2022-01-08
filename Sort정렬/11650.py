n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
array.sort(key=lambda array: (array[0], array[1]))
for i in array:
    print(i[0], i[1])
