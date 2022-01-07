import sys
n = int(input())

cnt = [0] * 10001

# for문 속에 append를 사용하면 메모리 재할당이 이루어져 메모리를 효율적으로 사용하지 못함.
for _ in range(n):
    cnt[int(sys.stdin.readline())] += 1

for i in range(10001):
    if cnt[i] != 0:
        for j in range(cnt[i]):
            print(i)
