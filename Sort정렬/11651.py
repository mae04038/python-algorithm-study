import sys
n = int(sys.stdin.readline())
array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))
array.sort(key=lambda array: (array[1], array[0]))
for i in array:
    print(i[0], i[1])
