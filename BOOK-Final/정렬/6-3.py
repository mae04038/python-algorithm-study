N = int(input())
data = {}
for _ in range(N):
    name, score = map(str, input().split())
    data[name] = int(score)

sorted_data = sorted(data.keys(), key=lambda x:data[x])

print(' '.join(sorted_data))