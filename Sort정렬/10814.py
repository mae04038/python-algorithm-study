n = int(input())
array = []
for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    array.append((age, name))
array.sort(key=lambda array: (array[0]))
for i in array:
    print(i[0], i[1])
