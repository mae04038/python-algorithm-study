from audioop import reverse


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # 오름차순 정렬 후 b의 내림차순과 짝 지어야 함.
decreaseB = sorted(b, reverse=True)

result = 0
for i in range(n):
    result += a[i]*decreaseB[i]
print(result)
